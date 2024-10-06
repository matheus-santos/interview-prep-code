# 226. Invert Binary Tree

- Link: https://leetcode.com/problems/invert-binary-tree
- Level: Easy
- Added in: 24-10-06
- Topics: Tree, DepthFirstSearch, BreadthFirstSearch, BinaryTree

## Description

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

Example 2:

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

Example 3:

```
Input: root = []
Output: []
```

Constraints:

- The number of nodes in the tree is in the range [0, 100].
- `-100 <= Node.val <= 100`

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 11ms (beats 80.43%) |
|           Memory | 11.62mb (beats 47.87%) |

| Exercise results |        |
|-----------------:|--------|
|      Brute Force | 10m00s |
|  Resolution Time | 12m00s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N)   |

### Solution

**Python3**

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    
    return root
```