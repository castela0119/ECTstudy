import sys
n = int(sys.stdin.readline())

stack_list = []

for i in range(n):
    command = sys.stdin.readline().split()  # 띄어쓰기(공백) 개수에 상관없이 나눠진 문자열을 인식

    if command[0]=='push':                  # push 입력
        stack_list.append(command[1])       # push 3 을 했을 경우 3을 append 한다.

    elif command[0]=='pop':                 # pop 입력
        if len(stack_list)==0:                   # 비어있을 경우
            print(-1)                       # -1 출력
        else:                               # 비어있지 않은 경우
            print(stack_list.pop())         # stack_list 의 가장 끝에 있는 수(가장 위에 있는 수)를 빼낸다.

    elif command[0] == 'size':              # size 입력
        print(len(stack_list))              # stack_list 의 길이 출력

    elif command[0] == 'empty':             # empty 입력(비어있는지 확인)
        if len(stack_list)==0:              # 비어있으면
            print(1)                        # 1 출력 (True 의미)
        else:                               # 비어있지 않으면
            print(0)                        # 0 출력 (False 의미)

    elif command[0] == 'top':               # top 입력
        if len(stack_list)==0:              # 비어있으면
            print(-1)                       # -1 출력
        else:                               # 비어있지 않으면
            print(stack_list[-1])           # 가장 끝에 있는 수(가장 위에 있는 수)를 출력

# 사실상 python 리스트 메서드를 이용해

# 스택의 자료구조를 구현 가능

# 그렇지 않은 언어에서 구현하는게 좀 더 유의미한 풀이라고 생각됨.

print(dir(stack_list))