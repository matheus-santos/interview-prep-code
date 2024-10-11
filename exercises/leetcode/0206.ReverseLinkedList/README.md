# 206. Reverse Linked List

- Link: https://leetcode.com/problems/reverse-linked-list
- Level: Easy
- Added in: 24-10-11
- Topics: LinkedList, Recursion

## Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

Example 1:

![](./rev1ex1.jpg)

> Input: head = [1,2,3,4,5]
> Output: [5,4,3,2,1]

Example 2:

![](./rev1ex2.jpg)

> Input: head = [1,2]
> Output: [2,1]

Example 3:

> Input: head = []
> Output: []

Constraints:

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up**: A linked list can be reversed either iteratively or recursively.
Could you implement both?

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 15ms (beats 78.55%) |
|           Memory | 13.37mb (beats 98.40%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 9m40s |
|  Resolution Time | 9m40s |
|          O Space | O(n) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

The approach consists of using a buffer list `items` to store items from
the linked list and then reverse it by running from end to start of the list.

```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
        
        item = head
        items = [item]

        while True:
            items.append(item)
            if not item.next: break
            else: item = item.next

        N = len(items)
        i = N-1

        while i > 0:
            items[i].next = items[i-1]
            i -= 1

        items[0].next = None

        return items[N-1]
```