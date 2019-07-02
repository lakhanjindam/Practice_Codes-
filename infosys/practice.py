class Mobile:
    def __init__(self, brand, price):
        print("Inside the Mobile constructor")
        self.brand = brand
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * discount / 100
        print("Total price of", self.brand, "mobile is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.brand, "mobile is", self.total_price)

class Shoe:
    def __init__(self, material, price):
        print("Inside the Shoe constructor")
        self.material = material
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.material == "leather":
            tax = 5
        else:
            tax = 2

        self.total_price = self.price + self.price * tax / 100
        print("Total price of", self.material, "shoe is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.material, "shoe is", self.total_price)

mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)

shoe1=Shoe("leather",3000)
shoe2=Shoe("canvas",200)

mob1.purchase()
mob2.purchase()

shoe1.purchase()
shoe2.purchase()

mob2.return_product()
shoe1.return_product()


#2

class ClassA(): 
    def __init__(self, var1, var2): 
        self.var1 = var1
        self.var2 = var2

    def get_no(self):
        return self.var1, self.var2

    def methodA(self): 
        self.var1 = self.var1 + self.var2 
        return self.var1 
  
class ClassB(ClassA): 
    def __init__(self, class_a): 
        self.var1 = class_a.var1 
        self.var2 = class_a.var2 
  
object1 = ClassA() 
# updates the value of var1 
summ = object1.methodA() 
  
# return the value of var1 
print (summ) 
  
# passes object of classA 
object2 = ClassB(object1) 
  
# return the values carried by var1,var2 
print (object2.var1) 
print (object2.var2) 
print(object1.get_no())