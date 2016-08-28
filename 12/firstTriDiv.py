import time

pastCounts = {}
def countDivisors(n):
    global pastCounts
    if n in pastCounts:
        return pastCounts[n]
    unFactored = n
    divisorCount = 2
    denominator = 2
    curExponentCount = 1
    while unFactored != denominator:
        if unFactored % denominator == 0:
            curExponentCount += 1
            unFactored = unFactored // denominator
        else:
            if curExponentCount > 1:
                divisorCount *= curExponentCount
            curExponentCount = 1
            denominator += 2 if denominator != 2 else 1
    pastCounts[n] = divisorCount
    return divisorCount

start_time = time.time()
k = 2
while True:
    kDivisors = countDivisors(k)
    k2m1Divisors = countDivisors(2 * k - 1)
    k2p1Divisors = countDivisors(2 * k + 1)
    if kDivisors * k2m1Divisors > 500:
        print("Triangular sum " + str(k*(2*k - 1)) + " has " + str(kDivisors * k2m1Divisors) + " divisors.")
        print(" " + str(time.time() - start_time) + " seconds.")
        break
    elif kDivisors * k2p1Divisors > 500:
        print("Triangular sum " + str(k*(2*k + 1)) + " has " + str(kDivisors * k2p1Divisors) + " divisors.")
        print(" " + str(time.time() - start_time) + " seconds.")
        break
    k += 1
