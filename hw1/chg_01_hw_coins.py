import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """Подбрасывание монетки"""
        self.side = random.randint(0, 1)


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

n = int(input("Enter qty of coins: "))
coin_list = []

heads = tails = 0

for cont in range(n):
    coin_list.append(Coin())


for coin in coin_list:
    coin.flip()
    if coin.side == 0:
        heads += 1
    else:
        tails += 1

print(f"Орел: {heads/n:.1%}")
print(f"Решка:  {tails/n:.1%}")
