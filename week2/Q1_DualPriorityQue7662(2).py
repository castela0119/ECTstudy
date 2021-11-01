'''
★★★★★

heap_push 는 이진 트리 구조를 유지시켜 주면서 push 해줍니다.
heap_pop 은 이진 트리 구조를 유지시켜 주면서 pop 해줍니다.

왜? min_heap, max_heap 을 이용해줘야 할까? ->

왜? visit 변수를 써서 해당 index(key) 의 True, False 를 확인해 줄까?

★★★★★
'''

''' 

I 의 경우 visit을 True 로 순차적으로 채워나가고,

D -1 의 경우 min_heap 의 작은 값부터 순차적으로 삭제합니다.
D -1 의 경우 양수로 I된 먼저 나온 visit[key] 의 True를 False 로 바꾸고
D -1 의 경우 음수로 I된 나중에 나온 visit[key] 의 True를 False 로 바꾸고 (우선적용)
    
    
D 1 의 경우 max_heap 의 (절대값 상) 큰 값부터 순차적으로 삭제합니다.
D 1 의 경우 양수로 I된 나중에 나온 visit[key] 의 True를 False 로 바꾸고 (우선적용)
D 1 의 경우 음수로 I된 먼저 나온 visit[key] 의 True를 False 로 바꾸고 로 바꿉니다.
    
'''
import sys
import heapq

test = int(input())
for _ in range(test):
	max_heap, min_heap = [], []
	visit = [False] * 1_000_001 
    


	order_num = int(input())
    
	for key in range(order_num):
		order = sys.stdin.readline().rsplit()
		if order[0] == 'I': # order 가 I인 경우 min_heap 과 max_heap 에 heappush 를 수행합니다. key 값은 0 부터 순차적으로 증가합니다.
			heapq.heappush(min_heap, (int(order[1]), key))
			heapq.heappush(max_heap, (int(order[1]) * -1, key))
			visit[key] = True; print(min_heap); print(max_heap); print("key : " + str(key)); print(f'{visit[0]} {visit[1]} {visit[2]} {visit[3]} {visit[4]} {visit[5]} {visit[6]} {visit[7]} {visit[8]} {visit[9]} {visit[10]}')

		elif order[0] == 'D':
			if order[1] == '-1': # 최소힙에서 가장 작은 값을 날립니다.
				while min_heap and not visit[min_heap[0][1]]: # min_heap이 비어있지 않고 min_heap의 key 값에 해당하는 visit이 False 인 경우 heappop 을 수행하여 이진 트리구조를 유지
					print(min_heap); print('D -1 while 문 작동'); heapq.heappop(min_heap); print(min_heap); print("key : " + str(key)); print(f'{visit[0]} {visit[1]} {visit[2]} {visit[3]} {visit[4]} {visit[5]} {visit[6]} {visit[7]} {visit[8]} {visit[9]} {visit[10]}')
				if min_heap:
					visit[min_heap[0][1]] = False; print('D -1 if 문 작동'); print(min_heap); print(f'{visit[0]} {visit[1]} {visit[2]} {visit[3]} {visit[4]} {visit[5]} {visit[6]} {visit[7]} {visit[8]} {visit[9]} {visit[10]}')
			elif order[1] == '1': # 최대힙에서 절댓값 상 가장 큰 값을 날립니다.
				while max_heap and not visit[max_heap[0][1]]: # max_heap이 비어있지 않고 max_heap의 key 값에 해당하는 visit이 False 인 경우 heappop 을 수행하여 이진 트리구조를 유지
					print(min_heap); print(max_heap); print('D 1 while 문 작동'); heapq.heappop(max_heap); print(min_heap); print(max_heap); print("key : " + str(key)); print(f'{visit[0]} {visit[1]} {visit[2]} {visit[3]} {visit[4]} {visit[5]} {visit[6]} {visit[7]} {visit[8]} {visit[9]} {visit[10]}')
				if max_heap:
					visit[max_heap[0][1]] = False
			
    
	while min_heap and not visit[min_heap[0][1]]: # min_heap이 비어있지 않고 min_heap의 0번째 index의 key 값에 해당하는 visit이 False 인 경우
		print('min_heap 출력중'); print(visit[min_heap[0][1]]); heapq.heappop(min_heap)
	while max_heap and not visit[max_heap[0][1]]: # max_heap이 비어있지 않고 min_heap의 0번째 index의 key 값에 해당하는 visit이 False 인 경우
		print('max_heap 출력중'); print(visit[max_heap[0][1]]); heapq.heappop(max_heap)

	if min_heap and max_heap:  
		print(max_heap[0][0] * -1, min_heap[0][0]); print('if문 출력중');print(max_heap[0]); print(min_heap[0])
	else:
		print('EMPTY'); print('else문 출력중')
    