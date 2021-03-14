
# Convert M to CM
m = eval(input('enter meter : '))
cm = m * 100
print('cm = ', cm)

# 1 USD = 1450 IQD
# Convert from IQD to USD
iqd = eval(input('\n\nIQD : '))
usd = iqd / 1450
print('USD : ', usd)
print('USD with Round 2', round(usd, 2))  # 0,##
print("USD with Round 3: %.3f" % float(usd))  # 0,###

# Convert from USD to IQD
usd = eval(input('\n\nUSD :'))
iqd = usd * 1.45
print('IQD : ', iqd)

# Convert Day to Month
days = int(input('\n\nDays : '))
months = int(days / 30)
days = int(days % 30)
print('Months : ', months, '\t Days : ', days)

# Convert Day to Month
days = int(input('\n\nDays : '))
months = days // 30
days = int(days % 30)
print('Months : ', months, '\t Days : ', days)

# Convert Min to Sec
sec = int(input('SEC : '))
mins = sec // 60
print('Min : ', mins, '\t Sec : ', sec % 60)

# sum 2 digit
number = int(input('enter 2 digit : '))
firstNumber = number // 10
secondNumber = number % 10
sumNumber = firstNumber + secondNumber
print(sumNumber)

# sum 3 digit
x = int(input('enter 3 digit :'))
firstNumber = x // 100
x %= 100
secondNumber = x // 10
thirdNumber = x % 10
sumNumber = firstNumber + secondNumber + thirdNumber
print(sumNumber)

number = input('enter 3 digit :')
firstNumber = int(number) // 100
secondNumber = (int(number) // 10) % 10
thirdNumber = int(number) % 10
sumNumber = firstNumber + secondNumber + thirdNumber
print(sumNumber)


