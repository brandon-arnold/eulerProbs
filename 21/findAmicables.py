def sumDivisors(n):
    divisorSum = 1
    sqrtN = int(n ** 0.5)
    for i in range(2, sqrtN + 1):
        if n % i == 0:
            divisorSum += i
            if i * i != n:
                divisorSum += n // i
    return divisorSum

sums = [sumDivisors(i) for i in range(2, 10001)]
sumsAlternate = [sumDivisors(i) for i in sums]
sumAmicable = 0
for i in range(2, 10001):
    if i != sums[i - 2] and i == sumsAlternate[i - 2]:
        sumAmicable += i
print(str(sumAmicable))
