# Project 1 for lesson 2 in 'Design of Computer Program' course
# by Peter Norvig
# ZebraPuzzle.py coded by Marco Fringuelli

# Topics:
# - List comprehensions
# - Generator expressions
# - Intro to generator functions
# - Aspect-oriented Programming
# - How to measure execution time for something
# - How to count calls (iterations) of something

# CONSTRAINTS (This is the puzzle the program is going to solve)
# 1 There are five houses.
# 2 The Englishman lives in the red house.
# 3 The Spaniard owns the dog.
# 4 Coffee is drunk in the green house.
# 5 The Ukrainian drinks tea.
# 6 The green house is immediately to the right of the ivory house.
# 7 The Old Gold smoker owns snails.
# 8 Kools are smoked in the yellow house.
# 9 Milk is drunk in the middle house.
# 10 The Norwegian lives in the first house.
# 11 The man who smokes Chesterfields lives in the house next to the man with the fox.
# 12 Kools are smoked in a house next to the house where the horse is kept.
# 13 The Lucky Strike smoker drinks orange juice.
# 14 The Japanese smokes Parliaments.
# 15 The Norwegian lives next to the blue house.
# Who drinks water? Who owns the zebra?

import itertools
import time

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    # The problem is solved using a long generator expression (object type)
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

# MEASURING TIMES
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n ,int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn,*args)[0])
    return min(times), average(times), max(times)

# COUNTING CALLS
# def c(sequence):
#     # Generator function (object type)
#     c.starts += 1
#     for item in sequence:
#         c.items += 1
#         yield item
#
# def instrument_fn(fn, *args):
#     c.starts, c.items = 0,0
#     result = fn(*args)
#     print '%s got %s with %5d iters over %7d items' % (fn.__name__, result, c.starts, c.items)

# MAIN
F = zebra_puzzle
solution = timedcall(F)[1]
print 'It took ',timedcall(F)[0],' to execute the function'
q = input('Time tests?\n')
T = timedcalls
p = []
t = ('Englishman', 'Spaniard', 'Ukranian', 'Japanese', 'Norwegian')
for i in solution:
    p.append(t[i-1])
for elem in p:
    print elem, '\n'
#instrument_fn(F)
tests = T(q,F)
print 'Minimum time: %s \nAverage time: %s \nMaximum time: %s' % (tests[0],tests[1],tests[2])
