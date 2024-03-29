# -*- coding: utf-8 -*-
"""Copy of 4.3. Домашняя работа

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NY1pY-_od5mvkvUOuO1E9GLiXgABhUj4

**Навигация по уроку**

1. [ Функции. Классы и объекты. Програмные модули](https://colab.research.google.com/drive/1LtSAdLzWIP-xTADXIktKF9yxsh0ioEqN#scrollTo=O0dFTIuYGKI4)
2. [Практика](https://colab.research.google.com/drive/1GblqLwJKMaNBV4cIyrbQqt7Rsf-7Bbx7)
3. Домашняя работа

## Задача 1. Случайный номерной знак

**Условие.** Представьте, что в вашем регионе устаревшим является формат номерных автомобильных знаков из трех букв, следом за которыми идут три цифры. Когда все номера такого шаблона закончились, было решено обновить формат, поставив в начало четыре цифры, а за ними три буквы.
Напишите функцию, которая будет генерировать случайный номерной знак. При этом номера в старом и новом форматах должны создаваться примерно с одинаковой вероятностью. В основной программе нужно сгенерировать и вывести на экран случайный номерной знак.
"""

#Напишите свое решение
import random

def generate_license_plate():
    # Выбираем случайный формат (старый или новый) с равной вероятностью
    is_old_format = random.choice([True, False])

    if is_old_format:
        # Генерируем номер в старом формате: три буквы + три цифры
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        numbers = ''.join(random.choices('0123456789', k=3))
        license_plate = f"{letters}{numbers}"
    else:
        # Генерируем номер в новом формате: четыре цифры + три буквы
        numbers = ''.join(random.choices('0123456789', k=4))
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        license_plate = f"{numbers}{letters}"

    return license_plate

# Генерируем и выводим случайный номерной знак
random_license_plate = generate_license_plate()
print(f"Случайный номерной знак: {random_license_plate}")

"""## Задача 2. Шестнадцатеричные и десятичные числа

**Условие.** Напишите две функции с  именами hex2int и  int2hex для конвертации
значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функция hex2int должна принимать на вход строку с единственным символом в  шестнадцатеричной системе и  преобразовывать его в  число от нуля до 15 в десятичной системе, тогда как функция int2hex будет выполнять обратное действие – принимать десятичное число из диапазона от 0 до 15 и возвращать шестнадцатеричный эквивалент. Обе функции должны принимать единственный параметр со входным значением и возвращать преобразованное число. Удостоверьтесь, что функция hex2int корректно обрабатывает буквы в верхнем и нижнем регистрах. Если введенное пользователем значение выходит за допустимые границы, вы должны вывести сообщение об ошибке.
"""

#Напишите свое решение
def hex2int(hex_value):
    try:
        # Преобразуем шестнадцатеричное значение в десятичное
        decimal_value = int(hex_value, 16)

        # Проверяем, что результат в диапазоне от 0 до 15
        if 0 <= decimal_value <= 15:
            return decimal_value
        else:
            raise ValueError("Ошибка: Введенное значение выходит за допустимые границы (0-15).")

    except ValueError:
        raise ValueError("Ошибка: Некорректное шестнадцатеричное значение.")

def int2hex(decimal_value):
    try:
        # Проверяем, что десятичное значение в диапазоне от 0 до 15
        if 0 <= decimal_value <= 15:
            # Преобразуем десятичное значение в шестнадцатеричное
            hex_value = hex(decimal_value)[2:].upper()
            return hex_value
        else:
            raise ValueError("Ошибка: Введенное значение выходит за допустимые границы (0-15).")

    except ValueError:
        raise ValueError("Ошибка: Некорректное десятичное значение.")

# Пример использования
try:
    hex_input = input("Введите шестнадцатеричное значение (0-9, A-F): ").upper()
    decimal_result = hex2int(hex_input)
    print(f"Десятичное значение: {decimal_result}")

    decimal_input = int(input("Введите десятичное значение (0-15): "))
    hex_result = int2hex(decimal_input)
    print(f"Шестнадцатеричное значение: {hex_result}")

except ValueError as e:
    print(e)

"""hex(decimal_value): Эта часть кода преобразует десятичное число decimal_value в его шестнадцатеричное представление в виде строки. Например, если decimal_value равно 10, то hex(10) вернет строку '0xa'.

    [2:]: Этот срез используется для исключения первых двух символов из строки, полученной в результате шестнадцатеричного преобразования. В шестнадцатеричной записи '0xa', '0x' - это префикс, и исключив его, мы получаем только символы, представляющие само значение (в данном случае, 'a').

    .upper(): Этот метод преобразует все символы строки в верхний регистр. Это важно, так как шестнадцатеричные числа могут быть представлены как в верхнем, так и в нижнем регистре букв (например, 'a' и 'A' обозначают одно и то же значение). Это обеспечивает единообразие и предотвращает путаницу.

Таким образом, выражение hex(decimal_value)[2:].upper() преобразует десятичное число в шестнадцатеричную строку и затем форматирует эту строку, чтобы она соответствовала стандарту, где буквы представлены в верхнем регистре, и удаляет префикс "0x".

## Задача 3. Беспилотный автомобиль

**Условие.** Это творческая задача. Представьте, что вы проектируете беспилотный автомобиль. Вам необходимо продумать, какими свойствами он обладает и какие действия совершает. Создайте класс беспилотный автомобиль и сохраните его в виде программного модуля. Импортируете класс и инициализируйте новый объект.
"""

#Напишите свое решение
# Создание файла car.py (ваш программный модуль)

class AutonomousCar:
    def __init__(self, make, model, year, autopilot_enabled=False):
        self.make = make
        self.model = model
        self.year = year
        self.autopilot_enabled = autopilot_enabled
        self.speed = 0

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"The {self.year} {self.make} {self.model} is accelerating to {self.speed} km/h.")

    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        if self.speed < 0:
            self.speed = 0
        print(f"The {self.year} {self.make} {self.model} is slowing down to {self.speed} km/h.")

    def engage_autopilot(self):
        if self.autopilot_enabled:
            print(f"The autopilot is now engaged for the {self.year} {self.make} {self.model}.")
        else:
            print("Error: Autopilot is not available for this car.")

# Инициализация объекта беспилотного автомобиля

# Импорт класса из файла car.py
#from car import AutonomousCar

# Создание объекта
my_autonomous_car = AutonomousCar(make="Tesla", model="Model S", year=2023, autopilot_enabled=True)

# Вызов методов объекта
my_autonomous_car.start()
my_autonomous_car.accelerate(50)
my_autonomous_car.engage_autopilot()
my_autonomous_car.brake(20)
my_autonomous_car.stop()