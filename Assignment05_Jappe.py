class BasicMathOperations:
    
    def Greet(self, firstname, lastname):
        self.firstnae = firstname
        self.lastname = lastname
        print("Nice to meet you", self.firstname, self.lastname)
    
    def Add(self, firstnumber, secondnumber):
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber
        self.sum = self.firstnumber + self.secondnumber
        print("The sum is", self.sum)