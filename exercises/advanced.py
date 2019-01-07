"""Advanced exercises"""
from collections import namedtuple
import csv

import random


def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    rows = string.split('\n')
    list_of_lists = []
    for row in rows:
        sub_list = row.split()
        sub_list = [int(n) for n in sub_list]
        list_of_lists.append(sub_list)
    return list_of_lists

# Testing
#print(matrix_from_string('1 2 \n 10 20'))

def parse_csv(file_obj):
    """Return namedtuple list representing data from given file object."""
    csv_reader = csv.reader(file_obj)
    Row = namedtuple('Row', next(csv_reader))
    return [Row(*values) for values in csv_reader]

# Testing
#with open('us-state-capitals.csv') as csv_file:
#    csv_rows = parse_csv(csv_file)
#    print(csv_rows[:3])

def get_cards():
    """Create a list of namedtuples representing a deck of playing cards."""
    Card = namedtuple('Card', 'rank suit')
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    full_deck = [Card(suit, rank) for suit in suits for rank in ranks]
    return full_deck

def shuffle_cards(deck):
    """Shuffles a list in-place"""
    random.shuffle(deck)
    return deck

def deal_cards(deck, count=5):
    """Remove the given number of cards from the deck and returns them"""
    hand = deck[-5:] # The last 5 cards of the deck
    deck = deck[:-5]
    return (hand, deck)

# Testing
#deck = get_cards()
#print('Original number of Cards: ', len(deck))
#deck = shuffle_cards(deck)
#hand, deck = deal_cards(deck)
#print(hand)
#print('Final number of Cards: ', len(deck))


