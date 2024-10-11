# 112. Path Sum

- Link: https://leetcode.com/problems/path-sum
- Level: Easy
- Added in: 24-10-11
- Topics: Tree, DepthFirstSearch, BreadthFirstSearch, BinaryTree

## Description

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

![](./pathsum1.jpg)

> Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
> Output: true
> Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

![](./pathsum2.jpg)

> Input: root = [1,2,3], targetSum = 5
> Output: false
> Explanation: There two root-to-leaf paths in the tree:
> (1 --> 2): The sum is 3.
> (1 --> 3): The sum is 4.
> There is no root-to-leaf path with sum = 5.

Example 3:

> Input: root = [], targetSum = 0
> Output: false
> Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 28ms (beats 24.14%) |
|           Memory | 13.57mb (beats 69.53%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 10m00s |
|  Resolution Time | 26m58s |
|          O Space | O(n) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

The approach we are going to use consists of decrementing root.val 
from targetSum each time we visit a new node:

```py
targetSum -= root.val
return self.hasPathSum(root.right, targetSum) ...
```

Our stop condition is when we reach a leaft and the root we are visiting
is equal to the remaining value in targetSum:

```py
if (not root.right and not root.left) and (root.val == targetSum):
    return True
```

Our carry-over will be a boolean value that indicates if the leaf we are
visiting matches with the remaining value in `targetSum`.

Result:

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root: return False

        if not root.right and not root.left and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)
```

