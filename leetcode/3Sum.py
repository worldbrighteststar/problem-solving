class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    if [nums[i], nums[left], nums[right]] not in answer:
                        answer.append([nums[i], nums[left], nums[right]])
                    left += 1; right -= 1
                elif three_sum < 0:
                    left += 1
                else: # three_sum > 0
                    right -= 1

        return answer
