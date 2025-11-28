"""
1팀 6명, 점수는 상위 네명의 점수 합한 값(결승점 통과 순서대로 점수 합산,
가장 낮은 점수 우승, 6명이 참가하지 못한 경우 실격, 동점은 5번째 주자가 가장빨리 들어온 경우 우승)

"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    count ={}
    rank_list = list(map(int, input().split()))

    #팀별 주자 세기
    for i in range(n):
        if rank_list[i] in count:
            count[rank_list[i]] += 1
        else:
            count[rank_list[i]] =1

    #팀 제외 : 6명이 참가하지 못한 경우 실격
    delete ={}
    for k,v in count.items():
        if v < 6:
            delete[k] =1
    # 점수 계산
    team = {}
    idx =1  # 점수 1부터
    for i in range(n):
        if rank_list[i] not in delete:
            if rank_list[i] in team:
                if team[i][0] <4:
                    team[rank_list[i]][0] += 1
                    team[rank_list[i]][1] += idx
                elif team[rank_list[i]][0] == 4:
                    team[rank_list[i]][0] += 1
                    team[rank_list[i]][2] = idx
            else:
                team[team[i]] = [1,idx,0]   # [팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수]
            idx += 1

    #순위 정렬
    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
