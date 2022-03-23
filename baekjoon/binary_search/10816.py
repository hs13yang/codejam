
import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
incard = list(map(int, input().split()))

card.sort()

# binary search - timeout
# def count_card(left,right,X):
#     cnt = 0
#     for i in range(left, right+1):
#         if i < N and card[i] == X:
#             cnt += 1

#     ans.append(str(cnt))

# def binary_search(left, right, X):
#     if left > right:
#         ans.append('0')
#         return

#     mid = (left + right) // 2
#     if card[mid] == X:
#         #count_card(left,right,X)
#         ans.append(str(card[left:right+1].count(X)))
#     elif card[mid] > X:
#         binary_search(left, mid-1, X)
#     elif card[mid] < X:
#         binary_search(mid+1, right, X)

# for i in range(M):
#     binary_search(0, N-1, incard[i])

# print(' '.join(ans))

# solution 1 - bisect 
from bisect import bisect_left,bisect_right

for i in range(M):
    print(bisect_right(card, incard[i]) -  bisect_left(card, incard[i]), end=' ')

# solution 2 - counter
from collections import Counter

counter = Counter(card)

for i in incard:
    if i in counter:
        print(counter[i], end=' ')
    else:
        print(0, end=' ')


# solution 3 - dictionary        
counter = {}
for i in card:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for i in incard:
    if i in counter:
        print(counter[i], end=' ')
    else:
        print(0, end=' ')