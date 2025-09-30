import sys
input = sys.stdin.readline  # 이거 추가 안하면 시간초과됨...

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()


for i in range(N):
    print(arr[i])
