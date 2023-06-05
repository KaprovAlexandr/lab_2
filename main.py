def pr1():
    b = False
    a = input("Введите пароль: ")
    while not b == True:
        for i in range(len(a)):
            if a[i] >= "0" and a[i] <= "9":
                print("number")
                a = input("Введите пароль: ")
                b = False
                break
            elif ord(a[i]) >= 65 and ord(a[i]) <= 90:
                print("reg")
                a = input("Введите пароль: ")
                b = False
                break
            else:
                if len(a) < 6:
                    print("Пароль слишком короткий")
                    a = input("Введите пароль: ")
                else:
                    b = True

    c = input("Подтвердите пароль: ")
    while a != c:
        print("Пароли не совпадают")
        c = input("Подтвердите пароль: ")
    print("Вы зарегистрированы!")
pr1()

def pr2():
    a = input("Введите ваш номер места: ")
    if (int(a) % 2 == 0) and (int(a) >= 2 and int(a) <= 36):
        print("Купе, верхнее")
    elif (int(a) % 2 != 0) and (int(a) >= 1 and int(a) <= 35):
        print("Купе, нижнее")
    elif (int(a) % 2 == 0) and (int(a) >= 38 and int(a) <= 54):
        print("Боковое, верхнее")
    elif (int(a) % 2 != 0) and (int(a) >= 37 and int(a) <= 53):
        print("Боковое, нижнее")
    else:
        print("Такого места не существует!")
pr2()

def pr3():
    n = input()

    def f(n):
        if (int(n) % 4 == 0 and int(n) % 100 != 0) or (int(n) % 400 == 0):
            return "Год" + " " + str(n) + " " + "- високосный"
        else:
            return "Этот год не високосный"

    print(f(n))
pr3()

def pr4():
    cvet1 = input("Введите первый цвет:")
    cvet2 = input("Введите второй цвет:")
    if (cvet1 != "Красный" and cvet1 != "Синий" and cvet2 != "Желтый") and (
            cvet2 != "Красный" and cvet2 != "Синий" and cvet2 != "Желтый"):
        print("Неправильные цвета")
    else:
        if cvet1 == "Красный" and cvet2 == "Синий":
            print("Фиолетовый")
        elif cvet1 == "Красный" and cvet2 == "Желтый":
            print("Оранжевый")
        elif cvet1 == "Синий" and cvet2 == "Желтый":
            print("Зеленый")
pr4()