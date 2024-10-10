# 141. Linked List Cycle

- Link: https://leetcode.com/problems/linked-list-cycle
- Level: Easy
- Added in: 24-10-10
- Topics: HashTable, LinkedList, TwoPointers

## Description

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 22ms (beats 98.21%) |
|           Memory | 18.55mb (beats 86.66%) |

| Exercise results |        |
|-----------------:|:-------|
|      Brute Force | 6m20s  |
|  Resolution Time | 19m38s |
|          O Space | O(1)   |
|           O Time | O(N)   |

### Solution

Here we used Turtle and Hare solution, with one pointer going one by one
and a second pointer going twice as fast. We stop when we both pointers
fall in the same object. If something breaks along the way, then it means
the list stops somewhere.

```py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        try:

            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next

            return True

        except:
            return False
```