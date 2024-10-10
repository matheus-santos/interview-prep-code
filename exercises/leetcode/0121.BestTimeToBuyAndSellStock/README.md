# 1. Two Sum

- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
- Level: Easy
- Added in: 24-10-06
- Topics: Array, DynamicProgramming

## Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

Constraints:

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

## Solutions

| Submission stats |        |
|-----------------:|--------|
|          Runtime | 780ms (beats 47.32%) |
|           Memory | 21.01mb (beats 24.45%) |

| Exercise results |        |
|-----------------:|--------|
|      Brute Force | 11m33s |
|  Resolution Time | 18m33s |
| Complexity Space | O(N)   |
|  Complexity Time | O(N)   |

### Solution: Use DP to store min and max values

Here we leverage the heapq idea, but instead of keeping the whole list in a
heap queue, we use two variables `buy` and `profit` to maximize the answer:

**Python3**

```py
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    N = len(prices)
    buy = prices[0]
    profit = 0

    for i in range(1, N):
        profit = max(profit, prices[i] - buy)
        buy = min(buy, prices[i])

    return profit
```

### Attempt 1: Brute force w/ double loop

Use a double loop to compare each entry.

### Attempt 2: Use heapq (accepted)

Using a heap to find the best day to sell and use a loop to find the best
day to buy.

**Python3**

```py
from heapq import heappop, heappush, heapify

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    i = 0
    heap = []
    heapify(heap)
    N = len(prices)

    i = 1
    while i < N:
      heappush(heap, (-1 * prices[i], i))
      i += 1

    i = 0
    maxprofit = -100000
    while (i < N - 1):

      (price, j) = heappop(heap)

      if (j > i):
          maxprofit = max(maxprofit, - prices[i] - price)
          heappush(heap, (price, j))

      i += 1

    return max(maxprofit, 0)
```