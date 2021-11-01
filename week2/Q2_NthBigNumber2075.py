import heapq
import sys

N = int(input())

list_heapq = []

for _ in range(N):
    nums = list(map(int,sys.stdin.readline().split()))

    if not list_heapq: 
        for num in nums:
            heapq.heappush(list_heapq, num)
    else:
        for num in nums:
            if list_heapq[0] < num:
                heapq.heappush(list_heapq, num) 
                # heappush 로 각 줄의 원소를 하나 하나씩 넣으면서 n개의 노드를 가진 heapq 자료구조를 유지하면서 
                # print(list_heapq)
                
                heapq.heappop(list_heapq)
                # heappop 으로 최소힙구조로 만들어 버린다. 
                # 결국 맨위의 노드에 n 번째 로 큰수가 남게된다. 
                
                # push 로 한개의 노드를 추가해주고
                # pop 으로 root node(가장 작은값을 가진 노드)를 날려버리고 정렬
                # 이 과정을 반복하게 된다.
                # print(list_heapq)

print(list_heapq[0])