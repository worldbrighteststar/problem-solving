from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        graph = defaultdict(list) 
        conditions = [0] * numCourses # the number of incoming edges
        for course, prev_course in prerequisites:
            graph[prev_course].append(course)
            conditions[course] += 1
            
        Q = deque([i for i in range(numCourses) if conditions[i] == 0])
        
        while Q:
            course = Q.popleft()
            answer.append(course)
            
            for next_course in graph[course]:
                conditions[next_course] -= 1
                if conditions[next_course] == 0:
                    Q.append(next_course)
        
        return answer if sum(conditions) == 0 else []
