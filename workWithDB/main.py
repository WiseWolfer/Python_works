import psycopg2
from psycopg2 import Error


if __name__ == '__main__':
    try:
        connection = psycopg2.connect(dbname='testdb',
                               user='Dimacik',
                               password='worldoftanks228F',
                               host='127.0.0.1',
                               port="5432"
                               )
        print("Соединение с БД успешно установлено!")
        # создал курсор для работы с бд
        cursor = connection.cursor()
        cursor.execute('''Select * from employees;''')
        connection.commit()
        records = cursor.fetchall()
        print('Данные из бд:', records)
    # если ошибка в запросе
    except(Exception, Error) as er:
        print("Ошибка при работе с PostgreSQL", er)
    # всегда отрабатывает при открытии соединения с базой
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
