from collections import deque
import sys
read = sys.stdin.readline

def dfs(v):                 # v 는 시작 지점
  visit_list2[v] = 1        # 방문했다는 표시로 visit_list2[1] 에 1 을 할당한다.
  print(f'현재 dfs(v)는 v : {v}')        
  print(v, end = " ")
  print()

  print(f'visit_list2 : {visit_list2}')

  for i in range(1, n + 1): # 1부터 n까지의 노드 번호
    if visit_list2[i] == 0 and graph[v][i] == 1: # 방문하지 않은 노드번호 이면서 그 노드 번호와 다른 노드 번호가 간선으로 연결되어 있으면
      print(f'visit_list2[i] - i : {i} 를 처리중 입니다.')
      dfs(i)                                     # 재귀적으로 dfs 호출

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
print(f'graph : {graph}')

visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

print(f'visit_list2 : {visit_list2}')

for _ in range(m):
  a, b = map(int, read().split())   # 주어진 m 의 수만큼 반복해서 node 번호 입력
  graph[a][b] = graph[b][a] = 1     # graph 정보가 쌓인다.

  print(f'graph : {graph}')

dfs(v)