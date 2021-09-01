
def check_user_input(max_num):
    message = "Введите цифру для выбора пункта меню(exit - выход): "
    help_message =f"Введите число от 1 до {max_num} или exit для выхода."
    while True:
        user_input = input(message)
        if user_input.isdigit():
            user_input = int(user_input)
            if max_num >= user_input > 0:
                return user_input
        elif user_input == "exit":
            return user_input
        
        print(help_message)


def user_answer():

    # Меню пользователя БД
    user_menu = """
         _______________________________________________
        /            МЕНЮ ДЛЯ РАБОТЫ С БД               \\
        | 1. Посмотреть все авто     2. Добавить авто   |
        | 3. Найти авто              4. Изменить данные |
        | 5. Удалить                 6. Выход           |
        \_______________________________________________/
    """
    max_number_menu = 6
    print(user_menu)
    return check_user_input(max_num=max_number_menu)


def customer_answer():

    # Меню покупателя
    customer_menu = """
         _______________________________________________
        /            МЕНЮ ПОКУПОК                       \\
        | 1. Посмотреть все авто   2. Добавить в корзину|
        | 3. Оплатить покупку(и)                        |
        \_______________________________________________/
    """
    max_number_menu = 3
    print(customer_menu)
    return check_user_input(max_num=max_number_menu)
