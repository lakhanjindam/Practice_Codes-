class Person:
    	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def printPerson(self):
        super().printPerson()
        

    def calculate(self):
        summ = 0
        avg = 0
        for i in self.scores:
            summ = summ + i

        avg = summ/len(self.scores)

        if(90<=avg<=100):
            return "O"
        elif(80<=avg<90):
            return "E"
        elif(70<=avg<80):
            return "A"
        elif(55<=avg<70):
            return "P"
        elif(40<=avg<55):
            return "D"
        elif(avg<40):
            return "T"

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())