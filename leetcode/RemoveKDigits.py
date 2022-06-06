from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        answer = []
        num = deque(num)
        
        while k > 0 and num:
            if answer:
                while answer[-1] > num[0]: 
                    answer.pop()
                    k -= 1
                    if answer == [] or k == 0: break
            answer.append(num.popleft())
        
        for _ in range(k): # remove remain k
            answer.pop()
            
        answer += num
        
        return '0' if sum(map(int, answer)) == 0 else ''.join(answer).lstrip('0')
