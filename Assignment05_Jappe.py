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
        self.firstnumber = float(input())
        print("What is the second number?")
        self.secondnumber = float(input())
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
    
    #Method for hypotenuse
    def calculateHypotenuse(self, base, perpendicular):
        self.base = base
        self.perpendicular = perpendicular
        def calculateSquare(number):
            square = number ** 2
            return square
        self.hypotenuse = (calculateSquare(self.base) + calculateSquare(self.perpendicular)) ** 0.5
        print("The hypotenuse is", self.hypotenuse)
    
    #Method for area
    def Area (self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        print("The area of the rectangle is", self.area)
    
    #Method for power
    def Power(self, base, power):
        self.base = base
        self.power = power
        self.result = self.base ** self.power
        print("The result is", self.result)
    
    #Method for type
    def Type(self, argument):
        self.argument = argument
        self.type = type(self.argument)
        print("The type of the argument is", self.type)

#Creating the instance
instance = BasicMathOperations()

#Introduction message
print("""List of Tasks:
      1. Greet
      2. Add two numbers
      3. Various math operations
      4. Square a number
      5. Compute the factorial of a number
      6. Count
      7. Calculate the hypotenuse of a base and perpendicular
      8. Calculate the area of a rectangle
      9. Compute the power of a number
      10. Get the type of an argument
      
      Type a number to execute a task""")

#Loop for if handle is not recognized
while (True):
    task = int(input())

    if task == 1:
        print("What is your first name?")
        firstname = input()
        print("What is your last name?")
        lastname = input()
        instance.Greet(firstname, lastname)
        break
    elif task == 2:
        instance.Add()
        break
    elif task == 3:
        print("What is the first number?")
        firstnumber = float(input())
        print("What is the second number?")
        secondnumber = float(input())
        print("What operation do you want performed (add, subtract, multiply, divide)?")
        operation = input()
        instance.Operation(firstnumber, secondnumber, operation)
        break
    elif task == 4:
        print("What number would you like squared?")
        number = float(input())
        instance.Square(number)
        break
    elif task == 5:
        print("What is the number?")
        number = int(input())
        instance.Factorial(number)
        break
    elif task == 6:
        print("What is the start number?")
        startnumber = int(input())
        print("What is the end number?")
        endnumber = int(input())
        instance.Count(startnumber, endnumber)
        break
    elif task == 7:
        print("What is the base?")
        base = float(input())
        print("What is the perpendicular?")
        perpendicular = float(input())
        instance.calculateHypotenuse(base, perpendicular)
        break
    elif task == 8:
        print("What is the width?")
        width = float(input())
        print("What is the height?")
        height = float(input())
        instance.Area(width, height)
        break
    elif task == 9:
        print("What is the base?")
        base = float(input())
        print("What is the power?")
        power = float(input())
        instance.Power(base, power)
        break
    elif task == 10:
        print("Please type the argument:")
        argument = input()
        instance.Type(argument)
        break
    
    #If task handle is not in range of 1 to 10
    else:
        print("Error! Task handle is not recognized! Try again!")