# manage and organise large amounts of data in py through the use of lists

friends = ["Kevin", "Karen", "Vivian", "Oscar", "Allie", "Toby", "Brandon"] # Keving has index of 0, Karen index of 1 Vivian has index of 2... so on.
print(friends[0]) # indexes from start of the list
print(friends[-1]) # indexes from back of list

print(friends[1:3]) # will grab all names from karen to vivian, specify ranges
# can change the index position as well, useful when modifying values inside arrays
friends[1] = "Vivian"
print(friends[1:3])

#exercises for practise