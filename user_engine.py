
def user_answer():
    # Меню пользователя

    user_menu = """
         _______________________________________________
        /            МЕНЮ ДЛЯ РАБОТЫ С БД               \\
        | 1. Посмотреть все авто     2. Добавить авто   |
        | 3. Найти авто              4. Изменить данные |
        | 5. Удалить                 6. Выход           |
        \_______________________________________________/
    """

    print(user_menu)
    message = "Введите цифру для выбора пункта меню(exit - выход): "
    help_message ="Введите число от 1 до 6 или exit для выхода."

    while True:
        user_input = input(message)
        if user_input.isdigit():
            user_input = int(user_input)
            if 6 >= user_input > 0:
                return user_input
        elif user_input == "exit":
            return user_input
        else:
            print(help_message)
