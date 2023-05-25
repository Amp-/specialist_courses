import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.randint(0,1)

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

n = int(input('Enter qty of coins: '))
coin_list = []
heads = 0
tails = 0
for cont in range(0,n):
    coin_list.append(Coin())

# for coin in coin_list:
#     coin.side = random.randint(0,1)
#     if (coin.side == 0):
#         heads += 1
#     else:
#         tails += 1


for coin in coin_list:
    coin.flip()
    if(coin.side == 0):
        heads += 1
    else:
        tails += 1

print(f'Орел: {heads}')
print(f"Решка:  {tails}")