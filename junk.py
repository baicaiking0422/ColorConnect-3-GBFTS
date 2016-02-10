import heapq

pq = []

item1 = [2, 1]  # 2
item2 = [5, 2]
item3 = [2, 3]
item4 = [1, 4]  # 1
item5 = [5, 5]
item6 = [4, 6]
item7 = [1, 7]  # 3
item8 = [4, 8]

heapq.heappush(pq, item1)
heapq.heappush(pq, item2)
heapq.heappush(pq, item3)
heapq.heappush(pq, item4)
heapq.heappush(pq, item5)
heapq.heappush(pq, item6)
heapq.heappush(pq, item7)
heapq.heappush(pq, item8)

for i in xrange(len(pq)):
    item = heapq.heappop(pq)
    print item[0], ":", item[1]
