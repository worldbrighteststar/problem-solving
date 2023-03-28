from itertools import permutations

def solution(ability):
    answer = 0
    
    cases = permutations(range(0, len(ability)), len(ability[0]))
    
    for case in cases:
        temp = 0
        for i, student in enumerate(case):
            temp += ability[student][i]
        answer = max(answer, temp)
        
    return answer


















a = [[40, 10, 10], 
     [20, 5, 0],
     [30, 30, 30], 
     [70, 0, 70], 
     [100, 100, 100]]
print(solution(a) == 210) 