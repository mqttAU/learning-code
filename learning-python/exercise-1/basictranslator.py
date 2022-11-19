# take in a string, and will be able to translate it into a different language

#this language will convert all vowels into a g: a e i o u

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation


# print(translate(input("Enter a phrase: ")))

# make it a bit more efficient

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))