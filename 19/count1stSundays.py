monthLens = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 0
year = 1901
firstWeekday = 2
numSundays = 0
while year < 2001:
    if firstWeekday == 0: numSundays += 1
    firstWeekday = (monthLens[month] + firstWeekday) % 7
    month = (month + 1) % 12
    if month == 0: year += 1
    if year % 4 != 0: monthLens[1] = 28
    else: monthLens[1] = 29
print(str(numSundays))
