
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # two index approach. one idx track the first unique element and the back_idx will to track the next non_duplicate element.
        front_idx = 0
        if len(nums) > 1:
            back_idx = 1
        else:
            return # 1 or 0 length array of nums. So, no need to check remove duplicates
        while back_idx < len(nums):
            while back_idx < len(nums) and nums[front_idx] == nums[back_idx]:
                back_idx = back_idx + 1
            
            if back_idx < len(nums):
                front_idx = front_idx + 1
                nums[front_idx] = nums[back_idx]

        remove_elements = len(nums) - front_idx - 1
        for i in range(remove_elements):
            nums.pop()
           


        