# This is the unit test of the classes Card and Deck in the file deck.py.
import unittest
from deck import Card, Deck

class DeckTests(unittest.TestCase):

    def setUp(self):
        self.d1 = Deck()

    def test_card(self):
        """An instance of card is correctly created."""
        c1 = Card('6', 'Hearts')
        self.assertEqual(c1.value, '6')
        self.assertEqual(c1.suit, 'Hearts')

        c2 = Card('Q', 'Diamonds')
        self.assertEqual(str(c2), 'Q of Diamonds')

    def test_count(self):
        """The count method works correctly."""
        self.assertEqual(self.d1.count(), 52, 'Full deck = 52 cards.')
        self.d1.deal_card()
        self.assertEqual(self.d1.count(), 51, '51 cards should be remaining.')

    def test_deal_card(self):
        """Deal card method works correctly."""
        c1 = self.d1.deal_card()
        self.assertNotIn(c1, self.d1.cards,
                        'Dealt card is no longer in the deck.')
        self.assertEqual(self.d1.count(), 51, '51 cards should be remaining.')

    def test_shuffle(self):
        """The shuffle method works correctly."""
        orig_deck = [card for card in self.d1]
        shuffled_deck = self.d1.shuffle()
        self.assertNotEqual(orig_deck, shuffled_deck,
            'The shuffled deck must be different from the non-shuffled deck.')
        self.assertEqual(set(orig_deck), set(shuffled_deck),
            'The shuffled and non-shuffled decks must contain the same cards.')
        self.d1.deal_card()
        with self.assertRaises(ValueError):
            self.d1.shuffle()
            #'Trying to shuffle an incomplete deck must raise an exception.'

    def test_deal_hand(self):
        """The deal_hand() method works correctly"""
        self.d1.shuffle()
        self.assertEqual(self.d1.count(), 52, 'A full deck must be 52 cards')
        a_hand = self.d1.deal_hand(num_of_cards=5)
        self.assertEqual(len(a_hand), 5, 'Must have dealt 5 cards.')
        self.assertEqual(self.d1.count(), 47,
                        '47 cards remaining in the deck.')
        self.assertNotIn(a_hand, self.d1.cards,
                        'The dealt cards must be missing from the deck.')

if __name__ == '__main__':
    unittest.main()
