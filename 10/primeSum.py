import sys;
from bitarray import bitarray
from math import sqrt

#
# Outputs
#
sum = 2

#
# Get/validate argument
#
if len(sys.argv) != 2:
    print("Must provide exactly one parameter. Usage: primeSum <N>")
    sys.exit()
n = 0
try:
    n = int(sys.argv[1])
except ValueError:
    print("Provided parameter is not an integer.")
    sys.exit()

#
# Create bitmap
#
bMap = bitarray()
bMap.extend((0, 1, ) * (n / 2))

#
# Perform prime sieve, with sqrt(n) as the upper bound
#
floorSqrtN = int(sqrt(n))
for i in range(3, floorSqrtN + 1):
    if not bMap[i - 1]:
        sum += i
        multiple = i * i
        while multiple < n:
            bMap[multiple - 1] = True
            multiple += i

#
# sum the remaining primes greater than sqrt(n)
#
for i in range(floorSqrtN + 1, n - 1):
    if not bMap[i - 1]:
        sum += i

#
# Output result
#
print("Sum of primes less than " + sys.argv[1] + ": " + str(sum))
