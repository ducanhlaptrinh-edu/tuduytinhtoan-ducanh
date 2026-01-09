import math
class Calculate() : 
	def __init__(self ,x ,y) : 
		self.x = x 
		self.y = y
	def add(self) : 
		result = self.x + self.y 
		return result
	def substract(self) : 
		result = self.x - self.y
		return result

	def product(self) : 
		result = self.x * self.y
		return result

	def divide(self) :
		result = self.x / self.y
		return result

	def power(self) : 
		result = self.x**self.y
		return result

	def mod(self) : 
		result =  self.x % self.y
		return result

	def set_number(self) : 
		number_input = input("Enter the two numbers to be calculated (x,y) : ")
		number_input = number_input.split(",")
		self.x = int(number_input[0])
		self.y = int(number_input[1])
		
	def exit(self) : 
		print("Are you sure you want to get out of here ? ")
		user = input("Yes or No : ")
		if user.lower() == "yes" : 
			return True
		return False

	def menu_display(self) : 
		print("Main menu : ")
		print("1.add")
		print("2.substract")
		print("3.product")
		print("4.divide")
		print("5.power")
		print("6.mod")
		print("7.set number")
		print("8.exit")

	def main(self) : 
		running = True
		while running : 
			self.menu_display()
			user = int(input("Enter an option : "))

			if user == 1 : 
				print(self.add())
				input("\nPress Enter to continue")
			if user == 2 : 
				print(self.substract())
				input("\nPress Enter to continue")

			if user == 3 : 
				print(self.product())
				input("\nPress Enter to continue")

			if user == 4 : 
				print(self.divide())
				input("\nPress Enter to continue")

			if user == 5 : 
				print(self.power())
				input("\nPress Enter to continue")

			if user == 6 : 
				print(self.mod())
				input("\nPress Enter to continue")

			if user == 7 : 
				self.set_number()
				input("\nPress Enter to continue")

			if user == 8 : 
				if self.exit() : 
					print("You have left the program successfully")
					running = False
				else : 
					running = True
					input("\nPress Enter to continue")


if __name__ == "__main__" : 
	number_input = input("Enter the two numbers to be calculated (x,y) : ")
	number_input = number_input.split(",")
	x = int(number_input[0])
	y = int(number_input[1])

	numbers = Calculate(x, y)

	numbers.main()

