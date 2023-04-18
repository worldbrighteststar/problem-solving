from collections import defaultdict

def solution(input_string):
    alphaInfo = defaultdict(int)
    
    currentAlpha = ''
    for alpha in input_string:
        if alpha != currentAlpha: # new alphabet group
            alphaInfo[alpha] += 1
            currentAlpha = alpha # update current
    
    answer = [alpha for alpha in sorted(alphaInfo) if alphaInfo[alpha] > 1]

    return ''.join(answer) if len(answer) > 0 else "N"
