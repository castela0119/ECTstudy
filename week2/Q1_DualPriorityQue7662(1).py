# 1. I 는 무조건 append 한다.
# 2. D 는 무조건 del, pop 등을 한다
# 2.1 D 1 이면 max 값을 없앤다.
# 2.2 D -1 이면 min 값을 없앤다.

import sys
from collections import deque       # 덱 자료구조 이용

def input():
    return sys.stdin.readline()

t = int(input())                    # 테스트 케이스 갯수
for i in range(1, t+1):     
    num = int(input())              # 입력할 num 의 갯수를 정해준다.
    
    list_deq = []
    deque(list_deq)

    for cmd in range(1, num+1):                 # 주어진 num 숫자대로 커맨드를 입력해준다.
        cmd = input().split()
        if(cmd[0] == 'I'):                      # cmd[0] == I 인 경우
            list_deq.append(int(cmd[1]))
            # print(list_deq)

        elif(cmd[0] == 'D'):                    # cmd[0] == D 인 경우
            if(len(list_deq) > 0):
                if(cmd[1] == '1'):              # cmd[1] == 1 인 경우
                    temp = int(max(list_deq))
                    # print(temp)
                    list_deq.remove(temp)
                    # print(list_deq)
                elif(cmd[1] == '-1'):           # cmd[1] == -1 인 경우
                    temp = int(min(list_deq))
                    # print(temp)
                    list_deq.remove(temp)
                    # print(list_deq)
            elif(len(list_deq) == 0):           # 중간에 list_deq 이 비어진 경우는 건너뛴다.
                continue

    if(len(list_deq) == 0):
        print('EMPTY')
    else:
        temp1 = max(list_deq)
        temp2 = min(list_deq)
        print(f'{str(temp1)} {str(temp2)}')

