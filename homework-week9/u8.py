def check_valid() : 
	file = input("Enter name's file : ") 
	lower_file = file.lower 
	if "." in lower_file : 
		slicing = lower_file.split(".")
		extension_file = slicing[-1]
		if extension_file == "txt" or extension_file == "zip" : 
			print("Read file successfully!")
			return
	print("Invalid file")
------------------------------------------------------------
def check_valid() : 
	file = input("Enter name's file : ") 
	lower_file = file.lower 
	extension_file = lower_file[-4:] # 4 phần tử cuối
	if extension_file == ".txt" or extension_file == ".zip" : 
		print("Read file successfully!")
	else : 
		print("Invalid file")
------------------------------------------------------------
def check_valid() : 
	file = input("Enter name's file : ") 
	lower_file = file.lower	
	if lower_file.endswith(('.txt') , ('.zip')) : 
		print("Read file successfully!")
	else : 
		print("Invalid file")
