it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['TCS', 'Infosys', 'Wipro'])
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

# remove gives error if item not exist, discard does not

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A
del B

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print(len(ages), len(ages_set))
# ages list is bigger because list allows duplicates, set removes duplicates

print("String is text, List is ordered mutable, Tuple is ordered immutable, Set is unordered no duplicates")

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(len(unique_words))
print(unique_words)