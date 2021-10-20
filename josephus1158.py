from collections import deque               # deque 자료구조를 이용합니다.

n, k = map(int, input().split())            # n, k 를 입력합니다.

deq = deque([i for i in range(1, n+1)])     # 1 ~ n 까지의 수를 deque 에 담고 deq 에 할당합니다.

temp_list = ['<']                           # 답안에서 요구하는 '<' 문자를 미리 list 에 담아둡니다.
temp_str = ''                               # 마지막에 list 를 join 을 하여 빈 문자열에 합쳐주기 위함.

for i in range(n):                          # 입력된 n 만큼 없애는 행위를 반복합니다.

    deq.rotate(-k+1)                        # 순서상 3번째 사람을 삭제해야하는 경우 2칸만 움직이주면 됩니다.

    temp = str(deq.popleft())               # 해당 순서를 삭제해주고 join 을 위해 숫자를 문자열 형테로 temp 에 담아둡니다.
    temp_list.append(temp)                  # 삭제한 순서인 temp 를 빈 list 에 append 해줍니다.

    if(i < n-1):                            # 마지막 순서가 아닌 경우는 답안에서 요구하기 때문에
        temp_list.append(', ')              # list 에 ', ' 를 같이 추가해줍니다.

temp_list.append('>')                       # 반복문이 끝나고 답안에서 요구하는 '>' 문자를 list 마지막에 담아둡니다.

temp_str = "".join(temp_list)               # list에 모인 문자를 join 메서드로 합쳐줍니다.

print(temp_str)