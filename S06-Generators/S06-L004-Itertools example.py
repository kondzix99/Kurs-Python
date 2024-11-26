import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

i=0

#4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities
for note in it.permutations(notes,4):
    i += 1
    print(note)

print("Kombinacji bez powtorzen jest: {}".format(i))

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))

#4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities
j = 0

for note1 in it.product(notes,repeat = 4):
    j += 1
    print(note1)

print("Kombinacji z powtorzeniami jest: {}".format(j))

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))