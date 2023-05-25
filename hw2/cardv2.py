import random,pprint
# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def __str__(self):
        return self.value + SUITS_UNI[self.suit]

    def equal_suit(self, other_card):
        if(self.suit == other_card.suit):
            return True
        return False

    def __gt__(self, other):
        if VALUES.index(self.value) == VALUES.index(other.value):
            return SUITS.index(self.suit) > SUITS.index(other.suit)
        return VALUES.index(self.value) > VALUES.index(other.value)


    def __lt__(self, other):
            if VALUES.index(self.value) == VALUES.index(other.value):
                return SUITS.index(self.suit) < SUITS.index(other.suit)
            return VALUES.index(self.value) < VALUES.index(other.value)


class Deck():
    def __init__(self):
        self.cards = [Card(value,suit) for suit in SUITS for value in VALUES]

    def __str__(self):
        return f"Deck[{len(self.cards)}]{','.join([str(card) for card in self.cards])}"

    def draw(self,x=10):
        result = self.cards[:x]
        self.card=self.cards[x:]
        return result

    def shuffle(self):
        random.shuffle(self.cards)


    def __getitem__(self, item):
        return self.cards[item]

# # Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1)
print(card2)

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1} и {card2} одинаковые масти")
else:
    print(f"У карт: {card1} и {card2} разные масти")

deck = Deck()
print(deck)

for card in deck:
    print(card, end=" ")

print(deck[6])
