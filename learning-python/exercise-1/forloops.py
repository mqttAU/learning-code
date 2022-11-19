#forloops allow you to loop over different collections of items.
#e.g. loop through different arrays, or letters inside of a string/series of numbers

#e.g. of for loops

friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])
    
    
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")
    
