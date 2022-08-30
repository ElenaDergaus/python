# coding : utf-8
# lesson 8 exercise 4,5,6

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


import random


class Storage:

    """Класс Storage содержит данные о всех поступивших на склад единицах офисной техники и подразделении,
    в которое была передана техника.
    Имеет следующие методы:
    - get_item - метод добавляет единицу техники в основную теблицу equipment_main
    - send_item - метод меняет в основной таблице данные о местоположении единицы техники
     """

    total_items_count = 0 #количество единиц техники находящееся на складе
    equipment_main = [] # основная таблица, содержащая информацию о каждой единице техники, поступающей на склад.
    #Заполняется при вызове метода get_item, который добавляет словарь с данными о конкретной еднице техники.
    location_list = ['офис', 'бухгалтерия', 'канцелярия', 'дирекция'] # подразделения, куда может быть направлена техника


    def get_item(self, item):
        """Метод добавляет единицу техники в сводную таблицу и присваевает ей инвентарный номер """

        equipment_dict = dict(
            [('type', None), ('firm', None), ('cost', None), ('inventory number', None), ('location', None)])

        self.total_items_count += 1

        equipment_dict['type'] = item.type
        equipment_dict['firm'] = item.firm
        equipment_dict['cost'] = item.cost
        equipment_dict['inventory number'] = random.randint(100, 999)
        equipment_dict['location'] = 'на складе'
        self.equipment_main.append(equipment_dict)

        item.inv_number = equipment_dict['inventory number']

    def send_item(self, item, location):
        """Метод отмечает в основной теблице, в какое подразделение была передана данная единица техники
        и осуществляет контроль данных  """

        flag = 0 # Флаг для проверки наличия экземпляра техники на складе

        #Проверка указанного подразделения
        if not location in Storage.location_list:
            print('Нет такого подразделения! \n')
            flag = 1
        else:
            for i in self.equipment_main:
                #Если указанное пользователем подразделение существует, осуществляется поиск по словарям
                # инвентарного номера единицы техники, устанавливается новое место прибывания и выставляется флаг, что  такая единица техники на складе обнаружена

                if i['inventory number'] == item.inv_number:
                    if i['location'] != 'на складе':
                        print(f'{i["type"]}, инвентарный номер {i["inventory number"]} уже отдан в:  {i["location"]}.\n')
                        flag = 1
                    else:
                        i['location'] = location
                        flag = 1
                        self.total_items_count -= 1

        # Если единицы техники на складе нет, флаг остается нулевым и выводится сообщение пользователю
        if flag == 0:
            print("Данная единица не числиться на складе!\n")


class OfficeEquipment:

    """Класс OfficeEquipment описывает основные параметры любой единицы офисной техники
     и осуществляет проверку корректности вводимых пользователем данных при создании экземпляра класса: цены единицы техники.
     Если введенные данные не корректны у пользователя есть три попытки ввести корректные данные"""

    inv_number = 0
    _count = 0
    cost = 0
    firm = 'unknown'
    n = 0

    def __init__(self, firm='Philips', cost=1000):
        OfficeEquipment._count += 1
        self.firm = firm
        self.cost = cost
        # Если неверно задана цена программа будет три раза просить ввести корректные данные
        while OfficeEquipment.check(self.cost):
            self.n += 1
            print(f'Неверный тип данных: {self.cost}\n'
                  f'Цена может принисмать только числовое значение.'
                  )
            self.cost = input('Задайте корректные данные: цена товара - ')
            OfficeEquipment.check(self.cost)
            if self.n > 2:
                print("Вы исчерпали все попытки!")
                quit()


    @staticmethod
    def check(cost):
        flag = False
        try:
            float(cost)
        except:
            flag = True
        return flag


class Printer(OfficeEquipment):
    """Создает единицу офисной техники - принтер"""
    def __init__(self, firm, cost, print_type='black'):
        super().__init__(firm, cost)
        self.type = 'Принтер'
        self.print_type = print_type #Индивидуальный параметр - цвет печати


class Scanner(OfficeEquipment):
    """Создает единицу офисной техники - сканер"""
    def __init__(self, firm, cost, scan_resolution='300 dpi'):
        super().__init__(firm, cost)
        self.type = 'Сканер'
        self.scan_resolution = scan_resolution # Индивидуальный параметр - разрешение сканирования



class Xerox(OfficeEquipment):
    """Создает единицу офисной техники  - ксерокс"""
    def __init__(self, firm, cost, color='gray'):
        super().__init__(firm, cost)
        self.type = 'Ксерокс'
        self.color = color #Индивидуальный параметр - цвет ксерокса





# Создадим экземпляры офисной техники
printer1 = Printer('Philips', 700, 'color')
scaner1 = Scanner('Philips', 650)
printer2 = Printer('Epson', 1200, 'color')

# Вывод атрибутов экземпляров
print(OfficeEquipment._count)
print(printer1.print_type)
print(printer1.type)
print(printer1.cost)
print(scaner1.firm)

# Создадим склад
storage1 = Storage()

# Добавим на склад один принтер и сканер
storage1.get_item(printer1)
storage1.get_item(scaner1)

# Посмотрим, что есть на складе
print(storage1.equipment_main)

# Отправим принтер в бухгалтерию
storage1.send_item(printer1, 'бухгалтерия')
print(storage1.equipment_main)


# Попробуем куда-нибудь отправить второй принтер, не сданный на склад
storage1.send_item(printer2, 'офис')

# Попробуем отправить сканер в несуществующее подразделение
storage1.send_item(scaner1, 'библиотека')

# Попробуем отправить куда-нибудь принтер, который уже в бухгалтерии
storage1.send_item(printer1, 'офис')

# Попробуем неправильно ввести стоимость:
xerox1 = Xerox('Xerox', 'sto dollarov')

# Проверим цену у созданной единицы техники:
print(xerox1.cost)