""" 
1. PS
"""
from collections import defaultdict

def solution(board):
    answer = 0
    board = [len(board[0]) * [0] for _ in range(2)] + board # prevent out of range
    blocks = defaultdict(list) # blocks[block_number] = [(x1,y1), ...]
    rest_of_rectangle = defaultdict(list) # rest parts of rectangle
    
    for row in range(len(board)): # find all blocks
        for col in range(len(board[0])):
            if board[row][col] != 0:
                blocks[board[row][col]].append((row, col))
    
    for bl in blocks: # find rest_of_rectangle
        rest_of_rectangle[bl] = find_rest_of_blocks(blocks[bl])
        
    while True:
        cnt = 0 # the number of removed blocks
        keys = list(blocks.keys()) # remained blocks
        added_blocks = [] # can be filled in this loop
        
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] in blocks:
                    added_blocks += [(row-1, col), (row-2, col)]
                    break
                
        for bl in keys: # find rectangles
            flag = True
            
            for rest in rest_of_rectangle[bl]:
                if rest not in added_blocks: flag = False
                    
            if flag == True:
                cnt += 1
                del blocks[bl]
                
        if cnt == 0: return answer
        else: answer += cnt
    

def find_rest_of_blocks(block):
    """
    input : block info (list)
    output : rest part of rectangle (list), len(list) must be 2
    """
    default = [set([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]),
               set([(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)])]
    gap = (min(block, key=lambda x:x[0])[0], min(block, key=lambda x:x[1])[1])
    temp = set([(b[0]-gap[0], b[1]-gap[1]) for b in block])
    
    if len(default[0] - temp) == 2:
        return [(b[0]+gap[0], b[1]+gap[1]) for b in default[0] - temp]
    else:
        return [(b[0]+gap[0], b[1]+gap[1]) for b in default[1] - temp]
