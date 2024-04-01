import os, shutil
#file handling -> open file, close file, read file, write and maintain file
path = r'C:\Users\DELL\Desktop\maha\python\test.txt'
# my_file = open(path)
# print(my_file)
# print(my_file.read()) #to read the file.
# print(my_file.writable()) # to check whether to write in file or not
# my_file.close()

# my_another_file = open(path, 'r+')
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write('Ram \n')


# my_another_file = open(path, 'w+')
# print(my_another_file.read())
# print(my_another_file.readable())
# print(my_another_file.writable())

# my_another_file.write('Ram')
# print(my_another_file.seek(1))
# print(my_another_file.read())
# # print(my_another_file.readlines())

my_next_file = open('next.txt', 'a+')
print(my_next_file.writable())
print(my_next_file.readable())
print(my_next_file.write('Hello \n World'))

print(my_next_file.seek(0))
print(my_next_file.read())
list1 = ['\nRam\n','\nShyam\n', '\nhari\n']
print(my_next_file.writelines(list1))
print(my_next_file.seek(0))
print(my_next_file.readline())
print(my_next_file.readlines())

# shutil.copy('next.txt', 'next1.txt')
# os.remove('next1.txt')


shutil.move('test.txt', 'next1.txt')
