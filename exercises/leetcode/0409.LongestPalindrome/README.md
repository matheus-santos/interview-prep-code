# 409. Longest Palindrome

- Link: https://leetcode.com/problems/longest-palindrome
- Level: Easy
- Added in: 24-10-10
- Topics: HashTable, String, Greedy

## Description

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
> Input: s = "abccccdd"
> Output: 7
> Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
> Input: s = "a"
> Output: 1
> Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

- `1 <= s.length <= 2000`
- s consists of lowercase and/or uppercase English letters only.

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 15ms (beats 73.07%) |
|           Memory | 11.62mb (beats 51.66%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 5m12s |
|  Resolution Time | 5m12s |
|          O Space | O(n+c), _where n is len(s) and c is len(counter)_ |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

We use `count` as a hash table to count the character's frequency.
Then we go back and collect as much pairs as we can and a single odd character.

```py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = {}
        total = 0
        inc = 0

        for c in s:
            if c not in count: count[c] = 1
            else: count[c] += 1

        for c in count:
            if count[c] % 2 == 0: total += count[c]
            else:
                total += count[c] - 1
                inc = 1
        
        return total + inc

```
