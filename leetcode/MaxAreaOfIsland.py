from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        answer = 0
        
        COL, ROW = len(grid[0]), len(grid)
        direction = ((0,1),(1,0),(0,-1),(-1,0)) # weights : right, down, left, up
        hist = [[0 for c in range(COL)] for r in range(ROW)] # 1 : already found
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and hist[r][c] == 0:
                    hist[r][c] = 1
                    area = 1 # total size of this time
                    Q = deque([(r,c)])
                    
                    while Q: # BFS : find connected lands
                        cr, cc = Q.popleft()
                        
                        for d_r, d_c in direction:
                            nr = cr + d_r
                            nc = cc + d_c
                            if 0 <= nr < ROW and 0 <= nc < COL:
                                if grid[nr][nc] == 1 and hist[nr][nc] == 0:
                                        Q.append((nr, nc))
                                        hist[nr][nc] = 1
                                        area += 1
                    
                    answer = max(answer, area)
        
        return answer
