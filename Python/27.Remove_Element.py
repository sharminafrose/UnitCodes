'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

# in-place constraint: we need to modify the nums array in-place without using extra space for another array. 
# # two pointer approach. ith idx and last idx swap if ith idx is the duplicate item. then remove the last duplicate item
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # checking and modifying the num
        

        for i, n in enumerate(nums):
            # remove last duplicate items
            while len(nums)> 0 and nums[-1] == val:
                nums.pop()
            
            # two pointer approach. ith idx and last idx swap if ith idx is the duplicate item. then remove the last duplicate item
            if len(nums)> 0 and i < len(nums):
                if n == val :
                    temp = nums[i]
                    nums[i] = nums[-1]
                    nums.pop()
                    # removed element found in the nums array
               
        return len(nums)

        

