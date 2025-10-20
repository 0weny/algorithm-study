""""
*************개인적으로 어려웠음*****************
1. 왼, 직진,오른 중 택1, 같은방향 연속 두번 이동 불가능
2. 최소값 구하는 문제
3. N행 M열 -> 원소값 주어짐

완전탐색 dfs로 접근해봄

위에서 아래로 이동하면서
- 각 칸에서 갈 수 있는 3가지 방향(왼, 직, 오른)을 모두 시도해 봄
- 같은 방향으로 연속 이동 불가능하므로 바로 직전에 선택한 방향(prev_dir)은 제외하고 다음 방향을 고름.
- 모든 가능한 경로의 총 연료를 계산하고 그중 최소값(min_fuel)을 찾음


"""

import sys

input =  sys.stdin.readline
N,M = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

# 방향
directions = [-1, 0, 1]
# 최소 연료
min_fuel = float('inf')


def dfs(row, col, prev_dir, total):     # 현재위치(row, col), 이전이동방향, 지금까지의 연료총합
    global min_fuel

    #마지막 행 도착시 결과 비교후 갱신
    if row == N - 1:
        min_fuel = min(min_fuel, total)
        return

    for i, d in enumerate(directions):
        next_col = col + d
        if next_col < 0 or next_col >= M:
            continue
        if i == prev_dir:       # 같은 방향 연속 이동 금지
            continue
        # 다음 행으로 이동
        dfs(row + 1, next_col, i, total + arr[row + 1][next_col])



for start_col in range(M):
    dfs(0, start_col, -1, arr[0][start_col])

print(min_fuel)
