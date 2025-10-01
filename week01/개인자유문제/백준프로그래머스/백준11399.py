# 정렬 최솟값
# 돈인출 시간이 적은 순으로 배열해야 총합이 적어짐
from functools import total_ordering

N = int(input())
arr = list(map(int, input().split()))

""" 인덱스 초과
for i in range(N):
    if(arr[i]> arr[i+1]):
        arr[i] = arr[i+1]"""

arr.sort()

result=0
total_ordering=0

for j in arr:
    total_ordering += j
    result += total_ordering

print(result)





