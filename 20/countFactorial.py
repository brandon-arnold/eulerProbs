import math
n = 100
print(reduce(lambda x,y: x + int(y), str(math.factorial(n)), 0))
