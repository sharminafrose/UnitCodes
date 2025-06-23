"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # two approaches to solve this problem:
        # 1. using collections.Counter to count the number of occurrences of each element and return
        # 2. Boyer-Moore voting algorithm (only works if the majority element appears more than n/2 times)

        # 1. using collections.Counter
        # counts = collections.Counter(nums)
        # return max(counts.keys())
        # time complexity = O(n)
        # space complexity O(n)

        # 2. need space complexity 0(1) -- solution: Boyer-Moore voting algorithm (only works if the majority elements appears more than n/2 times)
        # nice tutorial here: https://www.youtube.com/watch?v=n5QY3x_GNDg 

        candidate = nums[0]
        vote = 0
        for n in nums:
            if n == candidate:
                vote = vote + 1
            else:
                vote = vote - 1
                if vote == 0:
                    candidate = n
                    vote = 1


        return candidate
