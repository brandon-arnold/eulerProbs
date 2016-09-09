# (it is provable that all integers greater
# than 28123 are a sum of two abudant numbers)
N = 28123

# sieve proper divisors into each sum
F = [1] * (N + 1)
for i in range(2, N / 2):
    for j in range(2, (N / i) + 1):
        F[i * j] += i

# capture abundant numbers
A = [ i for i in range(1, N) if F[i] > i]

# mark sums of two abundant numbers
Sa = [False] * (2 * N + 1)
for i in range(0, len(A)):
    for j in range(0, i + 1):
        Sa[A[i] + A[j]] = True

# sum numbers not a sum of two abundant numbers
result = sum([i for i in range(1, N) if not Sa[i]])
print(result)
