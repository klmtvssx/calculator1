a = float(input("Биринчи сан: "))
op = input("Операция (+, -, *, /): ")
b = float(input("Экинчи сан: "))

if op == "+":
    print("Жооп:", a + b)
elif op == "-":
    print("Жооп:", a - b)
elif op == "*":
    print("Жооп:", a * b)
elif op == "/":
    if b == 0:
        print("Бөлүү мүмкүн эмес !")
    else:
        print("Жооп:", a / b)
else:
    print("Туура эмес операция тандалды.")
