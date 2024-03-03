class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for i, n in enumerate(nums):
            print(n)
            m = target - n
            if m in a:
               return [a[m], i]
            a[n] = i
        # return a
        # num_indices = {}  # Dictionary to store indices of elements
        #
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in num_indices:
        #         return [num_indices[complement], i]
        #     num_indices[num] = i
        #
        # # If no solution found
        # return []

print(Solution().twoSum([3, 2, 4], 6))
