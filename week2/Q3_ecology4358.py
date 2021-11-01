import sys
from collections import defaultdict

input = sys.stdin.readline

tree = defaultdict(int)

print(tree)

cnt = 0
while True:
    name = input().rstrip()                 # 나무 이름을 입력받습니다.
    if name == "":                          # 더 이상 입력받지 않는다면
        break                               # 반복문을 종료합니다.

    tree[name] += 1                         # 해당 나무 이름을 key 값으로 하고 그 이름이 나올때마다 value 값을 1 더해줍니다.
    print(tree)

    cnt += 1                                # 모든 나무의 수를 cnt 에 담습니다.


print(f'tree 입니다. : {tree}')
tname = list(tree.keys())                   # keys() 메서드로 key 만 따로 빼서 tname(list) 에 담아줍니다.

print(f'tname 입니다. : {tname}')

tname.sort()                                # sort() 메서드로 A, B, C... 순서대로 정렬해줍니다.

print(f'정렬된 tname 입니다. : {tname}')

print(f'tree 입니다. : {tree}')

for n in tname:                             # 나무 이름을 n 에 할당하고
    print("%s %.4f" % (n, tree[n]*100/cnt)) # 그 나무 이름에 해당하는 수를 전체 나무갯수로 나누고 100 곱한 소숫점 4자리 까지의 백분율로 나타내줍니다. 