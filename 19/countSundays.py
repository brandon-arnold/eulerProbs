fromSunday = [0, 6, 5, 4, 3, 2, 1]
year = 1901
weekday = 2
numSundays = 0
yearLen = 365
while year < 2001:
    if year % 4 != 0: yearLen = 365
    else: yearLen = 366
    numSundaysThisYear = int((yearLen - fromSunday[weekday]) // 7) + 1
    numSundays += numSundaysThisYear
    print("year: %i, numSundays: %i" %(year, numSundaysThisYear))
    weekday = (yearLen + weekday) % 7
    year += 1
print(str(numSundays))
