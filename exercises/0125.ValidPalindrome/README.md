# 125. Valid Palindrome

- Link: https://leetcode.com/problems/valid-palindrome
- Level: Easy
- Added in: 24-10-06
- Topics: TwoPointers, String

## Description

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```
 
Constraints:

- `1 <= s.length <= 2 * 105`
- s consists only of printable ASCII characters.

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 21ms (beats 91.84%) |
|           Memory | 13.96mb (beats 26.5%) |

| Exercise results |        |
|-----------------:|--------|
|      Brute Force | 6m33s  |
|  Resolution Time | 13m33s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N/2) |

### Solution: Clean string and use two pointers

First, we need to prepare the string and get rid of all non-characters and also
format it to all lower case. For this, we can use the `re` standard library:

```py
import re

class Solution(object):
  def isPalindrome(self, s):
                                              # s     = "a R a R a"
    clean = s.lower()                         # clean = "a r a r a"
    clean = re.sub(r'[^a-z0-9]+', '', clean)  # clean = "arara"
```

After that, we use a pointer to go from the edges until the middle of the string.

Here's the final solution:

**Python3**

```py
import re

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """

    clean = re.sub(r'[^a-z0-9]+', '', s.lower())
    
    N = len(clean)
    i = 0

    while i < N // 2:
      if (clean[i] != clean[N-i-1]):
        return False
      
      i += 1

    return True
```