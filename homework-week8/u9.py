# so sánh 2 cặp số cạnh nhau , so sánh 2 số lớn nhất mỗi cặp , loại đi số lớn hơn , thế số 5 vô và lặp lại sự so sánh đến khi tìm được
# số lớn thứ 3

def Median(nums) :
	a,b,c,d,e = nums[0],nums[1],nums[2],nums[3],nums[4]
	if a > b : 
		a , b = b , a
	if c > d : 
		c ,d = d , c
	if b > d : 
		a , b , c , d = c , d , a , b

	if c > e : 
		c , e = e , c 
	if b > e : 
		a , b , c , e = c ,e ,a , b

	if c > b : 
		return c
	return b


# arr = [10 , 6 ,5 ,4 ,7]
# print(Median(arr))