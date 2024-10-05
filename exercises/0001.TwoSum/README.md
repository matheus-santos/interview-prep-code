# 1. Two Sum

- Link: https://leetcode.com/problems/two-sum/description/
- Level: Easy
- Added in: 24-10-04
- Topics: Array, HashTable

## Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- Only one valid answer exists.
 
**Follow-up**: Can you come up with an algorithm that is less than O(n2) time complexity?

## Solutions

### Solution 1: Using Hash Table

|                  |        |
|-----------------:|--------|
|  Resolution Time | 19m47s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N)   |

Using cache "diff" to create a key-value dict where key is the
different between target and current number. In the following 
loop we use  this cache to find the matching number and return
its indexes.

**Python3**

```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)
        diff = {}

        for (i, num) in enumerate(nums):
            diff[target - num] = i

        for (i, num) in enumerate(nums):
            if num in diff and i != diff[num]:
                return [i, diff[num]]

        return None
```