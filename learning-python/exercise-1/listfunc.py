lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers)
friends.append("Creed") # allows u to append another item onto the list
print(friends)
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)

print(friends.count("Jim"))
print(friends.sort())