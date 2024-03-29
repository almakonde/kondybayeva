# -*- coding: utf-8 -*-
"""hw_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VKkunVX8jKg0nAci391mUYuEXq33YqW

**Навигация по уроку**

1. [Нейронные сети. Математическая модель нейрона.](https://colab.research.google.com/drive/1XXxO2vyd9IDYT23tQrVMAAYeHYn-Awww)
2. [Нейронные сети. Функции активации](https://colab.research.google.com/drive/1mhEEhb3mdE5mKFIvOiC5tHvkPiWD8DBj)
3. Домашняя работа

## Задача 1. Класс Neuron

**Условие** Используя примеры из теоретической части 5.1 и 5.2, составьте класс Neuron модели нейрона, принимающего на вход от одного до 10 входных параметров. Для последнего параметра используется вес $x_n$ = 1, таким образом $w_n=b$ - является смещением. Запрещается пользоваться библиотекой numpy. На вход подается список. Матричное умножение реализуется с помощью циклов самостоятельно. Класс содержит методы для вычисления взвешенной суммы, а также содержит функции активации из урока.
"""

#Напишите свое решение
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def weighted_sum(self, inputs):
        # Проверяем, что количество весов и входных параметров совпадает
        if len(self.weights) != len(inputs):
            raise ValueError("Количество весов должно быть равно количеству входных параметров.")

        # Вычисляем взвешенную сумму
        weighted_sum = self.bias
        for i in range(len(inputs)):
            weighted_sum += self.weights[i] * inputs[i]

        return weighted_sum

    def step_activation(self, weighted_sum):
        # Функция активации - ступенчатая функция (пороговая)
        return 1 if weighted_sum >= 0 else 0

    def sigmoid_activation(self, weighted_sum):
        # Функция активации - сигмоидальная функция
        import math
        return 1 / (1 + math.exp(-weighted_sum))

# Пример использования
if __name__ == "__main__":
    # Создаем объект нейрона с тремя весами и смещением
    neuron = Neuron(weights=[0.5, -0.2, 0.1], bias=0.5)

    # Пример входных параметров
    inputs = [0.3, -0.8, 1.0]

    # Вычисляем взвешенную сумму
    weighted_sum_result = neuron.weighted_sum(inputs)
    print("Взвешенная сумма:", weighted_sum_result)

    # Применяем функцию активации (ступенчатая)
    step_activation_result = neuron.step_activation(weighted_sum_result)
    print("Результат ступенчатой функции активации:", step_activation_result)

    # Применяем функцию активации (сигмоидальная)
    sigmoid_activation_result = neuron.sigmoid_activation(weighted_sum_result)
    print("Результат сигмоидальной функции активации:", sigmoid_activation_result)

"""## Задача 2. Класс Neuron (продолжение)

**Условие.** Используя класс Neuron из первой задачи, придумать свой пример на принятие решения (по аналогии с задачей "о рыбаке и рыбке"), не менее 4 входных параметров, веса установить произвольно из логики задачи, произвести расчёт функций активаций, определённых в классе первой задачи.
"""

# Импортируем класс Neuron из предыдущего примера

# Создаем объект нейрона с произвольными весами и смещением
neuron_cafe_decision = Neuron(weights=[0.5, 0.3, -0.2, 0.4], bias=0.1)

# Входные параметры для решения об открытии кафе
weather = -3  # теплая погода
cafe_rating = 2  # высокий рейтинг кафе
ingredient_availability = 9  # хорошая доступность сырья
economic_condition = 2  # хорошая экономическая ситуация

# Составляем список входных параметров
inputs = [weather, cafe_rating, ingredient_availability, economic_condition]

# Вычисляем взвешенную сумму
weighted_sum_result = neuron_cafe_decision.weighted_sum(inputs)

# Применяем функцию активации (ступенчатая)
step_activation_result = neuron_cafe_decision.step_activation(weighted_sum_result)

# Применяем функцию активации (сигмоидальная)
sigmoid_activation_result = neuron_cafe_decision.sigmoid_activation(weighted_sum_result)

# Выводим результаты
print(f"Взвешенная сумма: {weighted_sum_result}")
print(f"Решение (ступенчатая функция): {step_activation_result}")
print(f"Решение (сигмоидальная функция): {sigmoid_activation_result}")