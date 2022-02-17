"""
1.LRU algorithm
"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])

    def LRU(data):
        """
        input : input data (string)
        output : working time, hit 1 miss 5 (int) 
        """
        if cacheSize == 0: return 5
        
        hit = False
        if data in cache:
            cache.remove(data)
            hit = True
        
        if len(cache) == cacheSize:
            cache.popleft()

        cache.append(data)

        return 5 if hit == False else 1
    
    
    for city in cities:
        answer += LRU(city.lower())
        
    return answer
