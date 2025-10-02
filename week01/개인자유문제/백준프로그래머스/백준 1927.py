import heapq
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    pq = []  

    for _ in range(N):
        num = int(input())
        if num == 0:
            if pq:
                print(heapq.heappop(pq))  
            else:
                print(0)
        else:
            heapq.heappush(pq, num)  

if __name__ == "__main__":
    main()
