from typing import List
"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

"""
def runningSum(nums: List[int]) -> List[int]:
    return [sum(nums[0:i+1]) for i in range(len(nums))]


"""
1431. Kids With the Greatest Number of Candies
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
"""

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    return [True if candies[i]+extraCandies >= max(candies) else False for i in range(len(candies))]

"""
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
def isMonotonic(A: List[int]) -> bool:
    if A[0]>A[-1]:
        A = A[::-1]
    if len(A)<2:
        return True
    for i in range(1,len(A)):
        if A[i] < A[i-1]:
            return False
    else:
        return True

"""
1502. Can Make Arithmetic Progression From Sequence
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
"""
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    res = arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i] - arr[i-1] != res:
            return False
    else:
        return True

"""
1331. Rank Transform of an Array
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

-Rank is an integer starting from 1.
-The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
-Rank should be as small as possible.
"""
def arrayRankTransform(arr: List[int]) -> List[int]:
    arr1 = sorted(list(set(arr)))
    mapping = {}
    count = 1
    
    for i in arr1:
        mapping[i] = count
        count += 1
    return [mapping[i] for i in arr]