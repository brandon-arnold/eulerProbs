import time
start_time = time.time()

lookupMin =  60000000
lookupMax = 110000000
divCount = 500
D = [2]*(lookupMax - lookupMin)
T = [False]*(lookupMax - lookupMin)

# mark all triangular numbers in the lookup range
curTriI = 2
sum = 3
while sum < lookupMin:
    curTriI += 1
    sum += curTriI
while sum < lookupMax:
    T[sum - lookupMin] = True
    curTriI += 1
    sum += curTriI

# sift divisors less than lookupMin within lookup range
for i in range(2, lookupMin):
    for j in range((lookupMin // i + 1) * i, lookupMax // 2, i):
        D[j - lookupMin] += 1

# continue sifting, but start comparing divisor count
result = 0
maxDivisors = 2
maxDivTri = 1
for i in range(lookupMin, lookupMax):
    if T[i - lookupMin]:
        if D[i - lookupMin] >= divCount:
            print("Triangle number " + str(i) + " has " + str(D[i - lookupMin]) + " divisors.")
            print(" %s seconds" % str(time.time() - start_time))
            result = i
            break
        else:
            if D[i - lookupMin] > maxDivisors:
                maxDivisors = D[i - lookupMin]
                maxDivTri = i
    for j in range(i, lookupMax // 2, i):
        D[j - lookupMin] += 1

if result == 0:
    print("No result found.")
    print("Max divisors is " + str(maxDivisors) + " for triangle number " + str(maxDivTri) + ".")
