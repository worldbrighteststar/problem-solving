"""
1. String
"""
def solution(s):
    answer = len(s) 
    
    for weight in range(1, len(s) // 2 + 1):
        incode = '' # incoded result
        block = s[:weight]
        cnt = 1
        
        for i in range(weight, len(s) - weight + 1, weight): 
            if block == s[i:i+weight]: # incode
                cnt += 1
            else: 
                if cnt == 1: cnt = '*' # prevent to remove '1' when cnt is '1x..'
                incode += str(cnt) + block
                block = s[i:i+weight]
                cnt = 1
             
        if cnt == 1: cnt = '*'   
        incode += str(cnt) + block + s[i+weight:] # last incode and remaining string
        answer = min(answer, len(incode) - incode.count('*'))
                
    return answer
