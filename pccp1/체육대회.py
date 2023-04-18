from itertools import permutations

def solution(ability):
    answer = 0
    
    cases = permutations(range(0, len(ability)), len(ability[0])) # all cases of selected students
    
    for case in cases:
        temp = 0
        for i, student in enumerate(case): # sum of each case
            temp += ability[student][i]
        answer = max(answer, temp)
        
    return answer
