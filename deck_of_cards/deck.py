# Take advantage of OOP in modelling a deck of cards. Make it possible to
# shuffle a deck, to deal a single card from the deck and to deal a hand
# of five cards from the deck.

from random import shuffle as official_shuffle


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):
        self.cards = [Card(val, sui)
                      for sui in Deck.suits for val in Deck.values]
        self.count = len(self.cards)

    def __repr__(self):
        # return f"Deck of {self.count} cards"
        return "Deck of {} cards".format(self.count)

    def shuffle(self):
        if self.count != 52:
            raise ValueError('Only full decks can be shuffled.')
        else:
            official_shuffle(self.cards)
        return self.cards

    def _deal(self, num):
        i = 0
        card_list = []
        while i < num and self.count > 0:
            card_list.append(self.cards.pop())
            i += 1
            self.count = len(self.cards)
        if self.count == 0 and i < num:
            raise ValueError('All cards have been dealt.')
        return card_list

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num_of_cards):
        return self._deal(num_of_cards)

    def display_deck(self):
        i = 1
        print()
        print(f'The following {self.count} cards are remaining in the deck:\n')
        for crd in self.cards:
            if i % 5 == 0:
                print(crd)
            else:
                print(crd, end=', ')
            i += 1
        print('\n')


# Testing
# c1 = Card('A','Hearts')
# print(c1)
d1 = Deck()
# d1.display_deck()
d1.shuffle()
d1.display_deck()
print('Dealt: ', d1.deal_card())  # Deal the last card of the deck
d1.display_deck()
print('Dealt a hand: ', d1.deal_hand(5))  # Deal 5 last cards of the deck
d1.display_deck()
# d1.shuffle() # Shuffling an incomplete deck of cards should raise an error.
