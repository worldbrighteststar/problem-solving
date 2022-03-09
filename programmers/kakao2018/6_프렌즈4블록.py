"""
1. Brute force
2. deque
"""
from collections import deque

def solution(m, n, board):
    answer = 0
    board = [deque([board[row][col] for row in range(m)]) for col in range(n)]
    weights = ((0,0),(0,1),(1,0),(1,1))
   
    def find_square():
        """
        input : (None)
        output : elements of every square (list)
        """
        indexs_of_every_square = set()
        for row in range(len(board) - 1):
            for col in range(len(board[0]) - 1):
                if board[row][col] == ' ': continue
               
                indexs_of_square = set([(row+w[0], col+w[1]) for w in weights])
                elements_of_square = set([board[row+w[0]][col+w[1]] for w in weights])
                if len(elements_of_square) == 1:
                    indexs_of_every_square.update(indexs_of_square)
                   
        return sorted(list(indexs_of_every_square), key=lambda x : x[1])
         
    def remove_block(elemets):
        """
        input : elements of every square (list)
        output : (None)
        """
        for el in elemets:
            del board[el[0]][el[1]]
            board[el[0]].appendleft(' ')
   
    while True:
        indexs_of_every_square = find_square()
        if len(indexs_of_every_square) == 0:
            return answer
        else:
            answer += len(indexs_of_every_square)
            remove_block(indexs_of_every_square)
