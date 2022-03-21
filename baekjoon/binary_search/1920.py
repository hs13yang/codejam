import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

M = int(input())

X = list(map(int, input().split()))

A. sort()

def binary_search(left,right, xi):
    if left > right:
        return 0

    mid = (left + right) // 2

    if A[mid] == xi:
        return 1
    elif A[mid] > xi:
        return binary_search(left, mid-1, xi)
    else:
        return binary_search(mid+1, right, xi)

for i in range(M):
    left = 0
    right = N -1
    print(binary_search(left,right,X[i]))



# Case 1 - timeout
#for i in range(M):
#    if X[i] in A:
#        print(1)
#    else:
#        print(0)
