import sys
input = sys.stdin.readline

ans = [0, 0] #white, blue

def divide_and_conquer(N, paper, startX, startY):
    if N == 1:
        ans[paper[startX][startY]] += 1
        return
    
    for i in range(startX, startX+N):
        for j in range(startY, startY+N):
            if paper[i][j] != paper[startX][startY]:
                divide_and_conquer(N//2, paper, startX, startY)
                divide_and_conquer(N//2, paper, startX + N//2, startY)
                divide_and_conquer(N//2, paper, startX, startY + N//2)
                divide_and_conquer(N//2, paper, startX + N//2, startY + N//2)
                return

    ans[paper[startX][startY]] += 1
    return

N = int(input())
paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

divide_and_conquer(N, paper, 0, 0)

print(ans[0])
print(ans[1])