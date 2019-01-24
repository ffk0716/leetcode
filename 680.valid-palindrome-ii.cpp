class Solution {
    public:
        bool check(size_t start, size_t end, const string &s) {
            while (start <= end) {
                if (s[start] != s[end])
                    return false;
                start++;
                end--;
            }   
            return true;
        }   

        bool validPalindrome(const string &s) {
            size_t start = 0;
            size_t end = s.size() - 1;
            while (start <= end) {
                if (s[start] == s[end]) {
                    start++;
                    end--;
                    continue;
                }   
                return check(start + 1, end, s) || check(start, end - 1, s); 
            }   
            return true;
        }   

};
