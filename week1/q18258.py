import sys
from collections import deque           # deque 자료구조를 이용합니다.

n = sys.stdin.readline()                # 시간을 줄이기위한 stdin.readline() 메서드 ?, 테스트 케이스 n

deque_list = deque([])                  # 리스트에 deque 자료구조 부여

for i in range(int(n)):

    k = sys.stdin.readline().split()    # 테스트 케이스 입력
    
    if(k[0] == 'push'):                 # push 하는 경우
        deque_list.append(k[1])
        # print(deque_list[-1])         # push 하는 경우 print 하라는 문제요구가 없었음 !! 

    if(k[0] == 'pop'):
        if(len(deque_list)>0):
            print(deque_list[0])
            deque_list.popleft()
        else:
            print('-1')
            

    if(k[0] == 'size'):
        print(len(deque_list))

    if(k[0] == 'empty'):
        if(len(deque_list) == 0):
            print('1')
        else:
            print('0')
    
    if(k[0] == 'front'):
        if(len(deque_list) > 0):
            print(deque_list[0])
        else:
            print('-1')
        
    if(k[0] == 'back'):
        if(len(deque_list) > 0):
            print(deque_list[-1])
        else:
            print('-1')
    