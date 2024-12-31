from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
                Card(rank, suit) 
                for suit in self.suits 
                for rank in self.ranks
                ]

    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self):
        return len(self._cards)


deck = FrenchDeck()

print(f"{len(deck)=}")
print(f"{choice(deck)=}")
print(f"{choice(deck)=}")
print(f"{choice(deck)=}")
print(f"{deck[8:15]=}")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print("\nFrench Deck sorted by value")
for card in sorted(deck, key=spades_high):
    print(card)
