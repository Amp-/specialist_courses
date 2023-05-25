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
            # if VALUES.index(self.value) == VALUES.index(other.value):
            #     return SUITS.index(self.suit) < SUITS.index(other.suit)
            # return VALUES.index(self.value) < VALUES.index(other.value)
        return not self > other


class Deck():
    def __init__(self):
        self.cards = [Card(value,suit) for suit in SUITS for value in VALUES]

    def __str__(self):
        return f"Deck[{len(self.cards)}]{','.join([str(card) for card in self.cards])}"

    def draw(self,x):
        result = self.cards[:x]
        self.cards=self.cards[x:]
        return result

    def shuffle(self):
        random.shuffle(self.cards)


    def __getitem__(self, item):
        return self.cards[item]

class Hand:
    def __init__(self, name, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
        self.lead = None
        self.name = name

    def first_action(self):
        out_card = min(self.cards)
        self.cards.remove(out_card)
        print(f"Игрок {self.name} положил карту {out_card}")
        return out_card

    def second_action(self,out_card):
        a = []
        for card in self.cards:
            if card.suit == out_card.suit and card > out_card:
                a.append(card)
        if len(a):
            best_card = min(a)
            self.cards.remove(best_card)
            print(f"{self.name} отбился картой {best_card}")
            return best_card
        else:
            self.cards.append(out_card)
            print(f"Игрок не смог отбиться и забарал карту себе")

    def third_action(self, table) -> Card | None:
        a = []
        for x in self.cards:
            for y in table.cards:
                if x.value == y.value:
                    a.append(x)
        add = random.choice([0,1])
        if len(a) and add:
            best_card = min(a)
            self.cards.remove(best_card)
            table.cards.append(best_card)
            print(f"Игрок подкинул {best_card}")
            return best_card
        else:
            print("Бито")

    def change_lead(self):
        self.lead ^=1

    def take_card(self):
        if len(self.card) < 10:
            self.card.extend(deck.draw(10 - len(self.card)))

    def __str__(self):
        return f"{','.join(str(card) for card in self.cards)}"

deck = Deck()
deck.shuffle()
print(deck)


hand1= Hand(name="Игрок 1", cards=deck.draw(10))
print(f"{hand1 = !s}")
hand2= Hand(name="Игрок 2", cards=deck.draw(10))
print(f"{hand2 = !s}")

hand1.lead = 1
hand2.lead = 0

table = Hand("table")
table_card1 = hand1.first_action()
table.cards.append(table_card1)

table_card2 = hand2.second_action(table_card1)

if table_card2 is not None:
    table.cards.append(table_card2)
    table_card3 = hand1.third_action(table)
    if table_card3 is not None:
        table_card4 =hand2.second_action(table_card3)
        if table_card4 is not None:
            table.cards.append(table_card4)
            hand1.change_lead(hand2)
            print("Переход права хода")

table.cards = []

