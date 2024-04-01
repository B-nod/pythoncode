dictionary = {}

dictionary['name']="Ram"
dictionary['age']=18
dictionary['subject'] = ['Math', 'Science', 'Nepali']
dictionary['education'] = {
    'School':{
    'name':'Xavier School',
    'address':'Kalopul, Kathmandu'
    },
'High school':{'name':'DAV College',
               'address': 'Jawlakhel, Lalipur'},
'Bachelor level': {
    'name':'Xavier College',
    'address':'Boudha, Kathmandu'
    }
}
print(dictionary)

# for i in dictionary.keys():
#     print(i)

# for i in dictionary['subject'][0]:
#     print(i, end="")

#accessing element of nested dictionary from for loop
# for i, j in dictionary['education']['School'].items():
#     print(i, "=", j)

#dictionary = {key:{nestkey:{subnestedkey:value}}}
print(dictionary['education']['School']['name'])