def calculate_bread_cost(quantity):
    # Цена за буханку хлеба
    regular_price = 49.0
    
    # Скидка на вчерашний хлеб в процентах
    discount_percentage = 60
    
    # Расчет цены со скидкой
    discounted_price = regular_price - (regular_price * (discount_percentage / 100))
    
    # Общая стоимость
    total_cost = quantity * discounted_price
    
    return regular_price, discounted_price, total_cost

def main():
    try:
        # Запрашиваем у пользователя количество приобретенных вчерашних буханок хлеба
        quantity = int(input("Введите количество приобретенных вчерашних буханок хлеба: "))
        
        # Рассчитываем стоимость
        regular_price, discounted_price, total_cost = calculate_bread_cost(quantity)
        
        # Выводим результаты на экран с форматированием
        print(f"Обычная цена за буханку: {regular_price:.2f}")
        print(f"Цена со скидкой: {discounted_price:.2f}")
        print(f"Общая стоимость приобретенного хлеба: {total_cost:.2f}")
    
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число для количества буханок.")

# Вызываем основную функцию
if __name__ == "__main__":
    main()
