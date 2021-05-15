'''import modul as m 

m.print_func(m.mult_func(4))
m.print_func("Hello")

x0 = 10

def move(t):
  x = x0 *  t
  return x

print(move(3))


a = 500
print(id(a))
a = a + 5
print(id(a))

b = [500]
print(id(b))
b[0] = 505
print(id(b))
x = 3
y = 4
z = complex(x, y)
print(z)

w = complex(y, x)
print(z + w)

t = (1, 4, 9)
print(t)
print(t[0])

d = {'a1': 4, 
     'a2': 3,
     'str': 'Hello'}
print(d['str'])
d['str'] = 'Good'
print(d)

def my_func(a=1, b=0):
  x = 3 * a - b
  return x

print(my_func(b=1,a=2))
print(my_func(3))
print(my_func())

a = [1,2,3,4,5]
b = [*a,6,7,8]
c = [a,6,7,8]
print(b)
print(c)

def my_func(*args):
  x = 3 * args[0] - args[1]
  return x

print(my_func(3,4,8))

def my_func(**kwrgs):
  x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
  return x 

print(my_func(obj_2 = 4, obj_1 = 3))

def my_func(a,b):
  x1 = 3*a - 2*b
  x2 = 5*b - 4*a
  return x1, x2

tmp = my_func(3,2)

print(type(tmp))
print(my_func(3,2)[1])
import numpy as np

def my_func(arr):
  s = 1
  for i in range(0, len(arr)):
    s *= int(arr[i])
  return s
a=[65,76,4]
arr = np.array(a)
print(my_func(arr))

import library as lb

def my_func(v, m, h):
  x = (((m*(v**2))) / 2) + m*h*lb.g
  return x 

print(my_func(30,2,10))

def my_func(a,b):
  arr = []
  for i in range(a,b+1):
    arr.append(i**2)
  return(arr)

print(my_func(3,8))'''

def my_func(**kwrgs):
  if kwrgs['figure'] == 'треугольник':
    p = (kwrgs['a']+kwrgs['b']+kwrgs['c'])/2
    s = (p*(p-kwrgs['a'])*(p-kwrgs['b'])*(p-kwrgs['c']))**(1/2)
    return s
print(my_func(figure = 'треугольник', a = 3, b = 4, c = 2))