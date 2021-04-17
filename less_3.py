'''
import lec_3_my_module
print(lec_3_my_module.a)

b = lec_3_my_module.b *3
print(b)
print(lec_3_my_module.c[2])

import lec_3_my_module as mm

print(mm.a)

b = mm.b *3
print(b)

print(mm.c[2] + b +mm.c[0])

from lec_3_my_module import *

print(a * b)
print(c[2] * c[1])

from lec_3_my_module import earth_mass as em
from lec_3_my_module import gravity_constant as G
from lec_3_my_module import sigma_steff_bolc as sigma

g = 500 * G / 10**2
print(g)

x = em * G * sigma
print(x)

import math

a = math.sin(3 * math.pi / 5)
print(a)

b = math.sqrt(3)
print(b)

c = math.log10(42)
print(c)

d = math.asin(math.tan(math.pi / 4)) * 180 / math.pi
print(d)

import numpy as np

a = [1, 2, 4]

b = np.array(a)

print(type(a))
print(type(b))

print(b * b)
print(b / b)
print(b - b)

print(b[-1])

import numpy as np

a = np.zeros((2, 3))
print(a)

a[0, 2] = 5
print(a)

b = np.ones((3, 2))
print(b)

d = np.ndarray((3, 3))
print(d)

import numpy as np

a = range(0, 5, 1)
print(a)

b = np.arange(0, 5, 0.1)
print(b)

d = np.linspace(0, 5, 10)
print(d)

a = [4, 16, 10, 5, 7, 1, 8]
slice = a[2:5:1]
print(slice)

import numpy as np

a = 'Томчук лох'
print(a[:3])
print(a[:])
print(a[::2])
print(a[::-1])

a = [1, 5, 3, 6]
b = np.array([a, np.array(a)*3])
print(b)

slice = b[::, 1]
print(slice)

slice = b[1,2:3:1]
print(slice)

slice = b[1, 2::1]
print(slice)'''

import numpy as np

g = 9.8
x0 = input("Введите x0: ")
y0 = input("Введите y0: ")
v0x = input("Введите v0x: ")
v0y = input("Введите v0y: ")

time = np.arange(0, 11, 1)

x = np.array(x0 +v0x*time)
y = np.array(y0 +v0y*time - ((g*(time**2))/2))

print(x)
print(y)