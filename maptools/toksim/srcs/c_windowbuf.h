# ifndef C_WINDOWBUF_H
# define C_WINDOWBUF_H
# include "c_typing.h"
# include "c_token.h"

using namespace std;

namespace toksim{

    class C_WindowBuf{
        public:
            vector<int> 
                size_i,
                size_i_np,
                size_o,
                ks,
                strides,
                pads;
        
            int ni, rptr, wptr;
            
            int need_token, released_token, max_buf;
            bool close, done;

            vector<vector<int>> buf;
            tuple<int, int, int, int> winpos;
            
            C_WindowBuf();
            C_WindowBuf(
                int xbar_num_ichan,
                vector<int> input_size,
                vector<int> output_size,
                vector<int> kernel_size,
                vector<int> strides,
                vector<int> pads
            );

            void _init_pads();
            void _update_max_buf();
            void add_token(C_Token token);
            tuple<int, int, int, int> win_pos();
            bool is_pad(int buf_y, int buf_x);
            void _release_data();
            C_Token try_slide();
            void echo_buf();
    };

}

# endif