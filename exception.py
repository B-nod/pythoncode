#exception -> an event that occurs to disrupt the normal flow of operation
# try:
#     age = int(input())
#     print(age)
# except:
#     print('Please provide numberic value')

# print('Xavier College')

# try:
#     a = int(input("Enter a value"))
#     b = int(input("Enter a value "))
#     c = a/b
# except ValueError:
#     print('Please provide numeric value')
# except ZeroDivisionError:
#     print('Zero will not divide any other number')
# else:
#     print("The value of c is ", c)
def login():
    user1 = 'admin'
    pass1 = 'admin'
    try:
        username = input("Enter a username = ")
        password = input("Enter a password = ")

        if user1 != username:
            raise ZeroDivisionError
        elif pass1 != password:
            raise ValueError
        
    except ZeroDivisionError:
        print("Username is invalid")
        login()
    except ValueError:
        print("Password is invalid")
        login()
    else:
        print("Login successfull")
    finally:
        print("Home")

login()
