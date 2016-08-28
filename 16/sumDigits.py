power = 1000
digits = [1]
carry = 0
while power > 0:
    for i in range(len(digits)):
        product = digits[i] * 2 + carry
        digits[i] = product % 10
        carry = 0 if product < 10 else int(product // 10)
    while carry > 0:
        digits.append(carry % 10)
        carry //= 10
    power -= 1

print(str(sum(i for i in digits)))
