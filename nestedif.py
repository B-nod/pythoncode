pin = int(input("Enter your pin : "))
pin1 = 1234

if pin == pin1:
    print("You have successfull login. Click 1 for fast cash. Click 2 for Withdraw. Click 3 for exit")
    number = int(input("Click number: "))
    if number == 1:
        print("Fast Cash")
    elif number == 2:
        print("Withdraw")
    elif number == 3:
        print("You are exit from system")
    else:
        print("Please enter valid number")
else:
    print("Your pin is incorrect")
