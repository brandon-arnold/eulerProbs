from math import ceil, sqrt

N = 1000

def getCycLen(x):
    numerator = 1
    recurDigs = {}
    while numerator > 0 and numerator not in recurDigs:
        if numerator < x:
            recurDigs[numerator] = numerator * 10
        else:
            recurDigs[numerator] = (numerator % x) * 10
        numerator = recurDigs[numerator]
    if numerator == 0: return 0
    else:
        cycLen = 1
        curNumerator = recurDigs[numerator]
        while curNumerator != numerator:
            cycLen += 1
            curNumerator = recurDigs[curNumerator]
        return cycLen

# init coPrimes with numbers divisible by 2 or 5 marked as false
coPrimes = [False, True, False, True, False, False, False, True, False, True]*((N/10) + 1)
bound = ceil(sqrt(N))
for i in range(int(bound)):
    if coPrimes[i]:
        for j in range(i, N // i):
            coPrimes[i * j] = True
    
maxCyc = 0
maxCycLen = 0
for i in range(N + 1):
    if coPrimes[i]:
        cycLen = getCycLen(i)
        if cycLen > maxCyc:
            maxCyc = i
            maxCycLen = cycLen

print(maxCyc)
print(maxCycLen)
