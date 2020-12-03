# Matt Morrow
# Class: COP4533
# Prof: Henry Cutler
# Student ID: 2412353
# Collaboration statement: I, Matthew Morrow, have completed this assignment on my own.
# This program adds values into a list and then runs a sequential search and then a binary search
# in order to determine whether or not an stated value is present within the list.

print("Run sequential search: ")

class SequentialStringList:
    def __init__(self, name):
        self.name = name
        self.stringList = []

    # method to add the element to a list
    def add(self, name):
        self.stringList.append(name)
        #print ("list is: ", self.stringList)

    def find(self, name):
        for i in self.stringList:

            if i == name:
                print("Entry", name, "was found in the sequential search list!")
                return i

        print("Entry", name, "was NOT found in the sequential search list!")
        return None


run1 = SequentialStringList("Matt")

run1.add('Matt')
run1.find('John')
run1.find('Matt')

print("\nRun Binary Search: ")


class BinaryStringList:
    #print("\nRun binary search: \n")
    def __init__(self, name):
        self.name = name
        self.stringList = []

    # method to add the element to a list
    def add(self, name):
        self.stringList.append(name)

    def find(self, name):

        first = 0
        last = len(self.stringList)-1
        found = False
        while first <= last and not found:
            midpoint = (first + last)//2

            if self.stringList[midpoint] == name:
                print("Entry" ,name, "was found in the binary search!")
                count = 1
                found = True
            else:

                if name < self.stringList[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                    found = False
        if found == False:
            print("Entry", name, "was NOT found in the binary search!")




run2 = BinaryStringList('Matt')
#Asssign variables to the list
run2.add('Matt')
run2.add('Roberto')
run2.add('Matt')
run2.add('Matthew')
run2.add('Jennifer')
run2.add('Lauren')
run2.add('Karen')
run2.add('Clarke')
run2.add('Paul')
run2.add('Greg')
run2.add('Sam')
run2.add('Kevin')
run2.add('Mark')
run2.add('Danny')
run2.add('Britton')
run2.add('Sally')
run2.add('Susan')
run2.add('Meredith')
run2.add('Mary')
run2.add('Lou')
run2.add('Roger')
run2.add('Ron')
run2.stringList.sort()
#Search a variable that is in the list
run2.find('Matt')
#Search for a variable that is NOT in the list
run2.find('Burtha')
