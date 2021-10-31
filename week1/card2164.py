# 1번 부터 N 까지의 번호가 붙어있다.

# 제일 위의 카드를 바닥에 버린다.

# 그 다음 제일 위에있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# -> deque 을 이용 pop 과 rotate 를 이용한다.

# [1, 2, 3, 4, 5, 6, 7, 8] 1을 버린다.

# [2, 3, 4, 5, 6, 7, 8] 2를 제일 밑으로 옮긴다.

# [3, 4, 5, 6, 7, 8, 2] 3을 버린다.

# [4, 5, 6, 7, 8, 2] 4를 제일 밑으로 옮긴다.

# [5, 6, 7, 8, 2, 4]

import sys
from collections import deque

n = sys.stdin.readline()

deque_list = deque([i for i in range(1, int(n)+1)])

while(len(deque_list)>1):
    deque_list.popleft()
    deque_list.rotate(-1)

print(deque_list[0])