'''i = 5
while i < 15:
  print(f'i: {i}')
  i +=2


for i in 'hello world':
  if i == 'o':
    break
  print(i)


for i in 'hello world':
  if i == 'o':
    continue
  print(i)


a = int(input())
b = int(input())
c = int(input())
x1 = 0
x2 = 0

D = (b**2) - (4*a*c)

if D > 0:
  x1 = (((-b + (D**(1/2)))/(2*a)))
  x2 = (((-b - (D**(1/2)))/(2*a)))
  print(x1, x2)
elif D == 0:
  x1 = (-b )/2*a
  print(x1)
else:
  print("Действительных корней нет")


a = int(input())
b = int(input())
c = int(input())

if a < (b+c) and b < (a+c) and c < (b+a):
  if a != b and b != c and c !=a:
    if a > b and a > c:
      if (a**2) == ((b**2) + (c**2)):
        print('Треугольник прямоугольный')
    elif a < b and b > c:
      if (b**2) == ((a**2) + (c**2)):
        print('Треугольник прямоугольный')
    elif c > b and a < c:
      if (c**2) == ((b**2) + (a**2)):
        print('Треугольник прямоугольный')
    else:
      print('Треугольник разносторонний')
  elif a == b and b == c and a == c:
    print('Треугольник равносторонний')
  else:
    print('Треугольник равнобедренный')
else:
  print('Треугольника не существует')


list = []

for i in range(0,4,1):
  i = int(input())
  list.append(i)

print(max(list))
print(min(list))

a = input()
c = ''

for i in range(1,len(a)+1,1):
  c += a[-i]
print(c)
'''
a = int(input())
d = int(input())
n = int(input())
s = 0

for i in range(1, n+1, 1):
  a *= d
  s += a
print(a,s)