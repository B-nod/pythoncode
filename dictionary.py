alphabets = ['a','b','c','d']
number = [1,2,3,4]

dictionary = dict.fromkeys(alphabets, number)
print(dictionary)
result= dictionary.get('a')
print(result)

print(dictionary.items()) # returns a view object that displays a list of dictionary's tuple pair