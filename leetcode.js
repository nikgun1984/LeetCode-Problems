/*
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let total = 0;
    const lst = [];
    for(let i of nums){
        total += i;
        lst.push(total);
    }
    return lst;
};

/*
1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.

*/

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const maxNum = Math.max(...candies);
    const isGreatest = [];
    for(let i of candies){
        (i+extraCandies)>=maxNum?isGreatest.push(true):isGreatest.push(false);
    }
    return isGreatest;
};