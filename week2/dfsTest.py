def recursive_dfs(v, discovered):
    discovered.append(v)
    print(discovered)
    print(f'현재 정점 v 는 : {v} 입니다.')
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
        print(f'정점v : {v} 의 인접노드 w : {w} 를 모두 방문하였습니다.')
    return discovered

discovered = []

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

print(recursive_dfs(1, discovered))
print('끝')