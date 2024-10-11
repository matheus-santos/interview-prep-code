# 5. Longest Palindromic Substring

- Link: https://leetcode.com/problems/longest-palindromic-substring
- Level: Medium
- Added in: 24-11-11
- Topics: TwoPointers, String, DynamicProgramming

## Description

Given a string s, return the longest palindromic substring in s.

Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

Constraints:

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 1987ms (beats 30.26%) |
|           Memory | 19.60mb (beats 7.18%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 12m12s |
|  Resolution Time | 43m17s |
|          O Space | O(n*m) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

Solution consists of using DP to save all previous calculations:

```py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ""

        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        max_len = 1

        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if max_len < (end - start + 1):
                            max_len = end - start + 1
                            ans = s[start:end+1]

        return ans
```

## Naive approach

The naive approach (O(n^3)) consists of using a double loop to check the palindromes:

```py
class Solution(object):
    def isPalindrome(self, s):

        N = len(s)
        k = N // 2
        i = 0
        
        while i < k:
            if s[i] != s[N-i-1]: return False
            i += 1
            
        return True


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        i, j, a, b = 0, 1, 0, 1
        N = len(s)
        maxpal = 0

        while i < N:
            while j < N+1:
                piece = s[i:j]
                M = len(piece)
                
                if self.isPalindrome(piece) and M > maxpal:
                    maxpal = M
                    a, b = i, j

                j +=1

            i += 1
            j  = b

        return s[a:b]
```