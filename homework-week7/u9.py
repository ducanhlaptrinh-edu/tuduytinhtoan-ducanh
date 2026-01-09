class Student() : 
	def __init__(self , name) : 
		self.subject = subject 
		self.score = []

	def add_score(self , subject , score) : 
		self.score.append(score)

	def avg(self) : 
		if len(self.score) == 0 : 
			return 0 
		else : 
			return sum(self.score) / len(self.score)

	def rank(self) : 
		average = self.avg() 
		if average >= 8 : 
			return "Excellent"
		elif average >=6.5 :
			return "Good"
		elif average >= 5 : 
			return "Average" 
		else : 
			return "Poor"

if __name__ == "__main__" : 
	name = input("Enter student's name : ")
	student = Student(name)

	number = int(input("Enter the number of subjects : "))
	for _ in range(number) : 
		sub_sco = input().strip().split()
		if sub_sco : 
			score = float(sub_sco[-1])
			subject = " ".join(sub_sco[:-1])
			student.add_score(subject , score)
print(f"{student.name} {student.avg():.2f} {student.rank()}")