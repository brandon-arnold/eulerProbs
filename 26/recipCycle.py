from math import ceil, sqrt

N = 1000

# init coPrimes with numbers divisible by 2 or 5 marked as false
coPrimes = [False, True, False, True, False, False, False, True, False, True]*((N/10) + 1)
bound = ceil(sqrt(N))
for i in range(bound):
    if coPrimes[i]:
        for j in range(i, n // i):
            coPrimes[i * j] = True

