# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

'''x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.plot(y, x)

plt.show()'''

'''s = 0
x = [1, 2, 3]
for s in x:
  print(s)'''
  
'''numbers = [0,1,2,3,4,5]
for n in numbers:
    print(n)'''
#Goal: randomly shuffles the indecies of an array
'''
tenArray = np.arange(1, 11)   
tenArrayRand = tenArray
s=0

while s <len(tenArray):
  randIndex1 = int(np.random.rand()*len(tenArray))
  randIndex2 = int(np.random.rand()*len(tenArray))
  originalValIndex1 = tenArrayRand[randIndex1]
  tenArrayRand[randIndex1] = tenArrayRand[randIndex2]
  tenArrayRand[randIndex2] = originalValIndex1
  s = s+1
  
print(tenArrayRand)
'''

#The above while loop works but it is inefficient. What if we want to ensure every index is flipped at least once?
'''
tenArray = np.arange(1, 11)   
tenArrayRand = tenArray
loopCycles = 0
checker = np.array([])
while len(checker) < len(tenArray):
  randIndex1 = int(np.random.rand()*len(tenArray))
  loopCycles += 1
  if not randIndex1 in checker:
    randIndex2 = int(np.random.rand()*len(tenArray))
    originalValIndex1 = tenArrayRand[randIndex1]
    tenArrayRand[randIndex1] = tenArrayRand[randIndex2]
    tenArrayRand[randIndex2] = originalValIndex1
    checker = np.append(checker, randIndex1)
  
print(tenArrayRand)
print(loopCycles)
'''
#The above loop works however it can sometimes require dozens of cycles. Make it take exactly 10 cycles
'''
tenArray = np.arange(1, 11)   
tenArrayRand = np.random.choice(tenArray, len(tenArray), False)

print(tenArrayRand)
'''
#That feels like cheating. Maybe return to this optimization problem.







