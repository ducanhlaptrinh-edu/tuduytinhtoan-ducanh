intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]

# import heapq

# def min_intervals_length(intervals,queries) : 
# 	intervals.sort()

# 	queries_sorted = []
# 	for i , q in enumerate(queries) : 
# 		queries_sorted.append((q , i))
# 	queries_sorted.sort()

# 	result = [-1] * len(queries)


# 	for q_val , q_ind in queries_sorted : 
# 		min_heap = []
# 		i = 0
# 		while i<len(intervals) and intervals[i][0] <= q_val : 
# 			l , r = intervals[i]
# 			length = r - l + 1
# 			heapq.heappush(min_heap , (length , r))
# 			i+=1 
# 		while min_heap and min_heap[0][1] < q_val : 
# 			heapq.heappop(min_heap)

# 		if min_heap : 
# 			result[q_ind] = min_heap[0][0]
# 	return result


# print(min_intervals_length(intervals,queries))


import bisect

def min_interval_binary_search(intervals , queries) : 
	intervals = sorted(intervals , key=lambda x : x[1] - x[0] + 1)
	
	list_que = []
	for i , q in enumerate(queries):
		list_que.append((q,i))

	list_que.sort()

	q_val = []
	for x in list_que : 
		q_val.append(x[0])

	result = [-1] * len(queries)

	running = [False] * len(queries)

	for l , r in intervals : 
		length = r - l + 1 

		start_idx = bisect.bisect_left(q_val,l)
		end_idx = bisect.bisect_right(q_val , r)

		for k in range(start_idx,end_idx) : 
			if not running[k] : 
				original_idx = list_que[k][1]
				result[original_idx] = length
				running[k] = True
	return result



