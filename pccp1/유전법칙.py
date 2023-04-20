from math import ceil

def solution(queries):
    genDict = {1:'RR', 2:'Rr', 3:'Rr', 4:'rr'}
    
    def dfs(number, currentType, currentGen):
        
        if currentType in ['RR', 'rr']: # it has to be a first condition
            return currentType   
        
        if currentGen <= 2: # second condition
            if currentGen == 1: return 'Rr'
            else: return  genDict[number]
        
        totalNumOfChildren = 4 ** (currentGen - 1)
        childOrder = ceil(number / totalNumOfChildren * 4) 
        newNumber = number - (childOrder - 1) * totalNumOfChildren / 4

        return dfs(newNumber, genDict[childOrder], currentGen - 1)
            
    answer = [dfs(query[1], 'Rr', query[0]) for query in queries]
        
    return answer