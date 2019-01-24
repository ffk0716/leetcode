class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        grid = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                grid[x][y] = min(x + 1, y + 1, N - x, N - y);
        for x, y in mines:
            grid[x][y] = 0
            for s in range(int(x / 2) + 1):
                if s < grid[x - s][y]:
                    grid[x - s][y] = s
            for s in range(int((N - x)/2) + 1):
                if s < grid[x + s][y]:
                    grid[x + s][y] = s
            for s in range(int(y / 2) + 1):
                if s < grid[x][y - s]:
                    grid[x][y - s] = s
            for s in range(int((N - y)/2) + 1):
                if s < grid[x][y + s]:
                    grid[x][y + s] = s
        max_order = 0
        for x in range(N):
            for y in range(N):
                max_order = max(max_order, grid[x][y])
        return max_order 

