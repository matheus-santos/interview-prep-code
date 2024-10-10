Couting bodies of water

0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

DFS on (0,0), then mark all 0 as 2 (Visited Water)
Every time you find a 1 (Land) add to queue `land`

2 2 2 2 2
2 1 1 1 2
2 1 0 1 2
2 1 1 1 2
2 2 2 2 2

lands = [1, 1, 1, 1, 1, 1, 1, 1, 1]

Now, do a DFS for every land, marking it as 2 (Visited Land)
For every body of water 0 (Water) you find, add to queue `water`

2 2 2 2 2
2 2 2 2 2
2 2 0 2 2
2 2 2 2 2
2 2 2 2 2

For every body of water in `water`, do a DFS
If you find a land 1, add to queue `land`
when DFS finishes, count +1

Do until both water and land are empty