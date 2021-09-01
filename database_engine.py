import sqlite3


class CarDatabase:

    def __init__(self, db_name):
        # Создание таблицы если её нет
        self.db_name = db_name

        try:
            with sqlite3.connect(self.db_name) as db_connection:
                cursor = db_connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model TEXT NOT NULL,
                    color TEXT NOT NULL,
                    price INT NOT NULL)
                """)
                db_connection.commit()

        except sqlite3.Error as error:
            print(f'Error: {error} while connecting to {self.db_name}')

    def add_car_in_bd(self):
        # Добваление новых значений в таблицу

        while True:
            car_info = input('Модель(без пробелов, "-" и ".")/цвет/цена (выход - exit): \n').split("/")
            if car_info[0] == "exit":
                return None
            if len(car_info) != 3:
                continue
            elif car_info[0].isalnum and car_info[1].isalpha and car_info[2].isdigit:
                break

        with sqlite3.connect(self.db_name) as db_cars_conn:
            cursor = db_cars_conn.cursor()
            cursor.execute("""INSERT INTO cars(model, color, price) 
                VALUES (?, ?, ?)""", car_info)
            db_cars_conn.commit()

    def create_bd(self):
        # Создание таблицы
        try:
            with sqlite3.connect(self.db_name) as db_connection:
                cursor = db_connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model TEXT NOT NULL,
                    color TEXT NOT NULL,
                    price INT NOT NULL)
                """)
                db_connection.commit()

        except sqlite3.Error as error:
            print(f'Error: {error} while connecting to {self.db_name}')

    def find_car(self):
        # Поиск по модели
        massage = (
                "Введите модель автомобиля которую надо найти\n" +
                "(без пробелов, только буквы) или exit: "
        )
        while True:
            model = self.check_model_car(massage=massage)
            with sqlite3.connect(self.db_name) as db_connection:
                cursor = db_connection.cursor()
                find_request = "SELECT * FROM cars WHERE model = ?"
                cursor.execute(find_request, (model,))
                result = cursor.fetchall()
                if result:
                    print(*result)
                    break
                elif result == "exit":
                    break
                elif not result:
                    print("Данной модели нет в БД")
                else:
                    print("Непредвиденные данные ", result)

    def show_cars(self):
        # Просмотр таблицы
        with sqlite3.connect(self.db_name) as db_connection:
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM cars")
            for res in cursor:
                print(res)

    def del_car(self):
        # Удаление по модели
        model = None
        while True:
            massage = "Введите модель автомобиля которую надо удалить\n"
            model = input(massage)
            if model == "exit":
                break
            if model:
                with sqlite3.connect(self.db_name) as db_connection:
                    cursor = db_connection.cursor()
                    cursor.execute("DELETE FROM cars WHERE model = ?", (model,))
                    db_connection.commit()
                    self.show_cars()
                    print("Актуальная база данных")
                    break
            else:
                print("Непредвиденная ошибка, ", model)

    def check_id(self, id):
        # Проверка наличия id
        with sqlite3.connect(self.db_name) as db_connection:
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM cars WHERE car_id = ?", (id,))
            result = cursor.fetchall()
            if result:
                print(result)  # вывод на экран строки по id
                return True
            else:
                return False

    def check_model_car(self, massage):
        # Проверка корректности ввода по модели
        while True:
            model = input(massage)
            if model.isalpha():
                return model
            elif model == 'exit':
                return None

    def check_collect_update_data(self, names_columns, user_input):
        # Проверяет корректность собранных данных
        cach_name = None
        for column in names_columns:
            for value in user_input:
                if len(value.split("=")) != 2:
                    return False
                column_name, column_value = value.split("=")
                if column_name in column and cach_name != column:
                    if len(column_name) != len(column):
                        return False
                    if column_name == "model" or column_value == "color":
                        if not column_value.isalpha():
                            print("Ошибка ошибка ошибка")
                            return False
                    if column_name == "price":
                        if not column_value.isdigit():
                            print("Ошибка ошибка ошибка")
                            return False
                    if column_name not in names_columns:
                        return False
        return True

    def collect_update_data(self):
        # Собирает нужные данные для вбивания
        massage = """
            Напишите что хотите изменить,
            формат записи ниже(exit для выхода)
            model=нива/color=красный/price=500000
            """
        error_message = "Введите корректные данные!"
        names_columns = "model", "color", "price"

        while True:
            user_input = input(massage).split("/")
            if user_input[0] == "exit":
                return None
            if 3 < len(user_input) or user_input == [""]:
                print("Количество колонок не верное!!", error_message)
                continue
            if self.check_collect_update_data(names_columns=names_columns, user_input=user_input):
                return user_input
            else:
                print(error_message)

    def get_update_data(self):
        # Получает необходимые данные для внесения в БД
        massage = (
                "Введите id авто из БД для изменения\n" +
                "(exit для выхода из меню обновления): "
        )
        id = input(massage)

        while True:
            if id == "exit":
                return None
            if id.isdigit():
                if self.check_id(id=id):
                    break
            print("id введен не корректно либо его нет в БД!")
            id = input(massage)

        new_data = self.collect_update_data()
        if new_data is None:
            return new_data
        return new_data, id

    def update_bd(self):
        # Вносит обновленные данные
        update_data = self.get_update_data()
        if update_data:
            update_command = "UPDATE cars SET"
            filter_id = f" WHERE car_id = ?"
            id_car = int(update_data[1])
            record_list = list()
            for values in update_data[:-1]:
                for value in values:
                    title, parameter_car = value.split("=")
                    update_command += f" {title} = ?,"
                    record_list.append(parameter_car)
            update_command = update_command[:-1] + filter_id
            record_list.append(id_car)
            with sqlite3.connect(self.db_name) as db_cars_conn:
                cursor = db_cars_conn.cursor()
                cursor.execute(update_command, record_list)
                db_cars_conn.commit()
            self.show_cars()
        elif update_data is None:
            print("Отмена изменений")
        else:
            print("Непредвиденная ошибка!")


class Customer:
    pass