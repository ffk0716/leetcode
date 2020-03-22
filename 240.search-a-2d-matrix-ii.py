#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])

        a = [0, 0]
        b = [m, n]
        if m == 0 or n == 0:
            return False

        def p():
            return
            print('=======', a, b)
            for y in matrix[a[1]:b[1]]:
                print(y[a[0]:b[0]])

        p()
        while b[1] != a[1] or b[0] != a[0]:
            s, e = a[0], b[0]
            r = a[1]
            while True:
                se = (s + e) // 2
                v = matrix[r][se]
                if v > target:
                    e = se
                elif v < target:
                    s = se
                else:
                    return True
                if e - s <= 1:
                    break
            b[0] = e
            p()

            s, e = a[1], b[1]
            c = a[0]
            while True:
                se = (s + e) // 2
                v = matrix[se][c]
                if v > target:
                    e = se
                elif v < target:
                    s = se
                else:
                    return True
                if e - s <= 1:
                    break
            b[1] = e
            p()

            s, e = a[0], b[0]
            r = b[1] - 1
            while True:
                se = (s + e) // 2
                v = matrix[r][se]
                if v > target:
                    e = se
                elif v < target:
                    s = se
                else:
                    return True
                if e - s <= 1:
                    break
            a[0] = e
            p()

            s, e = a[1], b[1]
            c = b[0] - 1
            while True:
                se = (s + e) // 2
                v = matrix[se][c]
                if v > target:
                    e = se
                elif v < target:
                    s = se
                else:
                    return True
                if e - s <= 1:
                    break
            a[1] = e
            p()

        return False


# @lc code=end

a = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
a = [[-5]]
s = Solution()

print(s.searchMatrix(a, -10))
