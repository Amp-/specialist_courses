"""
class Money

Напишите класс для работы с денежными суммами.

Реализовать:
*   сложение
*   вычитание
*   умножение на целое число
*   сравнение (больше, меньше, равно, не равно)

==========================================================================================
from functools import total_ordering
Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
__lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

    @total_ordering
    class Student:

        def __eq__(self, other):
            return self.last_name == other.last_name

        def __lt__(self, other):
            return self.last_name < other.last_name

=========================================================================================

При всех операциях, сумма должна преобразовываться к сумме с минимальным количеством копеек.

Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 5коп



Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Дополнительные задания **

Добавьте операцию - вычисление процента от суммы. %

Пример:

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money1 % 21

print(percent_sum)  # 4руб 33коп

__mod__()
Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
После вычисления процента, используем округление (функция round())


### Конвертация валют

Доработайте класс Money, добавив ему метод .convert(), для конвертации суммы в рублях в евро и доллары(*любую валюту).
Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js

#### Отправка запроса на url-адрес

pip install requests
py -m pip install requests
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

, где url - адрес сайта, на который отправляете запрос.

В переменную response получите ответ сайта.

Для преобразования ответа из json-формата используйте функцию:

import json
data_dict = json.loads(response.text)

Модуля json

print(data_dict['Valute']['EUR']['Value'])
"""

from __future__ import annotations
from functools import total_ordering
import requests


url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
val_data = response.json()

@total_ordering
class Money():
    def __init__(self,rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        return f'{self.rub + self.kop // 100}.{self.kop %100}'

    def __add__(self, other):
        rub_sum = self.rub + other.rub + (self.kop + other.kop) // 100
        kop_sum = (self.kop + other.kop) % 100
        return Money(rub_sum, kop_sum)

    def __mul__(self, num):
        res = round(self.rub *100 + self.kop)*num
        return Money(res //100, res %100)

    def __mod__(self, numb):
        p = round(numb * (self.rub + self.kop) / 100)
        return Money(p // 100, p % 100)

    def __eq__(self, other: Money):
        return self.rub * 100 + self.kop == other.rub *100 + other.kop

    def __lt__(self, other):
        return self.rub * 100 + self.kop < other.rub * 100 + other.kop

    def convert(self,val_name):
        price = val_data['Valute'][val_name]['Value']
        nominal = val_data['Valute'][val_name]['Nominal']
        val_conv = nominal * (self.rub + self.kop/100)/price
        return round(val_conv,3)



# money_1 = Money(20, 45)
# print(money_1)


money_1 = Money(100,0)
money_2 = Money(15, 25)

print(f"money_1: {money_1}")
print(f"money_2: {money_2}")

money_3 = money_1 + money_2
print(f"money_3: {money_3}")

money_4 = money_3 % 10
print(f"money_4: {money_4}")

money_5 = money_1 * 3
print(f"money_5: {money_5}")

percent = money_1 % 20
print(percent)

print(money_1.convert("BYN"), "🐇")



# if(money_1 > money_4):
#     print(f"{money_1} > {money_4}")
# else:
#     print(False)
#
# if (money_2 == money_4):
#     print(f"{money_2} == {money_4}")
# else:
#     print(False)
print(money_1 > money_4)
print(money_2 == money_4)
print(money_1 < money_4)
print(money_1 >= money_4)
print(money_1 <= money_4)
