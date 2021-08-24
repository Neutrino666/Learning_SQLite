# -*- coding: utf-8 -*-

from car_in_bd_engine import add_car_in_bd, create_bd, show_cars, user_answer, find_car
from car_in_bd_engine import del_car, update_bd

db_name = 'cars.db'
cars_data = (
    ('lada', 'blue', 200000),
    ('mazda', 'yellow', 5000000)
)
user_choice = None

# создать таблицу если её нет
create_bd(db_name=db_name)

while True:
    user_choice = user_answer()

    if user_choice == 1:    # Показать таблицу
        show_cars(db_name=db_name)
    elif user_choice == 2:  # Добавить в таблицу
        add_car_in_bd(db_cars=db_name)
    elif user_choice == 3:  # Найти в таблице
        find_car(db_name=db_name)
    elif user_choice == 4:  # Изменить
        update_bd(db_name=db_name)
    elif user_choice == 5:  # Удалить
        del_car(db_name=db_name)
    elif user_choice == 6 or user_choice == "exit":  # Выход
        break
    else:
        print(f"Неверный ввод данных {user_choice}")

input("Press enter to exit")
