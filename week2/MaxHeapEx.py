import heapq

nums = [4, 1, 7, 3, 8, 5]
list_heap = []

for num in nums:
  heapq.heappush(list_heap, (-num, num))  # (우선 순위, 값)
  print(list_heap)

while list_heap:
  print(heapq.heappop(list_heap)[1])  # index 1