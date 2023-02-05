import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (2,3,4,5,6,7,8,9,10,11,12,13,14)
class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.rank} of {self.suit}'

class Deck:
  def __init__(self):
    self.all_cards = []

    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(suit, rank))

  def shuffle(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()


class Player:
  def __init__(self, name):
    self.name = name
    self.all_cards = []

  def remove(self, index):
    return self.all_cards.pop(index)

  def add_cards(self, cards):
    self.all_cards.extend(cards)

  def __str__(self):
    return f'Player {self.name} has {len(self.all_cards)} cards'
    