class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        fs = mii = 0
        for j in range(1, len(A)):
            i = j - 1
            mii = max(mii, A[i] + i)
            fs = max(mii + A[j] - j, fs)
        return fs
