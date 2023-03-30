`include "params.svh"

module cast_credit_counter #(
    parameter   isFC = 0, //is the FC start port or not
    parameter   [`NOC_WIDTH*`NOC_HEIGHT-1:0] FCdn = {(`NOC_WIDTH*`NOC_HEIGHT){1'b0}}, //FC destination nodes
    parameter   int FCpl = 16 //FC packet length
)( 
    input       wire                            clk,
    input       wire                            rstn, 

    input       wire                            fire, //input port fire
    input       wire        [1:0]               flit_type, //input port flit type

    input       wire        [31:0]              credit_upd[`NOC_WIDTH][`NOC_HEIGHT],
    output      wire        [31:0]              credit_cnt,

    input       wire                            pop, //consume credit only when popping

    // for credit logging
    output      var         int                 min_crd_x, min_crd_y
);

reg [31:0] cnt;
assign credit_cnt = cnt;
int min_crd;

int credit_inc[0:`NOC_WIDTH*`NOC_HEIGHT-1];
initial begin
    for(int i=0; i<`NOC_WIDTH*`NOC_HEIGHT; i++) begin
        credit_inc[i] = 0;
    end
end

function void update_credit();
    // update credit buffer
    for(int x=0; x<`NOC_WIDTH; x++) begin
        for(int y=0; y<`NOC_HEIGHT; y++) begin
            if(FCdn[y*`NOC_WIDTH+x]) begin
                if(credit_upd[x][y] > 0) begin
                    if(FCdn[y*`NOC_WIDTH+x]) begin
                        credit_inc[y*`NOC_WIDTH+x] = credit_inc[y*`NOC_WIDTH+x] + credit_upd[x][y];
                    end
                end
            end
        end
    end

    min_crd = 100000000;
    // record the minimum buffered credit among all destination nodes
    for(int i=0; i<`NOC_WIDTH*`NOC_HEIGHT; i++) begin
        if(FCdn[i]) begin
            if(credit_inc[i] < min_crd) begin
                min_crd = credit_inc[i];
                // record the bottleneck node that makes credit run out
                min_crd_x = i % `NOC_WIDTH;
                min_crd_y = i / `NOC_WIDTH;
            end
        end
    end

    if(min_crd > 0) begin // update credits
        cnt = cnt + min_crd;
        for(int i=0; i<`NOC_WIDTH*`NOC_HEIGHT; i++) begin
            if(FCdn[i]) begin
                credit_inc[i] = credit_inc[i] - min_crd;
            end
        end
    end

    if((flit_type == `HEAD) & pop & fire)
        cnt = cnt - FCpl + 2;
endfunction

always@(posedge clk or negedge rstn) begin
    if(~rstn) cnt <= `CAST_CREDIT_ALLOC;
    else if(~isFC) cnt = ~32'b0; //indicate this is not a FC start node
    else begin
        update_credit();
    end
end

endmodule
