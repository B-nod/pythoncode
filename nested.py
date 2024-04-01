user = input()
if user == "admin":
    print("Your are successfully login in your admin panel.")
    attendence = input("Take your staff attendence : ")
    if attendence == "Full":
        print("Staff work for full day.")
    elif attendence == "Half":
        print("Staff work for half day.")
    elif attendence == "Morning":
        print("Staff work for morning only.")
    else:
        print("Staff is absent")
else:
    print("You are not admin")