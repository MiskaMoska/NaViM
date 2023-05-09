# include "c_token.h"

namespace toksim{

    C_Token::C_Token(){}
    C_Token::C_Token(
        int token_num
    ):
        token_num(token_num),
        mode(SINGLE),
        upsample_h(1),
        upsample_w(1)
    {}

    void C_Token::merge(C_Token token){
        if(token.mode == UPSAMPLE){
            this->mode = token.mode;
            this->upsample_h = token.upsample_h;
            this->upsample_w = token.upsample_w;
        }
        this->token_num += token.token_num;
    }

    void C_Token::pop(C_Token token){
        this->token_num -= token.token_num;
    }
}
