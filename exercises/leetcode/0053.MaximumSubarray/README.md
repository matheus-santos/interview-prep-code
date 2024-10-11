# 53. Maximum Subarray

- Link: https://leetcode.com/problems/maximum-subarray
- Level: Medium
- Added in: 24-10-11
- Topics: Array, DivideAndConquer, DynamicProgramming

## Description

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

Obs.: a subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
```md
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2:
```md
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3:
```md
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```
 
Constraints:

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

**Follow up**: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 540ms (beats 59.46%) |
|           Memory | 24.52mb (beats 70.79%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 20m08s |
|  Resolution Time | 20m08s |
|          O Space | O(n) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

The naive approach is to do a double loop where i is the initial point,
j is the limit and the sum between i and j is the max sum for that range,
keeping only the max sum using by comparing current sum with new sum using 
`max(curr, sum)`. This should give us a O(nˆ2) result.

We know that we need a variable `curr` as a buffer to calculate the updated sum
and another variable `maxsum` as a carry-over that keeps the highest value found.

We can take advantage of Dynamic Programming to hold a buffer with the updated
calculation `currsum` and compare it with the current max value `maxsum` to keep
the highest value.

```py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        currsum = maxsum = nums[0]

        for num in nums[1:]:
            currsum = max(num, currsum + num)
            maxsum  = max(maxsum, currsum)

        return maxsum
```
