"""
1. String
2. Recursion
"""
def solution(p):
    if p == '': return p
    u, v, is_right = find_balance(p)
    
    if is_right == True:
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + u.replace('(','{').replace(')','(').replace('{',')')[1:-1]
    
def find_balance(s):
    """
    input : parentheses (string)
    output : [u, v, if u is right] (list)
    """
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(': cnt += 1
        else: cnt -= 1
        if cnt == 0: # s[:i+1] is balanced
            return [s[:i+1], s[i+1:], s[0] == '(']
