import bisect

def find_radius(houses , healters) : 
	max_min_distance = 0 
	healters.sort()

	for house in houses : 
		i = bisect.bisect_left(healters , house) # tìm vị trí đầu tiên từ trái qua mà house lớn hơn hoặc bằng healters[i]
		left_dist = float('inf') # tạo left_dist = vô cực
		if i > 0 : 
			left_dist = house - healters[i-1]
		right_dist = float('inf')
		if i < len(healters): 
			right_dist = healters[i] - house

		current_distance = min(left_dist , right_dist)

		max_min_distance = max(max_min_distance , current_distance)

	return max_min_distance

houses = [8,10,15]
healters = [10,12,10]

print(find_radius(houses,healters))