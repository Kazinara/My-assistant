print("Добро пожаловать в калькулятор.")
num_one = int(input("Введите первое число: "))
sign = input("Введите знак: ")
num_two = int(input("Введите второе число: "))
if sign == "+":
    result = num_one + num_two
    print(result)
elif sign == "-":
    result = num_one - num_two
    print(result)
elif sign == "*":
    result = num_one * num_two
    print(result)
elif sign == "/":
    result = num_one / num_two
    print(result)
elif sign == "**":
    result = num_one ** num_two
    print(result)
else:
    print("Некорректный ввод знака")
