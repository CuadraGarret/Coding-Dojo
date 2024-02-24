x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1] = [15,8,9] #changes the value of x from [ [5,2,3], [10,8,9] ]  -> [ [5,2,3], [15,8,9] ] 
print(x)
students[0]["last_name"] = 'Bryant' #changes the 1st students last name to Bryant
print(students[0])
sports_directory['soccer'][0] = 'Andres' #changes Messi to Andres
print(sports_directory['soccer'])
z[0]['y'] = 30 # changes the value of y to 30
print(z)

def iterateDictionary(some_list): #function that prints each key and associated value
    for i in range(len(some_list)):
        list = some_list[i]
        for key, val in list.items():
            print(key, "-", val) 

iterateDictionary(students) #calls function

def iterateDictionary2(key_name, some_list): #function that prints each value for the give key
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students) #calls function
iterateDictionary2('last_name', students) #calls function

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict): #function that prints the length of each key and the values of each key
    for key, val in some_dict.items():
        print(len(val), key)
        for item in val:
            print(item)

printInfo(dojo) #calls function