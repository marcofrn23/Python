# Project for lesson 1 in 'Design of Computer Program' course
# by Peter Norvig
# Poker.py coded by Marco Fringuelli

# Topics:
# - How to write function
# - Sets and tuples
# - How to test code
# - Key arguments
# - Intro to list comprehensions
import random

def dealer(numhands, n = 5, deck = [rank+suit for rank in '23456789TJQKA' for suit in 'SHDC']):
    "Function to start playing poker, giving n cards to all the numhands players"
    assert numhands*n <= len(deck), 'Deck is too small!'
    random.shuffle(deck)
    poker, hand = [],[]
    for x in range(numhands):
        hand = []
        for y in range(n):
            hand.append(deck.pop())
        poker.append(hand)
    return poker

def poker(hands):
    "Returns a list of winning hands"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Returns a list of the items with the highest key-value in iterable"
    res, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if xval > maxval:
            maxval = xval
            res = [x]
        elif xval == maxval:
            res.append(x)
    return res


def hand_rank(hand):
    "Return a value indicating the ranking of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "Returns a list with the ranks of the cards, handling the characters TJQKA correctly"
    ranks = ['__23456789TJQKA'.index(rank) for rank,suit in hand]
    ranks.sort(reverse = True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def flush(hand):
    "Determines whether a hand is a flush"
    suits = [suit for rank,suit in hand]
    return len(set(suits)) == 1

def straight(ranks):
    "Determines whether a hand (considering its ranks) is a straight"
    return len(set(ranks)) == 5 and max(ranks)-min(ranks) == 4

def kind(n, ranks):
    "Returns the first rank that is exactly n-of-a-kind in the hand"
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None

def two_pair(ranks):
    "Determines whether a hand contains two pairs"
    pair = kind(2,ranks)
    lowpair = kind(2, list(reversed(ranks)))
    return (pair, lowpair) if pair and lowpair != pair else None

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # STRAIGHT FLUSH
    fk = "9D 9H 9S 9C 7D".split() # FOUR-OF-A-KIND
    fh = "TD TC TH 7C 7D".split() # FULL HOUSE
    tp = "5S 5D 9H 9C 6S".split() # TWO PAIRS
    fs = "7C 2C JC QC 8C".split() # FLUSH
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert straight(card_ranks(sf))
    assert two_pair(card_ranks(tp))
    assert flush(fs)
    assert poker([sf,fk,fh,tp,fs]) == sf
    assert poker([fh,tp,fs]) == fh
    return 'tests pass'

#MAIN
players, r = dealer(input('Quanti giocatori?')), None
print 'Mani: ', players
for hand in players:
    r = hand_rank(hand)
    print r
print 'Vince la mano: ', poker(players)
