# 383. Ransom Note

- Link: https://leetcode.com/problems/ransom-note/
- Level: Medium
- Added in: 24-10-10
- Topics: HashTable, String, Counting

## Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote`
can be constructed by using the letters from magazine and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

Example 1:
> Input: ransomNote = "a", magazine = "b"
> Output: false

Example 2:
> Input: ransomNote = "aa", magazine = "ab"
> Output: false

Example 3:
> Input: ransomNote = "aa", magazine = "aab"
> Output: true

Constraints:

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 40ms (beats 70.58%) |
|           Memory | 11.66mb (beats 89.36%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 5m28s |
|  Resolution Time | 5m28s |
|          O Space | O(m) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

The approach here is to use a hash table to count the characters in the magazine
and then decrement from it based on ransom note content.

```py
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        bag = {}

        for c in magazine:
            if c not in bag: bag[c] = 1
            else: bag[c] += 1

        for c in ransomNote:

            if c not in bag: return False
            elif bag[c] == 0: return False
            else: bag[c] -= 1

        return True
```