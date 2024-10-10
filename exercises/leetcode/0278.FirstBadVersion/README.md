# 278. First Bad Version

- Link: https://leetcode.com/problems/first-bad-version/description/
- Level: Medium
- Added in: 24-10-10
- Topics: BinarySearch, Interactive.

## Description

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version 
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

Example 1:

> Input: n = 5, bad = 4
> Output: 4
> Explanation:
> call isBadVersion(3) -> false
> call isBadVersion(5) -> true
> call isBadVersion(4) -> true
> Then 4 is the first bad version.

Example 2:

> Input: n = 1, bad = 1
> Output: 1

Constraints:

- `1 <= bad <= n <= 231 - 1`

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 12ms (beats 63.89%) |
|           Memory | 11.37mb (beats 98.42%) |

| Exercise results |        |
|-----------------:|:-------|
|      Brute Force | 10m00s |
|  Resolution Time | 20m44s |
|          O Space | O(1)   |
|           O Time | O(log n) |
|             BTTC | O(N)   |

### Solution

Applied binary search to find the first bad version.

```py
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 0
        r = n
        mid = (r - l) // 2

        while abs(r-l) > 1:

            if isBadVersion(mid): r = mid
            else: l = mid

            mid = l + (r - l) // 2

        return mid+1
```