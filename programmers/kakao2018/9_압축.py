"""
1. Hash map
"""
def solution(msg):
    answer = []
    index = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    
    ch_group = ''
    for ch in msg:
        ch_group += ch
        if index.get(ch_group) == None:
            answer.append(index[ch_group[:-1]])
            index[ch_group] = len(index) + 1
            ch_group = ch_group[-1]
            
    answer.append(index[ch_group])
    
    return answer
