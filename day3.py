age = 18
height = 5.8
x = 1 + 2j
base = float(input("enter base"))
height_sec = float(input("enter height"))
area = 0.5 * base * height_sec
print(area)
side_a = int(input("enter side a"))
side_b = int(input("enter side b"))
side_c = int(input("enter side c"))
perimeter = side_a + side_b + side_c
print(perimeter)
length = float(input("enter length"))
width = float(input("enter width"))
area = length * width
print(area)
perimeter = 2 * (length + width)
radius = float(input("enter radius"))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(area)
print(circumference)
print("slope m = 2")
x = 0
y = 2*x - 2
print("y-intercept is",y, "point is (0,-2)")
y = 0
x = (y + 2)/ 2
print("x-intercept is",x, "point is (1,0)")
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = (y2 - y1) / (x2 - x1)
print("slope m is:", m)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("distance is:", distance)
slope_task8 = 2
slope_task9 = 2
print(slope_task8 == slope_task9)
x = -3
y = x**2 + 6*x + 9
print(y)
x = 0
y = x**2 + 6*x + 9
print("when x=0, y=", y)
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))
print('on' in 'python' and 'on' in 'dragon')
sentence = "i hope this course is not full of jargon"
print('jargon' in sentence)
print('on' not in 'dragon' and 'on' not in 'python')
text = 'python'
length = len(text)
print(length)
float_length = float(length)
print(float_length)
str_length = str(float_length)
print(str_length)
num = 4
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print(7 // 3)
print(int(2.7))
print(7 // 3 == int(2.7))
print(type('10'))
print(type(10))
print(type('10') == type(10))
print(int(9.8))
print(float('9.8'))
print(int(9.8) == 10)
print(int(float('9.8')) == 10)
hours = int(input("enter hours:"))
rate = int(input("enter rate per hour"))
pay = hours * rate
print(f"your weekly earning is{pay}")
years = int(input("enter number of years you have lived:"))
seconds = years * 365 * 24 * 60 * 60
print(f"you have lived for{seconds} seconds.")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")