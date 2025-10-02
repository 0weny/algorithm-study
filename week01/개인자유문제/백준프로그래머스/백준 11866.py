# 원형큐 까먹어서 리스트 배열 이용
# (현재 인덱스 + K-1) % 남은 사람 수

N, K = map(int, input().split())
people = list(range(1, N+1))
answer = []
index = 0

while people:
    index = (index + K - 1) % len(people)  # K번째 사람 위치
    ans.append(people.pop(index))


print("<", end="")

for i in range(len(answer)):
    print(answer[i], end="")
    if i != len(answer) - 1:   
        print(", ", end="")

print(">")
