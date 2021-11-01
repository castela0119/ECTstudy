import sys
import heapq

input = sys.stdin.readline

def heapsort(iterable):
    list_heap = []
    result = []

    # 3. [3, 5, 6, 2, 1] 를 차례대로 힙에 삽입 => 이진 트리 구조에 맞게끔 숫자를 배치해준다.
    for value in iterable:
        heapq.heappush(list_heap, value)
        print(list_heap)
    
    # 4. 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 => 최소값 먼저 꺼내는 동작을 해주고 그 순서의 수를 reuslt 에 할당
    for i in range(len(list_heap)):
        print(len(list_heap))
        result.append(heapq.heappop(list_heap))
        print(result)
    return result

# 1. 시작
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

# 2. heapsort 동작 arr = [3, 5, 6, 2, 1]
res = heapsort(arr)
print(res)

#for i in range(n):
#    print(res[i])