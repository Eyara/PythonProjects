a = int(input(("Введите число")))
b = int(input(("Введите число")))
c = str(input(("Введите знак")))
def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Неизвестная операция"
print (arithmetic(a, b, c))
