import math

N = 1000000
digs = range(10)

curPerm = 1
def permToN(i):
  global curPerm
  if i < 9:
    permToN(i + 1)
    j = findMinGreater(i, i + 1)
    while j != i and curPerm < N:
      swap(i, j)
      sortI(i + 1)
      curPerm += 1
      permToN(i + 1)
      j = findMinGreater(i, i + 1)

def findMinGreater(pivotI, i):
  minGI = pivotI
  minG = 11
  while i < 10:
    if digs[i] > digs[pivotI] and digs[i] < minG:
      minGI = i
      minG = digs[i]
    i += 1
  return minGI

def sortI(i):
  start = i
  while i < 9:
      i += 1
      curCompI = start
      while curCompI < i and digs[i] > digs[curCompI]:
        curCompI += 1
      if i != curCompI:
        while curCompI < i:
          swap(i, curCompI)
          curCompI += 1

def swap(i, j):
  temp = digs[i]
  digs[i] = digs[j]
  digs[j] = temp

permToN(0)
print(digs)
