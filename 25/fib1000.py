numDigs = 1
prev2Fibs = [[1],[1]]
curFibNum = 2

def nextFib():
    global curFibNum
    global numDigs
    prevFib = prev2Fibs[curFibNum % 2]
    curFibNum += 1
    curFib = prev2Fibs[curFibNum % 2]
    carry = 0
    for i in range(numDigs):
        digSum = curFib[i] + prevFib[i] + carry
        curFib[i] = digSum % 10
        carry = digSum // 10
    if carry > 0:
        numDigs += 1
        curFib.append(carry)
        prevFib.append(0)

while numDigs < 1000:
    nextFib()

fibStr = prev2Fibs[curFibNum % 2]
fibStr = [str(fibStr[i]) for i in range(numDigs - 1, -1, -1)]
fibStr = "".join(fibStr)
print("Result: " + fibStr)
print("Index: " + str(curFibNum))
