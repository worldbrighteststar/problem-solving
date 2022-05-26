from collections import deque

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        Q = deque([i for i in range(1, n + 1)])
        
        while len(Q) > 1:
            for _ in range(k - 1):
                Q.append(Q.popleft())
            Q.popleft()
        
        return Q[0]
        
