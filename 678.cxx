#include <iostream>
#include <string>
#include <cassert>
using namespace std;

class Solution {
    public:
        bool checkValidString(string s) {
            int as_r = 0, as_l = 0;
            for(auto c : s) {
                if (c == '(')
                    as_r++, as_l++;
                else if (c == ')')
                    as_r--, as_l--;
                else
                    as_r--, as_l++;
                if(as_r < 0)
                    as_r = 0;
                if(as_l < 0)
                    return false;
            }
            return as_r == 0;
        }
};

int main()
{
    Solution  s;
    assert(s.checkValidString("()") == true);
    assert(s.checkValidString("(*))") == true);
    assert(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") == false);
    assert(s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*") == false);
}
