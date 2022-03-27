"""
1. To N-number funtion
"""
def solution(n, t, m, p):
    answer = ''
    max_n = 16
    number_format = [str(i) for i in range(0, 10)] \
        + [chr(ord('A') + i - 10) for i in range(10, max_n)]
    
    current_number = 0
    turn = 1
    p = 0 if p == m else p
    while True:
        n_num = toNNum(n, current_number)
        
        for digit_number in n_num:
            if turn % m == p:
                answer += number_format[digit_number]
                
                if len(answer) == t:
                    return answer
            
            turn += 1
        current_number += 1
            
def toNNum(n, number):
    """
    input : N(binary, octal, decimal, etc) (int), original number (int)
    output : N-number of number (string)
    """
    return toNNum(n, number//n) + [number%n] if number >= n else [number]