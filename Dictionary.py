person ={
    "Id" : 101,
    "Name" : "RAHUL JAISWAL",
    "Age" : 22,
    "Address" : "Bihar",
    "Salary" : 25000
}
print(person)

 # print only one Value of person like Name & Id
print(person["Id"])
print(person["Name"])
# print only value of person
print(person.values())
# print only key of Person
print(person.keys())

# print all values and key of person
print(person.items())

 # if you check which type of data
print(type(person))
