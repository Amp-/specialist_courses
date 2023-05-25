"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров"
в результате поездки потратится бензин и увеличится пробег
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""


class Car():
    def __init__(self,gas,capacity,gas_per_km,milage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.milage = milage

    def fill(self,add):
        total = add + self.gas
        if total > self.capacity:
            more_max = total - self.capacity
            self.gas = self.capacity
            print(f"Максимальный объем бака {self.capacity} лишние {more_max}")

        else:
            self.gas += add

    def ride(self,distance):
        lit = (distance*self.gas_per_km)/100
        print(f'{lit} потрачено литров')
        d_max = (self.gas *100)/self.gas_per_km
        if (distance > d_max):
            distance = d_max
            self.milage += distance
            self.gas = 0
        else:
            self.gas -= lit
            self.milage += distance
        # print(round(d))


    def get_info(self):
        print(f"В баке {self.gas} литр , вместимость бака {self.capacity},"
              f" рассход составляет: {self.gas_per_km} литров на 100 км. Пробег автомобиля {self.milage}")



car = Car(39,40,10,22000)
car.get_info()
car.fill(2)
car.get_info()
car.ride(100)
car.get_info()