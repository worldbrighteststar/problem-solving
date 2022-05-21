from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        rvs_graph = defaultdict(lambda : [0]*(numCourses + 1))
        locked = [0]*(numCourses + 1)
        
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            rvs_graph[course][pre_course] = 1
            locked[course] = 1
        graph[numCourses] = [i for i in range(numCourses) if locked[i] == 0]
               
        def dfs(course):
            if sum(rvs_graph[course]) != 0:
                return
            
            locked[course] = 0
                
            for next_course in graph[course]:
                rvs_graph[next_course][course] = 0
                dfs(next_course)
        
        while sum(locked) > 0:
            possible_course_count = locked.count(0)
            dfs(numCourses)
            
            if possible_course_count == locked.count(0):
                return False
        
        return True
