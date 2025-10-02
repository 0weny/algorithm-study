from collections import deque

# 인접 리스트
vec = [[] for _ in range(10002)]
bfs_result = []
dfs_result = []
visit = [False] * 1002


def BFS(v):
    q = deque()
    q.append(v)
    visit[v] = True

    while q:
        next_node = q.popleft()
        bfs_result.append(next_node)

        for nxt in vec[next_node]:
            if not visit[nxt]:
                q.append(nxt)
                visit[nxt] = True


def DFS(x):
    visit[x] = True
    dfs_result.append(x)

    for nxt in vec[x]:
        if not visit[nxt]:
            DFS(nxt)


def main():
    n, m, v = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        vec[a].append(b)
        vec[b].append(a)

    for i in range(1, n + 1):
        vec[i].sort()

    # BFS 실행
    BFS(v)

    # 방문 배열 초기화
    global visit
    visit = [False] * (n + 1)

    # DFS 실행
    DFS(v)

    # 출력
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))


if __name__ == "__main__":
    main()
