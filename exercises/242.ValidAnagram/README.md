# 242. Valid Anagram

- Link: https://leetcode.com/problems/valid-anagram
- Level: Easy
- Added in: 24-10-06
- Topics: HashTable, String, Sorting

## Description

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 17ms (beats 98.14%) |
|           Memory | 11.83mb (beats 94.17%) |

| Exercise results |        |
|-----------------:|--------|
|      Brute Force | 00m48s |
|  Resolution Time | 01m00s |
| Complexity Space | O(N+C) |
|  Complexity Time | O(N)   |

### Solution

**Python3**

```py
class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # return sorted(s) == sorted(t)

    S = len(s)
    T = len(t)
    seen = {}
    
    for c in s:
      if c in seen: seen[c] += 1
      else: seen[c] = 1

    for c in t: 
      if c in seen: seen[c] -= 1
      else: return False
      if seen[c] == 0: del seen[c]
        
    return len(seen) == 0
```