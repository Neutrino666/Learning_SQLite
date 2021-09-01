# -*- coding: utf-8 -*-

from database_engine import CarDatabase
from user_engine import user_answer

db_name = 'cars.db'
user_choice = None
car_database = CarDatabase(db_name=db_name)

# создать таблицу если её нет
car_database.create_bd()

while True:
    user_choice = user_answer()

    if user_choice == 1:    # Показать таблицу
        car_database.show_cars()
    elif user_choice == 2:  # Добавить в таблицу
        car_database.add_car_in_bd()
    elif user_choice == 3:  # Найти в таблице
        car_database.find_car()
    elif user_choice == 4:  # Изменить
        car_database.update_bd()
    elif user_choice == 5:  # Удалить
        car_database.del_car()
    elif user_choice == 6 or user_choice == "exit":  # Выход
        break
    else:
        print(f"Выберите пункт меню - {user_choice} не корректен!")

input("Press enter to exit")