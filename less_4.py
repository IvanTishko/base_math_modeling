'''import numpy as np
import library as lb 
h = 100
a = (lb.pi) / 3
b = np.radians(30)
T = 200
E = 300
V = np.sqrt((lb.g * h * (np.tan(b)**2)) / (2 * ((np.cos(a))**2) * (1 - (np.tan(b) * np.tan(a)))))
print(int(V))
N = (2 / np.sqrt(lb.pi)) * (lb.h / (lb.Kb * T) ** (3/2)) * (lb.e ** (-E/(lb.Kb * T))) * (E**(T / 2))
print(N)

import numpy as np
n = int(input())
m = int(input())
arr = np.zeros((n,m))
b = 0
for i in range(0,n):
  for j in range(0, m):
    b = np.sin(n * (i+1) + m * (j + 1))
    if b <= 0:
      arr[i][j] = 0
    else:
      arr[i][j] = b
print(arr)
firstElementColumn  = int(input()) - 1
firstElementString  = int(input()) - 1
secondElementColumn = int(input()) - 1 
secondElementString = int(input()) - 1
s = arr[firstElementColumn][firstElementString]
arr[firstElementColumn][firstElementString] = arr[secondElementColumn][secondElementString]
arr[secondElementColumn][secondElementString] = s
print(arr)

print((1 + (1/10000))**10000)'''

import numpy as np
import random as rd

n = int(input())
m = int(input())
arr1 = np.zeros((n, m))
arr2 = np.zeros((n, m))
arr3 = np.zeros((n, m))

for i in range(0, n):
  for j in range(0, m):
    arr1[i][j] = rd.randint(0, 1000)
    arr2[i][j] = rd.randint(0, 1000)
print(arr1)
print(arr2)
for i in range(0, len(arr1)):
  for j in range(0, len(arr1[i])):
    arr3[i][j] = max(arr1[i][j], arr2[i][j])
print(arr3)