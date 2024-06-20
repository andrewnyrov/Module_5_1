# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print(f'Привет, у меня сегодня день рождения. Мне теперь {self.age}')
#
#
# den = Human('Денис', 22)
# max = Human('Макс', 23)
# den.say_info()
# max.say_info()
# den.birthday()
# max.birthday()

"""
Задача "Developer - не только разработчик":

Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), 
на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку 
"Такого этажа не существует".

Пункты задачи:
Создайте класс House.
Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте 
им переданные значения.

Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания 
задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.

Пример результата выполнения программы:
Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
Вывод на консоль:
1
2
3
4
5
"Такого этажа не существует"

Примечания:
self - это переменная указывающая на объект. Используйте её для обращения к атрибутам
или методам объекта.
Обращение к атрибутам или методам объекта/класса происходит при помощи "."
Метод __init__ вызывается в момент создания объекта.
"""

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, self.number_of_floors + 1):

            if 1 <= i <= new_floor:
                print(i)
            else:
                continue
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик', 3)

print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
h1.go_to(7)
h2.go_to(0)