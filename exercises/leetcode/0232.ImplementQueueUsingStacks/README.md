# 232. Implement Queues using Stacks

- Link: https://leetcode.com/problems/implement-queue-using-stacks
- Level: Easy
- Added in: 24-10-10
- Topics: Stack, Design, Queue

## Description

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 10ms (beats 83.70%) |
|           Memory | 11.82mb (beats 22.19%) |

| Exercise results |        |
|-----------------:|:-------|
|      Brute Force | 5m24s |
|  Resolution Time | 5m24s |
|          O Space | - |
|           O Time | - |
|             BTTC | - |

### Solution

Straightforward implementation of a queue using array as stack.

```py
class MyQueue(object):

    items = []

    def __init__(self):
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop(0)


    def peek(self):
        """
        :rtype: int
        """
        return self.items[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.items) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```