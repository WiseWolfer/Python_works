import psycopg2
from psycopg2 import Error

if __name__ == '__main__':
    try:
        connection = psycopg2.connect(dbname='suppliers_choice',
                                      user='Dimacik',
                                      password='worldoftanks228F',
                                      host='127.0.0.1',
                                      port="5432")
        print("Соединение с БД успешно установлено!")
        # создал курсор для работы с бд
        name = ''
        cursor = connection.cursor()
        cursor.execute("DELETE from result_suppliers;")
        connection.commit()
        name_sql = cursor.execute("select 'Name_var' from result_suppliers")
        if name_sql == None:
            cursor.execute("Insert into result_suppliers Values('Доступные цены', 0, 100000, 'низкие', 'высокие');")
            cursor.execute(
                "Insert into result_suppliers Values('Выгодные для заказчика условия сотрудничества с поставщиком',"
                " 0, 40, 'малые оптовые скидки', 'высокие оптовые скидки');")
            connection.commit()
        cursor.execute('''Select * from result_suppliers;''')
        records = cursor.fetchall()
        print('База знаний из бд:', records)
        min_value_Price = records[0][1]
        max_value_Price = records[0][2]
        min_string_value_Price = records[0][3]
        max_string_value_Price = records[0][4]
        min_value_Benefit = records[1][1]
        max_value_Benefit = records[1][2]
        min_string_value_Benefit = records[1][3]
        max_string_value_Benefit = records[1][4]
        number_of_notes = int(input('Введите кол-во поставщиков оборудования и материалов: '))
        # Материалы
        # ТехноНИКОЛЬ Унифлекс ТПП 50 11777  3890 оптовых скидок нет
        # AKDS-STROY Унифлекс ТПП 50 10250 3560 оптовых скидок есть(30)
        # ГидролКровля Унифлекс ТПП 50 10875 3500 оптовых скидок есть(15)
        # Оборудование
        # Элек-Трансфер Счетчик Меркурий 20  93846 600 оптовые скидки есть(20%)
        # Все_инструменты.ру Счетчик Меркурий 20  83100 290 оптовых скидок нет
        # Электромонтаж Счетчик Меркурий 20 88633 300 оптовых скидок да (10%)
        cursor.execute("DELETE from destributed_suppliers;")
        connection.commit()
        for k in range(number_of_notes):
            name_sql1 = cursor.execute("select 'Name_of_material' from destributed_suppliers")
            if cursor.execute("select 'Name_of_material' from destributed_suppliers") != name_sql1 or \
                    cursor.execute("select 'Name_of_material' from destributed_suppliers") is None:
                name_of_product = input('Введите название материала(оборудования): ')
                company_name = input('Введите название компании: ')
                amount = int(input('Введите кол-во материалов(оборудования): '))
                price_cost = int(input('Введиете цену материала(оборудования): '))
                price_order = int(input('Введиете цену доставки материала(оборудования): '))
                opt_discounts = int(input('Введите процент оптовых скидок: '))
                type_of_order = input('Введите тип заказа(материал/оборудование): ')
                if (min_value_Price < price_cost + price_order < max_value_Price and
                        min_value_Benefit < opt_discounts < max_value_Benefit):
                    cursor.execute(f"""Insert into destributed_suppliers
                                Values('{name_of_product}', '{company_name}', {price_cost + price_order},
                                {amount}, {opt_discounts}, '{type_of_order}')""")
                    connection.commit()
            else:
                break
        cursor.execute('select * from destributed_suppliers')
        records = cursor.fetchall()
        print('База знаний из бд:', records)
    # если ошибка в запросе
    except(Exception, Error) as er:
        print("Ошибка при работе с PostgreSQL", er)
    # всегда отрабатывает при открытии соединения с базой
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
