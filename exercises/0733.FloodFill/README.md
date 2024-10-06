# 733. Flood Fill

- Link: https://leetcode.com/problems/flood-fill
- Level: Easy
- Added in: 24-10-06
- Topics: Array, DepthFirstSearch, BreadthFirstSearch, Matrix

## Description

You are given an image represented by an `m x n` grid of integers image, 
where `image[i][j]` represents the pixel value of the image.
You are also given three integers `sr`, `sc`, and `color`. 

Your task is to perform a **flood fill** on the image starting from the pixel image[sr][sc].

To perform a flood fill:

1. Begin with the starting pixel and change its color to color.
2. Perform the same process for each pixel that is directly adjacent (pixels 
    that share a side with the original pixel, either horizontally or vertically)
    and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated
    pixels and modifying their color if it matches the original color of the
    starting pixel.
4. The process stops when there are no more adjacent pixels of the original
    color to update.

Return the **modified** image after performing the flood fill.

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 39ms (beats 98.15%) |
|           Memory | 11.66mb (beats 77.80%) |

| Exercise results |        |
|-----------------:|--------|
|      Brute Force | 11m20s |
|  Resolution Time | 16m53s |
| Complexity Space | O(M*N) |
|  Complexity Time | O(M*N) |

### Solution

The solution consists of doing a BFS (Breadth-First Search) and update all 
original colors found with the new color. In this case we are going to use
a `queue` to append the pixels we need to visit and a `seen` hash table to
mark the visited pixels.

The `seen` hash table is important to avoid infinite loops, for example: 
when original color and new color are the same.

**Python3**

```py
class Solution(object):
  def floodFill(self, image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    
    queue = []
    queue.append((sr, sc))
    px = image[sr][sc] # original color
    seen = {}

    while len(queue) > 0:

      (sr, sc) = queue.pop(0)

      if (sr, sc) not in seen and image[sr][sc] == px:

        image[sr][sc] = color
            
        if self.allowed(image, sr,   sc+1, px): queue.append((sr, sc+1)) # right
        if self.allowed(image, sr,   sc-1, px): queue.append((sr, sc-1)) # left
        if self.allowed(image, sr-1, sc,   px): queue.append((sr-1, sc)) # up
        if self.allowed(image, sr+1, sc,   px): queue.append((sr+1, sc)) # down

        seen[(sr, sc)] = True

    return image

  def allowed(self, image, sr, sc, px):
      return 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == px
```