class ShoppingCart() : 
	def __init__(self) : 
		self.items = []

	def add_product(self) : 
		dic = {}
		dic["name"] = input("Enter name's product : ")
		dic["price"] = int(input("Enter price's product : "))
		self.items.append(dic)	
		return self.items

	def remove_product(self) : 
		user_input = input("Enter the product you want to delete : ")
		for x in self.items: 
			if user_input == x["name"] : 
				self.items.remove(x)
		return self.items

	def check_empty_cart(self) : 
		if self.items == [] : 
			print("Shopping Cart is empty.")
		else : 
			print("Shopping Cart is not empty.")

	def calculate_total_price(self) : 
		total = 0 
		for x in self.items : 
			total += x["price"]
		return total

	def show_cart(self) : 
		print("Your cart : ")
		for x in self.items : 
			print(x["name"] + " : " + str(x["price"]) + " USD")

	def exit(self) : 
		print("Are you sure you want to get out of here ? ")
		user = input("Yes or No : ")
		if user.lower() == "yes" : 
			return True
		return False

	def menu_display(self) : 
		print("Main menu : ") 
		print("1. Add new product.")
		print("2. Delete product.")
		print("3. Check empty cart.")
		print("4. Calculate total price.")
		print("5. Show Cart")
		print("6. Save and exit")

	def main(self) : 
		running = True 
		while running : 
			self.menu_display() 
			user = int(input("Enter an option :"))
			if user == 1 : 
				self.add_product()
				input("\nPress Enter to continue")
			if user == 2 : 
				self.remove_product()
				input("\nPress Enter to continue")
			if user == 3 : 
				self.check_empty_cart()
				input("\nPress Enter to continue")
			if user == 4 : 
				print("Total price : "  + str(self.calculate_total_price()))
				input("\nPress Enter to continue")
			if user == 5 : 
				self.show_cart()
				input("\nPress Enter to continue")
			if user == 6 : 
				if self.exit() == True : 
					print("You have left the program successfully!!!")
					running = False
				else : 
					running = True



if __name__ == "__main__" : 
	ShoppingCart().main()