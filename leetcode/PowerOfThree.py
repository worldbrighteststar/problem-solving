class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while True:
            if n == 0: return False
            if n == 1: return True
            n, remain = divmod(n, 3)  
            if remain != 0: return False
