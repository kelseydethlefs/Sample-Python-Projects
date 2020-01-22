#Lab9.py

animal_dict = {}
total = 0
animal = input ("Please enter an animal name or press Return to end program. ")

while animal != '':
    if animal not in animal_dict:
        animal_dict[animal] = 0
    animal_dict[animal] += 1
    total += 1
    animal = input ("Please enter an animal name or press Return to end program. ")

print ('''
Nature Society -- UO 2013 Wild Animal Report

Animal Count''')

for animal in sorted(animal_dict):
    print (animal, animal_dict[animal])

print ("---" * 13)
print ("Total", total)
