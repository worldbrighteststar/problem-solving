"""
1.Handle string
"""
import re

def solution(dartResult):
    answer = [0] * 4
    SDT = {'S':1, 'D':2, 'T':3}

    times = re.findall(r'\d+[SDT][\*#]*', dartResult)
    for i, time in enumerate(times):
        each = re.split('([SDT])', time)
        answer[i+1] = int(each[0]) ** int(SDT[each[1]])
        if each[2] == '*':
            answer[i] *= 2;
            answer[i+1] *= 2;
        if each[2] == '#':
            answer[i+1] *= -1

    return sum(answer)

