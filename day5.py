1 lst = []
2 print(lst)
3 lst = ['a','b','c','d','e','f']
4 print(lst)
5 print(len(lst))
6 print(lst[0], lst[len(lst)//2], lst[-1])
7 mixed_data_types = ['Manohar', 21, 5.8, 'Single', 'Bangalore']
8 print(mixed_data_types)
9 it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
10 print(it_companies)
11 print(len(it_companies))
12 print(it_companies[0], it_companies[3], it_companies[-1])
13 it_companies[0] = 'Meta'
14 print(it_companies)
15 it_companies.append('Wipro')
16 print(it_companies)
17 it_companies.insert(4, 'Infosys')
18 print(it_companies)
19 it_companies[1] = it_companies[1].upper()
20 print(it_companies)
21 print('#; '.join(it_companies))
22 print('IBM' in it_companies)
23 it_companies.sort()
24 print(it_companies)
25 it_companies.reverse()
26 print(it_companies)
27 print(it_companies[:3])
28 print(it_companies[-3:])
29 print(it_companies[4])
30 it_companies.pop(0)
31 print(it_companies)
32 it_companies.pop(3)
33 print(it_companies)
34 it_companies.pop()
35 print(it_companies)
36 it_companies.clear()
37 print(it_companies)
38 del it_companies
39 front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
40 back_end = ['Node','Express', 'MongoDB']
41 full = front_end + back_end
42 print(full)
43 full_stack = full.copy()
44 full_stack.insert(5, 'Python')
45 full_stack.insert(6, 'SQL')
46 print(full_stack)
47 ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
48 ages