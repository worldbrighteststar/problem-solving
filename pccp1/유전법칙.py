from math import ceil

def solution(queries):
    genDict = {1:'RR', 2:'Rr', 3:'Rr', 4:'rr'}
    
    def dfs(number, currentType, currentGen):

        if currentGen <= 2:
            if currentGen == 1: return 'Rr'
            else: return  genDict[number]
        
        if currentType in ['RR', 'rr']:
            return currentType        
        
        totalNumOfChildren = 4 ** (currentGen - 1)
        childOrder = ceil(number / totalNumOfChildren * 4)
        newNumber = number - (childOrder - 1) * totalNumOfChildren / 4
        
        return dfs(newNumber, genDict[childOrder], currentGen - 1)
            
    answer = [dfs(query[1], 'Rr', query[0]) for query in queries]
        
    return answer








d = [[[4,  4**2]]]
print(solution(d[0]))