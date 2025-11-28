import sys
input = sys.stdin.readline

N = int(input())                               # 지방의 수
requests = list(map(int, input().split()))     # 각 지방의 요청 예산액
total_budget = int(input())                    # 국가 예산 총액

ans = 0

# 이진 탐색 범위
low = 0
high = max(requests)

while low <= high:
    mid = (low + high) // 2  # 중간값
    total = 0

    # 상한액(중간값) 기준으로 예산 배정 총합 구하기
    for req in requests:
        total += min(req, mid)

    # 총 배정액이 국가 예산보다 크면 → 상한액 줄임
    if total > total_budget:
        high = mid - 1
    else:
        # 예산 이내  → 가능한 상한액, 더 큰 값 시도
        ans = mid
        low = mid + 1

print(ans)

