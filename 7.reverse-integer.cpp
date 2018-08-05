class Solution {
public:
    int reverse(int x)
    {
        int64_t r = 0;
        while (x) {
            r *= 10;
            r += x % 10;
            x /= 10;
        }
        if ((int32_t)r != r)
            return 0;
        return r;
    }
};
