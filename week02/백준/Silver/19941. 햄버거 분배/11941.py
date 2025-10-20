"""
1. N개의 좌석이 일렬로 배치
2. 각 칸에는 H(햄버거) 또는 P(사람)가 위치
3. 사람(P)은 K칸 이내에 있는 햄버거(H)를 먹을 수 있음

입력 조건
1. N(좌석의 개수, 1 ≤ N ≤ 20,000)
2. K(햄버거를 먹을 수 있는 거리, 1 ≤ K ≤ 10)
3. N개의 문자열 (H: 햄버거, P: 사람)

출력 조건
최대 몇 명의 사람이 햄버거를 먹을 수 있는지 출력

"""


import sys

input =  sys.stdin.readline
N,K =map(int, input().split())
table = list(input().strip())

count =0 #햄버거 먹는거 가능

for i in range(N):
    if table[i] == 'P':
        for j in range(max(0, i-K),min(N,i+K+1)):
            if table[j] =='H':
                table[j] = 'X' #햄버거 먹어서 사라짐
                count +=1
                break

print(count)
