import sqlite3


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
    user_input = None

    print(user_menu)

    while True:
        user_input = input("Введите цифру для выбора пункта меню: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 6 >= user_input > 0:
                return user_input
        elif user_input == "exit":
            return user_input

        print("Введите число от 1 до 6")


def add_car_in_bd(db_cars):
    # Добваление новых значений в таблицу
    car_info = None

    while True:
        car_info = input('Модель(без пробелов, "-" и ".")/цвет/цена: \n').split("/")
        if len(car_info) != 3:
            continue
        elif car_info[0].isalnum and car_info[1].isalpha and car_info[2].isdigit:
            break

    with sqlite3.connect(db_cars) as db_cars_conn:
        cursor = db_cars_conn.cursor()
        cursor.execute("""INSERT INTO cars(model, color, price) 
            VALUES (?, ?, ?)""", car_info)
        db_cars_conn.commit()


def create_bd(db_name):
    # Создание таблицы
    try:
        with sqlite3.connect(db_name) as db_connection:
            cursor = db_connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                color TEXT NOT NULL,
                price INT NOT NULL)
            """)
            db_connection.commit()

    except sqlite3.Error as error:
        print(f'Error: {error} while connecting to {db_name}')


def check_model_car(massage):
    # Проверка корректности ввода по модели
    while True:
        massage = (
            "\n" + massage +
            "(без пробелов, только буквы) или exit: "
            )
        model = input(massage)
        if model.isalpha():
            return model
        elif model == 'exit':
            return None


def find_car(db_name):
    # Поиск по модели
    massage = "Введите модель автомобиля которую надо найти\n"

    model = check_model_car(massage=massage)
    if model:
        with sqlite3.connect(db_name) as db_connection:
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM cars WHERE model = ?", (model, ))
            result = cursor.fetchall()
            if result:
                return result
            else:
                return "Данной модели нет в БД"


def show_cars(db_name):
    # Просмотр таблицы
    with sqlite3.connect(db_name) as db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM cars")
        for res in cursor:
            print(res)


def del_car(db_name):
    # Удаление по модели
    massage = "Введите модель автомобиля которую надо удалить\n"
    model = check_model_car(massage=massage)
    with sqlite3.connect(db_name) as db_connection:
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM cars WHERE model = ?", (model, ))
        db_connection.commit()


def check_id(db_name, id):
    # Проверка корректности ввода id
    with sqlite3.connect(db_name) as db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM cars WHERE car_id = ?", (id, ))
        result = cursor.fetchall()
        if result:
            print(result) # вывод на экран строки по id
            return True
        else:
            return False


def check_collect_update_data():
    # Проверить корректность ввода для update 
    massage = """
        Напишите что хотите изменить формат записи ниже
        model=нива/color=красный/price=500000

    """
    while True:
        user_input = input(massage).split("/")


def collect_update_data(db_name, id):    
    check_collect_update_data()
    # Собирает нужные данные для вбивания


def get_update_data(db_name):
    # Получает необходим данные для ввода
    massage = (
            "Введите id авто из БД для изменения\n" +
            "(exit для выхода из меню обновления): "
        )
    id = input(massage)
    while True:
        if id == "exit":
                return None
        if id.isdigit():
            if check_id(db_name=db_name, id=id):           
                new_data = collect_update_data(db_name=db_name, id=id)
                if new_data == "exit":
                    return None
                elif new_data:
                    return new_data
        print("id введен не корректно либо его нет в БД")
        id = input(massage)


def update_bd(db_name):
    # Выполняет вбивание обновленных данных
    update_data = get_update_data(db_name)
    if update_data: 
        with sqlite3.connect(db_name) as db_cars_conn:
            cursor = db_cars_conn.cursor()
            cursor.execute(update_data)
            db_cars_conn.commit()
