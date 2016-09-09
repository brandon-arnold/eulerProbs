from math import sqrt

# sieve proper divisors into each sum
F = [3,1]*(28124 / 2)
for i in range(3, 28123 / 2):
	for j in range(2, (28123 / i)):
		F[i * j] += i

# mark sums of two abundant numbers
Sa = [False,]*28124
for i in range(12, 28123):
	for j in range(i, 28123 - i, 1):
		if F[i] > i and F[j] > j:
			Sa[i + j] = True

# sum numbers not a sum of two abundant numbers
sum = 0
numbersIncluded = []
for i in range(1, 28123):
	if not Sa[i]:
		numbersIncluded.append(i)
		sum += i
		
print(numbersIncluded)
print(str(sum))
