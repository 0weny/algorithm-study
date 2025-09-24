'''
원형 큐? =>  나무 N개 배열 -> 원형큐로 안해도 될듯 -> list로 접근

1. x>= M -> result += x & x== 0

2.벌목 후 이동
L: 왼쪽 이동 : x-1
R: 오른쪽 이동 : x+1
S: x번째 그대로 : x

3. 나무가 자람 -> 모든 배열에 +1

1,2,3 과정 Q번 반복

-------------예제파악 + 입력 -----------
[입력]
N M x(위치한 나무 순서)
초기 높이 나열
Q
D(1~Q) i번째 벌목의 2번 순서에서 움직일 방법 -> 각 벌목당 움직일 방향 결정

'''

N, M, x = map(int, input().split())
trees = list(map(int, input().split()))
Q = int(input())
D = list(input().split())
result = 0
x -= 1  # 파이썬 0  부터 시작


def felling(trees, M, x, result):
    if (trees[x] >= M):
        result += trees[x]
        trees[x] = 0
    return trees, result


def move():
    if D == 'L':
        x = (x - 1) % N  # *******
    elif D == 'R':
        x = (x + 1) % N  # *******
    return x


for i in range(Q):
    trees, result = felling(trees, M, x, result)
    move()
    for j in range(N):
        trees[j] += 1

print(result)








