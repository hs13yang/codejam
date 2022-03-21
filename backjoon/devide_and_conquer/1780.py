from os import sep
from re import S
import sys
input = sys.stdin.readline

#input
# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1

N = int(input())
ans = [0,0,0]
paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))


def divide_and_conquer(N, startX, startY):
    if N == 1:
        ans[paper[startX][startY]] += 1
        return
    for i in range(startX, startX + N):
        for j in range(startY, startY+ N):
            if paper[startX][startY] != paper[i][j]:
                s = N//3
                divide_and_conquer(s, startX, startY)
                divide_and_conquer(s, startX, startY + s)
                divide_and_conquer(s, startX, startY + s*2)
                divide_and_conquer(s, startX + s, startY)
                divide_and_conquer(s, startX + s, startY + s)
                divide_and_conquer(s, startX + s, startY + s*2)
                divide_and_conquer(s, startX + s*2, startY)
                divide_and_conquer(s, startX + s*2, startY + s)
                divide_and_conquer(s, startX + s*2, startY + s*2)
                return

    ans[paper[startX][startY]] += 1
    return


divide_and_conquer(N, 0, 0)
print(ans[2], ans[0], ans[1], sep='\n')