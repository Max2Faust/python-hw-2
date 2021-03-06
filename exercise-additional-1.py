# Напишіть функцію sumNum що задовільняє наступній умові:

# Дано ціле число num, 
# декілька кілька разів додайте всі його цифри, 
# доки в результаті не буде лише одна цифра, і поверніть її.

# Приклад 1
# sumNum(40) -> 4

# Для числа 40 потріботно повернути 4, чому?
# 1. 40 - розкладаємо на цифри -> 4, 0
# 2. Складаємо цифри 4 + 0 = 4
# 3. 4 - це одна цифра, повертаємо її

# Приклад 2
# sumNum(48) -> 3

# Для числа 48 потріботно повернути 3, чому?
# 1. 48 - розкладаємо на цифри -> 4, 8
# 2. Складаємо цифри 4 + 8 = 12
# 3. 12 - розкладаємо на цифри -> 1, 2
# 4. Складаємо цифри 1 + 2 = 3
# 5. 3 - це одна цифра, повертаємо її

# Приклад 3
# sumNum(2) -> 2

# Для числа 2 потріботно повернути 2, тому що число 2 складається з однієї цифри.

def sumNum(num):
	if str(num).isdigit():
		while len(str(num)) > 1: 
			sum = 0 
			for i in range(len(str(num))):
				sum += int(str(num)[i])
			num = sum
		return num
	else:
		print ('Illegal sumNum arg')

print(sumNum(38) == 2) 
print(sumNum(40) == 4)
print(sumNum(48) == 3) 
print(sumNum(2) == 2)
