"""
1. Counter
2. Sort
"""
from collections import Counter

def solution(N, stages):
    answer = {i : float(0) for i in range(1, N + 1)}
    stages = Counter(stages)
    reach_count = stages.get(N+1) if stages.get(N+1) is not None else 0
    
    for i in range(N, 0, -1):
        if stages.get(i) != None:
            reach_count += stages.get(i)
            answer[i] = stages.get(i) / reach_count

    return sorted(answer, key=lambda x : -answer[x])
