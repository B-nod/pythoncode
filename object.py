#OOP in python (object oriented program). We deal with real time object and its entities

# class Room: # blueprint of object.
#     l = int(input("Enter a length : "))
#     w = int(input("Enter a widht : "))
#     h = int(input("Enter a height : "))

#     def area(self):
#         print("Area of room is ", self.l*self.w)

#     def volume(self):
#         print("Volume of room is ", self.l*self.w*self.h)


# room = Room()
# print(room.area())
# print(room.volume())

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,*args):
        self.num1 = args[0]
        total = 0
        for n in args:
            total += n
        return total
    

cal = Calculator(1,2)
print(cal.num1)
print(cal.add(2,3,4))


