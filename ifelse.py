x= int(input())



# if x % 2 == 0:
#     print(x, "is even number")
# else:
#     print(x, "is odd number")

if x % 3 == 0 and x % 5 == 0:
    print("Fizzbuzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0 :
    print("Fizz")
else:
    print(x)

