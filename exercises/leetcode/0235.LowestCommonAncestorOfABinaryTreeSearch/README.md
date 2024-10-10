# 235. Lowest Common Ancestor of a Binary Search Tree

- Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
- Level: Medium
- Added in: 24-10-06
- Topics: Tree, DepthFirstSearch, BinarySearchTree, BinaryTree

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes in the BST.

According to the definition of LCA on Wikipedia [[1]](https://en.wikipedia.org/wiki/Lowest_common_ancestor?useskin=vector):

> “The lowest common ancestor is defined between two nodes p and q as the 
> lowest node in T that has both p and q as descendants (where we allow a node 
> to be a descendant of itself).”

Example 1:
![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
> Output: 6
> Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
> Output: 2
> Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
> Input: root = [2,1], p = 2, q = 1
> Output: 2

Constraints:

- The number of nodes in the tree is in the range `[2, 105]`.
- `-109 <= Node.val <= 109`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the BST.

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 47ms (beats 66.68%) |
|           Memory | 19.73mb (beats 38.34%) |

| Complexity       |        |
|-----------------:|--------|
|             Time | O(M*N) |
|            Space | O(M*N) |

| Submissions      |        |
|-----------------:|--------|
|      Brute Force |  9m46s |
|   1st Submission | 11m27s |
| Final Submission | 14m37s |

### Solution

The key idea here is how to understand how to traverse the tree. We know this is
a binary tree we also know what we are looking for:

> “The lowest common ancestor is defined between two nodes p and q as the 
> lowest node in T that has both p and q as descendants (where we allow a node 
> to be a descendant of itself).”

Now we need to create a rule to traverse the tree. Take the example 2:

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
> Output: 2
> Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

By looking at the drawing, we know the LCA will be 2. So, our steps would look
like this:

```
Starting from 6
Should I go right or left?
Are both `p = 2` and `q = 4` lower than 6?
  Yes. Then walk to the left side `root.left` of the tree
    Now we are at `root.val = 2`
      Are both `p = 2` and `q = 4` lower than 2?
        No. Are both `p = 2` and `q = 4` higher than 2?
          No. Then `root.val = 2` must be the LCA.
```

Let's see other example. Using the same tree, what is the LCA of `p = 7` and `q = 9`?

```
Starting from 6
Should I go right or left?
Are both `p = 7` and `q = 9` lower than 6?
  No.
  Are both `p = 7` and `q = 9` higher than 6?
    Yes. Then walk to the right side `root.right` of the tree
      Now we are at `root.val = 8`
        Are both `p = 7` and `q = 9` lower than 8?
          No.
          Are both `p = 7` and `q = 9` higher than 8?
            No.
            Then `root.val = 8` must be the LCA.
```

**Python3**

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """ 

    if not root:
      return None

    if root.val > p.val and root.val > q.val:
      return self.lowestCommonAncestor(root.left, p, q)

    if root.val < p.val and root.val < q.val:
      return self.lowestCommonAncestor(root.right, p, q)

    return root
```