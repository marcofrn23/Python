# Exercise 1 for lesson 2 in 'Design of Computer Program' course

from itertools import permutations

def is_adjacent(p1, p2):
    if abs(p1-p2) == 1:
        return True
    return False

def floor_puzzle():
    """Resolves the given puzzle with the given constraints."""
    residences = list(permutations([1,2,3,4,5], 5))
    # Expressing all the constraints with a generator expression
    return list(next((Hopper, Kay, Liskov, Perlis, Ritchie)
         for (Hopper, Kay, Liskov, Perlis, Ritchie) in residences
         if Hopper is not 5 and
         Kay is not 1 and
         Liskov is not 1 and
         Liskov is not 5 and
         Perlis > Kay and
         not is_adjacent(Ritchie, Liskov) and
         not is_adjacent(Liskov, Kay)))
#MAIN
f = floor_puzzle()
p = ('Hopper', 'Kay', 'Liskov', 'Perlis', 'Ritchie')
res = [person + ' lives in the floor no. ' for person in p]
floors = [str(number) for number in f]
for i in range(5):
    print '\n' + res[i] + floors[i]
print '\n......Puzzle resolved correctly.'
