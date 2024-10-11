# 57. Insert Interval

- Link: https://leetcode.com/problems/insert-interval
- Level: Medium
- Added in: 24-11-10
- Topics: Array

## Description

You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith 
interval and intervals is sorted in ascending order by starti. You are also 
given an interval newInterval = [start, end] that represents the start and 
end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

**Note:** that you don't need to modify intervals in-place. You can make a new 
array and return it.

Example 1:
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## Solutions

| Submission stats |        |
|-----------------:|:-------|
|          Runtime | 65ms (beats 29.24%) |
|           Memory | 15.81 (beats 5.12%) |

| Exercise results |        |
|-----------------:|:-------|
|   Naive Approach | 28m00s |
|  Resolution Time | 32m47s |
|          O Space | O(n) |
|           O Time | O(n) |
|             BTTC | O(n) |

### Solution

First, we run through each interval and place it into a heap structure.
Alongside the value, we place flags `-1` and `1` to indicate whether the 
value belongs to the start or end of any given interval.

We use the sweep line algorithm concept to accumulate the value i each
iteration until we find a closure (when open_brackets is 0).

The second loop will take an item from the heap, then sum up the open and closed
brackets. When `open_brackets=0`, we close the interval and start a new one. 
This procedure will "absorb" the new interval into the current list.

```py
from heapq import heappush, heappop

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        heap, ans = [], []
        
        # Step one:
        # Add start and end intervals into a min heap.
        # Tag -1 to starting interval and 1 to ending 
        # interval.
        for s, e in intervals + [newInterval]:
            heappush(heap, (s, -1))
            heappush(heap, (e, 1))
        
        # We use the sweep line algorithm concept
        # to accumulate the value i each iteration until
        # we find a closure (when open_brackets is 0).
        #
        # Example:
        #   intervals = [[1,3], [6,9]], newInterval = [2,5]
        #   heap = (1, -1), (2, -1), (3, 1), (5, 1), (6, -1), (9, 1), (6, 9)
        #       (fourth iteration)
        #       i, bracket = 1, -1
        #       s = 1                   # Because s is initialize with None
        #       open_brackets = -1
        #       
        #       (second iteration)
        #       i, bracket = 2, -1
        #       open_brackets = -2
        #
        #       (third iteration)
        #       i, bracket = 3, 1
        #       open_brackets = -1
        #
        #       (fourth iteration)
        #       i, bracket = 5, 1
        #       open_brackets = 0        !!Closed brackets!!
        #          if not open_brackets:
        #               ans.append([
        #                   s => 1       # From first iteration
        #                   i => 5       # Current value popped from heap
        #               ])
        #
        # When the brackets are closed, we take `s` (row 76) as starting 
        # interval and current popped value `i` as ending interval (row 83). 
        # Then we reset the variable `s` so it can be assigned again in the
        # next iteration.
        
        open_brackets, s = 0, None

        while heap:
            i, bracket = heappop(heap)
            
            if s is None: 
                s = i
            
            open_brackets += bracket
            
            # Closing brackets, merging interval
            if not open_brackets:
                ans.append([s, i])
                s = None

        return ans
```
