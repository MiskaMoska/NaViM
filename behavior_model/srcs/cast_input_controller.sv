`include "params.svh"

module cast_input_controller #(
    parameter   isFC = 0, //is the FC start port or not
    parameter   FCpl = 16 //FC packet length
)(
    input       wire                            clk,
    input       wire                            rstn,   
    input       wire                            fifo_empty, //from input buffer
    input       wire        [`CN-1:0]           candidateOutVC, //from route_calculator
    output      wire        [`CN-1:0]           reqVC, //to vc_allocator, multi-bit possibly asserted
    input       wire        [`CN-1:0]           selOutVC, //from vc_allocator, multi-bit possibly asserted
    input       wire                            VCgranted, //from vc_allocator
    output      wire        [`CN-1:0]           selXBVC, //to crossbar
    input       wire        [1:0]               flit_type,
    input       wire                            flit_fire,
    input       wire        [15:0]              credit_cnt //from credit counter
);

reg [`CN-1:0]   outVC;
reg             outVCLock;

always@(posedge clk or negedge rstn) begin
    if(~rstn) begin
        outVCLock <= 1'b0;
        outVC <= 0;
    end else if(flit_fire & (flit_type == `TAIL)) begin
        outVCLock <= 1'b0;
        outVC <= 0;
    end else if(VCgranted) begin
        outVCLock <= 1'b1;
        outVC <= selOutVC;
    end
end

assign selXBVC = outVCLock ? outVC : 
                    VCgranted ? selOutVC : 5'b0;

assign reqVC = (flit_type == `HEAD) & (~outVCLock) & (~fifo_empty) & (isFC ? (credit_cnt > FCpl) : 1'b1) ? candidateOutVC : 0;
endmodule