#Main class for operations
class BasicMathOperations:
    
    #Method for greeting
    def Greet(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        print("Nice to meet you", self.firstname, self.lastname)
    
    #Method for adding
    def Add(self):
        print("What is the first number?")
        self.firstnumber = input()
        print("What is the second number?")
        self.secondnumber = input()
        self.sum = self.firstnumber + self.secondnumber
        print("The sum is", self.sum)
    
    #Method for operations
    def Operation(self, firstnumber, secondnumber, operation):
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber
        if operation == "add":
            self.result = self.firstnumber + self.secondnumber
        elif operation == "subtract":
            self.result = self.firstnumber - self.secondnumber
        elif operation == "multiply":
            self.result = self.firstnumber * self.secondnumber
        elif operation == "divide":
            self.result = self.firstnumber / self.secondnumber
        else:
            print("Error! Operation not recognized!")
            return False
        print("The result is", self.result)
        return self.result
    
    #Method for squaring
    def Square(self, number):
        self.number = number
        self.square = self.number ** 2
        print("The square of the number is", self.square)
        
    #Method for factorial
    def Factorial(self, number):
        self.number = number
        self.factorial = self.number
        for x in range(1, self.number):
            self.factorial = self.factorial * x
        print("The factorial of the number is", self.factorial)
        
    #Method for counting
    def Count(self, startnumber, endnumber):
        self.startnumber = startnumber
        self.endnumber = endnumber
        for x in range(self.startnumber, self.endnumber + 1):
            print (x)
    
    