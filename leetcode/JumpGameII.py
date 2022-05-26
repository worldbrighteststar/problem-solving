class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_count = [10000] * len(nums) # DP
        min_count[0] = 0 # first position
        
        for idx in range(len(nums)):
            for dist in range(1, nums[idx] + 1):
                if idx + dist < len(nums):
                    min_count[idx + dist] = min(min_count[idx + dist], min_count[idx] + 1)
        
        return min_count[-1]
