import math

def isPythagTrip(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2);

def findPythagTrip(N):
    for c in range(N / 3, N):
        [a, b] = [c - 2, c - 1]
        sum = a + b + c
        while sum >= N:
            while b > a:
                if sum == N:
                    if isPythagTrip(a, b, c):
                        return [a, b, c];
                b = b - 1
            a = a - 1
            b = c - 1
            sum = a + b + c

print findPythagTrip(1000)
