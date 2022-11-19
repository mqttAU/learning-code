#building basic guessing game in py, using if statements while loops and variables etc.
#specify secret word stored inside program, user can interact with program to guess the word until they get it right.

secret_word = "giraffe" #created secret word variable
guess = "" #guess variable
guess_count = 0 #guess count variable, keeps track how many times user has guessed the word
guess_limit = 3 #how many times the user can guess
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): #specify condition looping code as long as conditions here are true, meaning as long as they have not guessed the word and not out of guesses
    if guess_count < guess_limit: #do they still have guesses left? if they do, otherwise else out of guesses plays out
        guess = input("Enter guess: ") #implementing the guess count
        guess_count += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("You did not guess the secret word within 3 attempts.")
else:
    print("You guessed the secret word!")
    


