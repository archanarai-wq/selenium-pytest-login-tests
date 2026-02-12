print("hello")

a,b,c=1,2,"Archana"
print(a+b)

print("{} {}".format("Value of c:",c))

class basicCalculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.s-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b

obj=basicCalculator(10,5)
print("Addition:",obj.addition())



