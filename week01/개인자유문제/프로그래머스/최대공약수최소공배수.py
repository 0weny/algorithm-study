
#최대공약수
def gcd(n, m):
    while m > 0:
        n,m = m,n%m
    return n
    
#최소공배수
def lcm(n, m):
    return n * m // gcd(n,m)

def solution(n, m):
    answer = [gcd(n, m),lcm(n,m)]
    return answer
