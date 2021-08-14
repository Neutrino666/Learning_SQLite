import sqlite3


def add_car_in_bd(db_cars, date_car):
    with sqlite3.connect(db_cars) as db_cars_conn:
        cursor = db_cars_conn.cursor()
        cursor.execute("""INSERT INTO cars(model, color, price) 
            VALUES (?, ?, ?)""", date_car)
        db_cars_conn.commit()


def create_bd(db_name):
    try:
        with sqlite3.connect(db_name) as sqlite_connection:
            cursor = sqlite_connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                color TEXT NOT NULL,
                price INT NOT NULL)
            """)
            sqlite_connection.commit()

    except sqlite3.Error as error:
        print(f'Error: {error} while connecting to {db_name}')


db_name = 'cars.db'
date_car = (
    ('lada', 'blue', 200000),
    ('mazda', 'yellow', 5000000)
)

create_bd(db_name=db_name)

for car_info in date_car:
    add_car_in_bd(db_cars=db_name, date_car=car_info)
