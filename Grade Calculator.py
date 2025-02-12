
x = [6, 5, 0]

tuple = (1, 4, 9)

dict = {
    'x' : 21,
    'y' : 22,
    'z' : 23
}

type(dict)

type(x)

dir(x)

dictionary = {
    'name' : 'me',
    'age' : 20,
    'country' : 'IR'
}

for key, value  in dictionary.items():
    print(key, value)

set = {1, 2, 3, 4, 5, 6}

type(set)

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == 'admin' and password == '12345':
  print('welcome admin!')
else:
  print('access denied')

grades = {}
total = 0
num = int(input('enter num?'))

for i in range(num):
  name = input('name:')
  grade = int(input('whats the grade:'))
  grades[name] = grades
  total += grade
average = total / num
print(f'miangin: {average}')
print(grades)

grades = {}
high = 0
top_student = {}

for i in range(5):
  name = input('name:')
  grade = int(input('grade:'))
  grades[name] = grade

  if grade > max_grade:
    max_grade = high
    top_stuent = name

print(f'highest:{top_student} , val:{max-grade}')