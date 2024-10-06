# 1. Two Sum

- Link: https://leetcode.com/problems/merge-two-sorted-lists/
- Level: Easy
- Added in: 24-10-05
- Topics: LinkedList, Recursion

## Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Solutions

### Solution 1: Using Hash Table

|                  |        |
|-----------------:|--------|
|      Brute Force | --     |
|  Resolution Time | 12m32s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N)   |

**Python3**

```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        nodes = []

        if not list1 and not list2:
            return None

        while True:

            if not list1 and list2:
                node = ListNode(list2.val, None)
                nodes.append(node)
                list2 = list2.next

            elif not list2 and list1:
                node = ListNode(list1.val, None)
                nodes.append(node)
                list1 = list1.next

            elif list1.val <= list2.val:
                node = ListNode(list1.val, None)
                nodes.append(node)
                list1 = list1.next

            elif list1.val > list2.val:
                node = ListNode(list2.val, None)
                nodes.append(node)
                list2 = list2.next

            if not list1 and not list2:
                break

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return ListNode(None) if len(nodes) == 0 else nodes[0]
```