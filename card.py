import random

class Card:
    """
    The Card class represents a single playing card and is initiated by passing a suit and a number.
    """
    def __init__(self, suit, number):
        """
        Initialize the Card instance by providing a suit string and number string
        """
        self._suit = suit
        self._number = number

    def __repr__(self):
        """
        Return a string representation of the Card instance
        """
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """ Gets or sets the string suit of the Card. """
        return self._suit

    @suit.setter
    def suit(self, suit):
        # There is not need for a docstring on a setter
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """ Gets or sets the string number of the Card. """
        return self._number

    @number.setter
    def number(self, number):
        # There is not need for a docstring on a setter
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The Deck class represents a deck in order.
    """
    def __init__(self):
        """
        Initialize the Deck array of Cards and populate it.
        """
        self._cards = []
        self.populate()

    def populate(self):
        """
        Populate the Deck array of Cards in order.
        """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """ Reorder the Deck of cards randomly """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """ Deal a number of cards, by removing them from the Deck and returning them as an array. """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """ Return a string representation of the number of cards remaining in the Deck. """
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)
