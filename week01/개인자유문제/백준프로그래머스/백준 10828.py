import sys

class Stack:
    def __init__(self):
        self.stack = []

    def order(self, command: str):
        if command == "pop":
            if not self.stack:
                print(-1)
            else:
                print(self.stack.pop())
        elif command == "size":
            print(len(self.stack))
        elif command == "empty":
            print(1 if not self.stack else 0)
        elif command == "top":
            if not self.stack:
                print(-1)
            else:
                print(self.stack[-1])
        else:  # push X
            value = command.split()[1]  # "push X" 에서 X만 뽑기
            self.stack.append(value)


def main():
    input = sys.stdin.readline
    N = int(input().strip())
    ss = Stack()

    for _ in range(N):
        cmd = input().strip()
        ss.order(cmd)


if __name__ == "__main__":
    main()
