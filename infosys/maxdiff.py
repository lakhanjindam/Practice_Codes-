# Find Max diff in elements of a list

class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0
    def computeDifference(self):

        #simply sort the list first
        self.sorted_elem = sorted(self.__elements)
        length = len(self.sorted_elem)

        #Now the max value is last and min value is first
        #length -1 because index starts at 0
        self.maximumDifference = self.sorted_elem[length-1] - self.sorted_elem[0]
        


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)