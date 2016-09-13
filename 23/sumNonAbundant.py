# (it is provable that all integers greater
# than 28123 are a sum of two abudant numbers)
N = 28123

# sum proper divisors using sieve approach
F = [1] * (N + 1)
for i in range(2, N / 2):
    for j in range(2, (N / i) + 1):
        F[i * j] += i

# capture abundant numbers
A = [i for i in range(1, N) if F[i] > i]

# mark sums of two abundant numbers
Sa = [False] * (2 * N + 1)  # size of 2N guarantees no index out of range error
for i in range(0, len(A)):
    for j in range(0, i + 1):
        Sa[A[i] + A[j]] = True

# capture all numbers that are not abundant sums and add them up
nonAbundantSums = [i for i in range(1, N) if not Sa[i]]
print(sum(nonAbundantSums))
