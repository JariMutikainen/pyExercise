# This is the unit test of the classes Card and Deck in the file deck.py.
import unittest
from deck import Card, Deck

class DeckTests(unittest.TestCase):

    def setUp(self):
        self.d1 = Deck()

    def test_card(self):
        """Testing the class Card"""
        c1 = Card('6', 'Hearts')
        self.assertEqual(c1.value, '6')
        self.assertEqual(c1.suit, 'Hearts')

        c2 = Card('Q', 'Diamonds')
        self.assertEqual(str(c2), 'Q of Diamonds')

    def test_count(self):
        """Testing the count method"""
        self.assertEqual(self.d1.count(), 52, 'Full deck = 52 cards.')
        self.d1.deal_card()
        self.assertEqual(self.d1.count(), 51, '51 cards should be remaining.')


if __name__ == '__main__':
    unittest.main()
