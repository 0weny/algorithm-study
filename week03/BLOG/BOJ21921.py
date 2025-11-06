N, X = map(int, input().split())

people = list(map(int, input().split()))

value = sum(people[:X])
s = value
cnt = 1

for i in range(X, N) :
    value += people[i]
    value -= people[i-X]
    
    if value > s :
        s = value
        cnt = 1
    elif value == s :
        cnt += 1
        
if s == 0 :
    print('SAD')
else :  
    print(s)
    print(cnt)
