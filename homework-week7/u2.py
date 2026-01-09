class Date() : 
	def __init__(self , day , month , year) : 
		self.day = day
		self.month = month 
		self.year = year 
	def is_leap_month(self) : 
		return self.year % 400 == 0 
	def get_max_days(self) : 
		if self.month in [1,3,5,7,8,10,12] : 
			return 31 
		elif self.month == 2 : 
			return 29 if self.is_leap_month() else 28
		elif self.month in [4,6,9,11] :
			return 30
		else :
			return 0
	def is_valid(self) : 
		if self.day > self.get_max_days() : 
			return False
		if self.month < 1 or self.month > 12 :
			return False
		if self.year < 1 : 
			return False
		return True
	def get_next_date(self) : 
		if self.day > self.get_max_days() : 
			self.day = 1 
			self.month += 1
			if self.month > 12 : 
				self.month = 1 
				self.year += 1
		return f"{self.day:02d}/{self.month:02d}/{self.year:02d}"

if __name__ == "__main__" : 
	user = list(map(int(input().split())))
	parts = user.split("/")
	day = parts[0]
	month = parts[1]
	year = parts[2]

	my_date = Date(day , month , year) 
	if my_date.is_valid() :
		day = parts[0]
		month = parts[1]
		year = parts[2]
		print(my_date.get_next_date())
	else : 
		print("Invalid")

