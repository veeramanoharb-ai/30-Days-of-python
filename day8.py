dog = {}
dog['name'] = 'Tommy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print(dog)

student = {
'first_name':'Veera',
'last_name':'Manohar',
'gender':'Male',
'age':18,
'marital_status':'Single',
'skills':['Python', 'Java'],
'country':'India',
'city':'Bangalore',
'address':'BTM'
}
print(student)
print(len(student))
print(type(student['skills']))
student['skills'].append('HTML')
print(student['skills'])

keys = list(student.keys())
print(keys)

values = list(student.values())
print(values)

items = list(student.items())
print(items)

del student['address']
print(student)

del dog