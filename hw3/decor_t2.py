"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 72 рубля) или в евро (курс: 1€ = 80 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
"""
import random

USD = chr(36)
EU = chr(8364)
RUB = chr(8381)
cur = ""
cur_value = 0
def decor(func):
    def wraper(*args, **kwargs):
        result = float(func(*args,**kwargs).strip(RUB))
        random_cur = random.randint(0, 1)
        if(random_cur ==0):
            cur = USD
            cur_value = 72
        else:
            cur = EU
            cur_value = 80
        return f"{str(round(result / cur_value,2)) + cur}"
    return wraper

# def wraper(args):
#     result = float(args.strip(RUB))
#     print(f"{result * 70}{chr(36)}")
#     random_cur = random.randint(0,1)
#     print(random_cur)

# wraper("2₽")

@decor
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'


print(summa(35.5, 2.4))
