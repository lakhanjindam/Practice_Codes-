class Base:
    def __init__(self):
        self.value = 200
    def get_value(self):
        return self.value+1
    
class Child(Base):
    def two(self):
        self.num = 200


#grandchild can inherit functions of above two classes 
class Grandchild(Child):
    def __init__(self):
        #this enables access of self.__value which was not accessible
        # bcoz instance variable value is defined in constructor of base class
        super().__init__()
        self.num = 200
        
    
c = Child()
g = Grandchild()
print(g.get_value())
