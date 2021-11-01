# boj, 3584: 가장 가까운 공통 조상,python3
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())

    p_list=[0 for _ in range(N+1)]                  # 각 노드의 부모노드 저장
    
    print(f'p_list 는 : {p_list}')
    print()
    
    for _ in range(N-1):                            # graph 정보 입력
        p,c=map(int,sys.stdin.readline().split())
        p_list[c]=p                                 # 부모 노드 저장
        print(f'p_list 는 : {p_list}')
        print()
    
 
    a,b=map(int,sys.stdin.readline().split())       # 입력된 a, b 의 공통 조상을 찾아볼 것임
    
    a_parent=[a]                                    # 입력된 a, b 값을 스스로의 부모로 리스트에 먼저 추가해놓는다.
    b_parent=[b]

                                        # 각노드의 부모노드가 루트일때까지 모두 저장
    while p_list[a]:
        a_parent.append(p_list[a])
        print(f'a_parent 는 : {a_parent}')
        print()
        a=p_list[a]
 
    while p_list[b]:
        b_parent.append(p_list[b])
        print(f'b_parent 는 : {b_parent}')
        print()
        b=p_list[b]
 
    a_level = len(a_parent)-1                       #같은 레벨로 맞추고 부모노드 같은거 찾기
    b_level = len(b_parent)-1
                                                    
    while a_parent[a_level] == b_parent[b_level]:   # 루트노드부터 비교하여, 같다면 한 칸씩 내려오면서 비교, 다른 경우 탈출
                                                    # a_parent[a_level], b_parent[b_level] 은 각 노드의 루트 노드를 뜻한다.
        a_level-=1
        b_level-=1
 
    print(a_parent[a_level+1])                      # 탈출 직전에서 조상이 같았으므로 그 조상을 출력해주도록 한다.