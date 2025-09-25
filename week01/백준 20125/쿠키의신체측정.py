import sys

'''
N -> N*N 행렬

1. N행에서 *가 있는 첫 행 착기 -> 머리가 됨 (x,y)
2. 심장의 위치 =(x+1,y)
3. 심장 기준 왼쪽 팔과 오른쪽 팔의 길이
4. 허리
5. 허리기준 왼쪽과 오른쪽 다리 

----------------------
[입력]
N 
쿠키
[출력] 
심장의 위치 x y
왼쪽팔, 오른쪽팔, 허리, 왼쪽 다리, 오른쪽 다리 (순서대로 공백 구분 출력)

'''

cookie_arr=[]
l_arm, r_arm, waist,l_leg, r_leg=0,0,0,0,0

N = int(input())
cookie_arr =[input().strip() for _ in range(N)]

#심장 찾기

def find_heart():
    for i in range(N):
        for j in range(N):
            if cookie_arr[i][j] =='*':
                return (i,j), (i + 1, j)


head, heart = find_heart()

#길이 구하기

for i in range(heart[1]-1,-1,-1):
    if cookie_arr[heart[0]][i] =='*':
        l_arm +=1
    else:
        break

for j in range(heart[1]+1,N):
    if cookie_arr[heart[0]][j] == '*':
        r_arm +=1
    else:
        break

waist_x=heart[0]
for i in range(heart[0]+1,N):
    if cookie_arr[i][heart[1]]=='*':
        waist +=1
        waist_x = i
    else:
        break

for i in range(waist_x+1,N):
    if cookie_arr[i][heart[1]-1]=='*':
        l_leg +=1
    else:
        break

for i in range(waist_x + 1, N):
    if cookie_arr[i][heart[1]+1] == '*':
        r_leg += 1
    else:
        break



print(heart[0]+1,heart[1]+1)  # 0based -> 1based로 변경

print(l_arm,r_arm, waist, l_leg, r_leg)
