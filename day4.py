# Day 4 - Strings - 34 Exercises - Manohar Veera

# 1
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' + last_name
print(full_name)

# 2
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 3
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 4
company = "Coding For All"
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[7:])

# 10
print(company.find('Coding'))

# 11
print(company.replace('Coding', 'Python'))

# 12
print("Python for Everyone".replace('Everyone', 'All'))

# 13
print(company.split())

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
print(company[0] + company[7] + company[11])

# 19
words = company.split()
print(words[0][0] + words[1][0] + words[2][0])

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
print("Coding For All People".rfind('l'))

# 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24
print(sentence.rindex('because'))

# 25
print(sentence[31:54])

# 26
print(company.startswith('Coding'))

# 27
print(company.endswith('coding'))

# 28
print(' Coding For All '.strip())

# 29
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 30
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 31
print('I am enjoying this challenge.\nI just wonder what is next.')

# 32
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 33
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))

# 34
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')