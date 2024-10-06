# 1. Two Sum

- Link: https://leetcode.com/problems/valid-parentheses
- Level: Easy
- Added in: 24-10-05
- Topics: String, Stack

## Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```

Example 4:
```
Input: s = "([])"
Output: true
```

Constraints:

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

## Solutions

### Solution 1: Using Hash Table

|                  |        |
|-----------------:|--------|
|      Brute Force | --     |
|  Resolution Time | 17m19s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N)   |

The approach here is to use a `match` dictionary to differentiate
between open and closed brackets. Then we stack the open brackets
and whenever we find a close bracket, we pop out the last bracket
added to the stack:

```
Input: s = "([{}])"
Stack: "([{"
c: "}"
Output: true
```

In the example above, when we find a closing bracket "}", we compare it to 
its matching bracket in match["{"] = "}". If the stack is empty or the
bracket we popped out from stack if different, the we return False.

**Python3**

```py
class Solution(object):
    def isValid(self, s):

        match = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c in match:
                stack.append(c)
            elif len(stack) == 0 or c != match[stack.pop()]:
                return False

        return len(stack) == 0
```