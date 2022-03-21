import sys
input = sys.stdin.readline

#input
# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011

N = int(input())
ans = []
video = []
for _ in range(N):
    video.append(list(input().strip()))

def divide_and_conquer(N, startX, startY):
    if N == 1:
        ans.append(video[startX][startY])
        return

    for i in range(startX, startX+N):
        for j in range(startY, startY+N):
            if video[i][j] != video[startX][startY]:
                ans.append('(')
                divide_and_conquer(N//2, startX, startY)
                divide_and_conquer(N//2, startX, startY+N//2)
                divide_and_conquer(N//2, startX+N//2, startY)
                divide_and_conquer(N//2, startX+N//2, startY+N//2)
                ans.append(')')
                return

    ans.append(video[startX][startY])
    
divide_and_conquer(N, 0, 0)
print(''.join(ans))