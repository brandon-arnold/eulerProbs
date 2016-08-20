import math

def isPythagTrip(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2);

def isAdd1000(a, b, c):
    return a + b + c == 1000;

def findPythagTrip1000():
    for c in range(334,1000):
        a = 1
        while a < c - 2:
            for b in range(a + 1, c - 1):
                if isAdd1000(a, b, c):
                    if isPythagTrip(a, b, c):
                        return [a, b, c];
            a = a + 1
