n = int(input())                                    # 테스트 케이스 n

for _ in range(n):                                  # 테스트 케이스 n번 반복
    ps = list(input())                              # 괄호 문자열을 입력합니다. ex. (())()
    
    stack = []                                      # 빈 list를 만들어 줍니다.

    cnt = 0                                         # ps 길이만큼 반복문을 다 돌았는지 확인하게 위한 cnt 입니다.

    for i in range(len(ps)):                        # ps 길이만큼 반복해줍니다.
        
        if ps[i] == '(':                            # 문자가 '(' 이면
            stack.append(ps[i])                     # list 에 append 해줍니다.

        else:                                       # 그 외의 경우
            if(len(stack) > 0 and ps[i] == ')'):    # stack 이 비어있지 않고 문자가 '(' 이면
                stack.pop()                         # stack 을 pop 해줍니다.

            else:                                   # stack 이 비어있다면
                print('NO')                         # NO 를 출력하고
                break                               # 반복문을 종료합니다.

        cnt += 1                                    # 반복문을 다 돌았는지 확인하기위한 cnt 입니다.

    if (len(stack) == 0 and cnt == len(ps)):        # 반복문을 다 돌았고 stack 이 비어있다면
        print('YES')                                # YES 를 출력합니다.

    elif(len(stack) > 0 and cnt == len(ps)):        # 반복문을 다 돌았고 stack 에 '(' 남아있다면
        print('NO')                                 # NO 를 출력합니다.