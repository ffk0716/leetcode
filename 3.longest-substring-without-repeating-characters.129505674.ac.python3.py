class Solution:
    def lengthOfLongestSubstring(self, s):
        cur_str = ""
        max_len = 0
        for c in s:
            i = cur_str.find(c)
            if i != -1:
                max_len = max(len(cur_str), max_len)
                cur_str = cur_str[i + 1:]
            cur_str += c    
        return max(len(cur_str), max_len)

