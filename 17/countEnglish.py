digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def getEnglish(n):
    english = ""
    if n > 999 and n <= 999999:
        english += getEnglish(int(n // 1000)) + " thousand "
        n %= 1000
    if n > 99 and n <= 999:
        english += getEnglish(int(n // 100)) + " hundred "
        n %= 100
        if n > 0: english += " and "
    if n > 19 and n <= 99:
        ten = int(n // 10)
        english += tens[ten - 1] + " "
        n %= 10
    if n > 9 and n <= 19:
        english += teens[n - 10] + " "
    elif n > 0:
        english += digits[n]
    return english

total = 0
for i in range(1, 1001):
    total += sum(len(word) for word in getEnglish(i).split())

print(total)
