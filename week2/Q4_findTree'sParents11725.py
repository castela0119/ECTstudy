import sys

# 준비 과정

node = int(input())                             # 전체 노드의 개수를 입력합니다.

node_graph = [[] for _ in range(node + 1)]      # node_graph 를 2차원 빈 배열 형태로 만들어 줍니다. , # 각 노드 번호의 연결 상태를 알 수 있습니다.
print(f'node_graph : {node_graph}')

parent_of_node = [[] for _ in range(node + 1)]          # parent_of_node 를 2차원 빈 배열 형태로 만들어 줍니다.
print(f'parent_of_node : {parent_of_node}')

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())   # 트리 상에서 연결된 두 정점을 입력합니다.
    node_graph[i].append(j)                     
    node_graph[j].append(i)                         # node_graph 상에 추가해줍니다.

# DFS나 BFS나 무관(함수 정의)

def dfs(graph_list, start, parent_of_node):

    stack = [start]                                 # stack 에 들어간 정점이 곧 부모, 어떤 자식이 있는지 찾아 볼 것임.
    
    print(f'stack : {stack}')
    print()

    while stack:                                    # dfs 구현 (스택을 이용한 반복 구조)
                                                    # 1. 스택을 이용해 모든 인접 간선을 추출
                                                    # 2. 다시 도착점인 정점을 스택에 삽입하는 구조
        
        node = stack.pop()                          # stack 에서 pop 해줌으로서 pop 당한 정점의 자식을 찾아보자

        print(f'stack 에서 pop 이 실행되었습니다. 현재 stack : {stack}')
        print()

        
        for i in graph_list[node]:                  # graph_list[부모정점] 에 연결된 자식들을 i 로 하나하나 꺼내보자
            
            print(f'node: {node} 에 연결된 다른 node i : {i}')
            print()

            parent_of_node[i].append(node)          # 자식노드 i 의 부모는 node 입니다. , parent_of_node 에 표시해주자.

            print(f'parent_of_node : {parent_of_node}')
            print()

            stack.append(i)                         # 이제 그 자식 노드가 부모 노드가 되어 자식 노드를 찾기 위한 준비

            print(f'stack 에 i : {i} 를 append 하였습니다. ')
            print(f'현재 stack : {stack}')
            print()
            
            graph_list[i].remove(node)              # graph_list 라는 현황판에서 자식을 찾은 부모 노드를 지워 준다.

            print(f'graph_list[{i}] 에서 node : {node} 를 remove 합니다.')
            print()
            print(f'현재 graph_list : {graph_list}')
            print()
            
    return parent_of_node

# 시작

print(f'node_graph : {node_graph}')
print()

print(f'parent_of_node : {parent_of_node}') 
print()

for i in list(dfs(node_graph, 1, parent_of_node))[2:]:      # 2번 노드부터 n
    
    print(i[0])