"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[0:i+1]) for i in range(len(nums))]


"""
1431. Kids With the Greatest Number of Candies
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candies[i]+extraCandies >= max(candies) else False for i in range(len(candies))]