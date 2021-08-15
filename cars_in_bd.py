import sqlite3


def add_car_in_bd(db_cars, car_info):
    with sqlite3.connect(db_cars) as db_cars_conn:
        cursor = db_cars_conn.cursor()
        cursor.execute("""INSERT INTO cars(model, color, price) 
            VALUES (?, ?, ?)""", car_info)
        db_cars_conn.commit()


def create_bd(db_name):
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


db_name = 'cars.db'
date_car = (
    ('lada', 'blue', 200000),
    ('mazda', 'yellow', 5000000)
)

create_bd(db_name=db_name)

for car_info in date_car:
    add_car_in_bd(db_cars=db_name, car_info=car_info)

with sqlite3.connect(db_name) as db_conn:
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM cars")
    for result in cursor:
        print(result)
