"""
1. combinations
"""
from itertools import combinations

def solution(relation):
    answer = 0
    indexs = [i for i in range(1, len(relation[0]) + 1)] # column index
    candidate_list = []
    for i in indexs: # get all cases of combination (as indexs) 
        candidate_list = [set(i) for i in combinations(indexs, i)] + candidate_list
    
    def is_candidate_key(candidate):
        temp_candidate_key = []
        
        for each in relation: # each element [a, b, c, d]
            temp = []
            for index in candidate: # target indexs of elements 
                temp.append(each[index-1])
                
            if temp in temp_candidate_key:
                return False
            
            temp_candidate_key.append(temp)
            
        return True
        
    def delete_candidate_key(target): # delete other candidate keys including the target
        for candidate in candidate_list[:]:
            if (target & candidate) == target:
                candidate_list.remove(candidate)
        
    while candidate_list: # main loop
        candidate = candidate_list.pop()
        if is_candidate_key(candidate):
            answer += 1
            delete_candidate_key(candidate)
    
    return answer
