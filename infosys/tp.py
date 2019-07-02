from abc import ABCMeta, abstractmethod
#abc stands for abstract base class

#declaring an abstract class

class ClassA(metaclass=ABCMeta):

    #to create a abstract method
    @abstractmethod
    def first_method(self):
        pass


#ClassB inherits from the ClassA i.e abstract class so ClassB should override Fisrt_method of ClassA
class ClassB(ClassA):

    def first_method(self):
        print("Inside the ClassB")

    def second_method(self):
        pass

#below statement will give error bcoz abstract class cannot be instantiated
#a = ClassA()

b = ClassB()


#NOTE : u cannot instantiate a abstract class with abstract methods in it.
# if there is no abstract methods in abstract class then u can instantiate
# instantiation means creating object of class
#abstract class can have 0 or more abstract methods

#Usually the parent class is an abstract class.
#Abstract classes should not be instantiated.
#If a class has an abstract method, then the class cannot be instantiated.
#Abstract classes are meant to be inherited.
#The child class must implement/override all the abstract methods of the parent class. 
# Else the child class cannot be instantiated.
