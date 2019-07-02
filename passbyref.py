class Mobile:
    #you need to pass a first parameter to a function inside class 
    # as it refers to the object created outside the class
    #NOTE: fisrt parameters doesn't need to be self.

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    #pass by reference using object variable
    def change_price(mobile_obj):
        print ("Id of object inside function", id(mobile_obj))
        mobile_obj.price = 3000

mob1=Mobile(1000, "Apple")
print ("Id of object in driver code", id(mob1))

#id of both variables are same
mob1.change_price()
#baove statement can also be written as below
Mobile.change_price(mob1)
print ("Price of mob1 ", mob1.price)

#reassigning object variable values results into a new object and previous data is unaffected.
class Customer:
    def __init__(self, cust_id, age):
        self.cust_id = cust_id
        self.age = age

c1=Customer(100,20)

def change(c2):
    c2=Customer(100,21)

change(c1)
print(c1.age)

#local and instance variable concept.
class Mobile:


    def __init__(self):
        print ("Inside the Mobile constructor")
        self.brand = None
        brand = "Apple" #This is a local variable.
        #Variables without self are local and they dont
        #affect the attributes.

        #Local varaibles cannot be accessed outside the init
        #Using self creates attributes which are
        #accessible in other methods as well

mob1=Mobile()
print(mob1.brand)#This does not print Apple
#This prints None because brand=Apple creates
#a local variable and it does not affect the attribute

#4

#Here self is not the first parameter. 
# Therefore the value 100 is assigned to self, which is the second parameter. 
# Here id is a reference to the current object. 
# Hence it creates an object with 2 attributes: self and age, where self is 100 and age is 20
class Customer:
    def __init__(id,self,age):
        id.self=self
        id.age=age

c1=Customer(100,20)
print(c1.self)

#5
#Iterating objects through dictionary
class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 5000)
mob3=Mobile("Apple", 3000)

mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3
          }

for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)

    

#6

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        #super() is  used to call parent function over child class
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()

#7
#using parent class constructor in child class with the help of super()
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")

    def buy(self):
        super().buy()
        print ("Buying a smartphone")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)

#8

#Public instance variable of parent class can be directly accessed in child class using self.variable_name, 
# as it belongs to the child object.
class Parent:
    def __init__(self):
        self.num=100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var=200
    def show(self):
        print(self.num)
        print(self.var)

son=Child()
son.show()