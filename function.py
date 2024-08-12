#function is a block of code. we used function to reuse the code. Two type of function 
# 1. Build-in function
# 2. User defined function

# def function_name():
#     function body

# function_name()

#simple program in user defined function
# def helloworld():
#     print("Hello, world!")

# helloworld()

#positinal arguments - takes value according to proper positional order.
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello('Ram', 'Python with django') #arguments

#keywords arguments - takes value according to keyword
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello(course_name='Python with django', name='Ram') #arguments

#default arguments
# def hello(name, course_name='Python with django'): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello(name='Ram', course_name='Python with Data Science') #arguments

#arbitrary arguments - *args
# def sum(*args):
#     total = 0
#     for n in args:
#         total+=n
    
#     return total  #return gives result of function and stop the excution of function

# resutlt = sum(2,3,5)
# print(resutlt)


#arbitrary keyword arguments - **kwargs which contain data in key:value pairs
# def hello(**kwargs): #parameter
#     print("Hello", kwargs['name'], "Welcome to Web development Training")
#     print(kwargs['course_name'])

# hello(name='Ram', course_name='Python with Data Science', another_course='Python with Data Science')

#scope of variable
#global variable -> which can accessible from any place.
l = float(input('Enter a length : '))
w = float(input('Enter a widht : '))

def area():
    #local variable -> that is defined inside the function and cannnot accessible from outside the function. its scope is only around the declared function.
    # h = float(input("Enter a height : "))
    global area_of_object
    area_of_object = l*w
    # volume = area_of_object * h
    return area_of_object

def volume():
    h = float(input('Enter a height : '))
    v = area_of_object* h
    return v


# result = area()
# result_volume = volume()
# print(result)

# print(result_volume)

#lambda function: the function without name. it is used for instant use and its one-time uses. lambda keyword is used.

# x = lambda a, b : a * b
# area = x(2,3)
# print(area)


# recursive function - fucntion calling itself again and again
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# result = factorial(3)
# print(result)
#filter()
#map()


