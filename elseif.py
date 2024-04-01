Science = int(input("Enter the marks of Science: "))
Math = int(input("Enter the marks of Science: "))
Nepali = int(input("Enter the marks of Science: "))
English = int(input("Enter the marks of Science: "))
Social = int(input("Enter the marks of Science: "))

total = Science+Math+Nepali+English+Social
print(total)
percentage = total/500*100
print('Your percentage is : ', percentage, '%')
if percentage > 90:
    print("Grade A")
elif percentage >80 and percentage <=90:
    print("Grade is B")
elif percentage >=60 and percentage <=80:
    print("Grade s C")
else:
    print("Grade is D") 

