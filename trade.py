# -*- coding: utf-8 -*-

from user_engine import customer_answer
from database_engine import CarDatabase, Customer

db_name = 'cars.db'
customer_choice = None
car_database = CarDatabase(db_name=db_name)
customer = Customer

while True:
    user_choice = customer_answer()

    if user_choice == 1:    # Показать таблицу
        car_database.show_cars()
    elif user_choice == 2:  # Добавить в корзину
        pass
    elif user_choice == 3:  # Оплатить покупку
        pass
    elif user_choice == "exit":  # Выход
        break
    else:
        print(f"Выберите пункт меню - {user_choice} не корректен!")

input("Press enter to exit")
