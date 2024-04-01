# range() to get range of number 
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 ==0:
#         print("FIzzbuzz")
#     elif i  % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

    


#nested loop is loop inside loop
# for i in range(1,11):
#     print("Multiplication table : ", i )
#     for j in range(1, 11):
#         print(i, "*", j, "=", i*j, end=" ")

# a = ['red', 'blue', 'orange', 'black']
# b = ['football', 'volleyball', 'basketball', 'baseball']

# for i in a:
#     for j in b:
#         print(i,j, end=" ")

#mutliplication table using nested while loop
# x = 0
# while x <= 10:
#     j = 0
#     while j <=10:
#         print(x, "*", j, "=", x*j)
#         j +=1
#     x +=1
    
#while loop inside for loop
for i in range(1, 11):
    print("Multiplication table : ", i)
    j = 1
    while j <=10:
        print(i,'*', j, i*j)
        j+=1
   