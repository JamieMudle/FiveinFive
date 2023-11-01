import random #import random for later

#Title of game
Title = "Five In Five"

#Define word bank variable as list
word_bank = []

#Get words from text file to put in word bank
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

# Pick random word from word bank

word_to_guess = random.choice(word_bank)

#game variables
misplaced_guesses = []
wrong_guesses = []
max_turns = 5
turns_taken = 0

#Displacy intial game state and welcome to game
print (f"Welcome to {Title}, you have Five turns to guess a Five letter word. Good Luck!")
print("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns left.")

while turns_taken < max_turns:
    #Get the guess
    guess = input("Guess a word: ").lower()

    #Check the guess is 5 letters and is an alpha
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter a Five letter word.")
    else:

#Check each letter against the selected letter
        index = 0
        for c in guess:
            if c == word_to_guess[index]:
                print(c, end=" ")
                if c in misplaced_guesses:
                    misplaced_guesses.remove(c)
            elif c in word_to_guess:
                if c not in misplaced_guesses:
                        misplaced_guesses.append(c)
                print("_", end=" ")
            else:
                if c not in wrong_guesses:
                        wrong_guesses.append(c)
                print("_", end=" ")
            index += 1

    print("\n")
    print(f"Misplaced letters: {misplaced_guesses}")
    print(f"Wrong letters: {wrong_guesses}")
    turns_taken += 1

#Check if winning word
    if guess == word_to_guess:
        print(f"Bloody well done! It took you: {turns_taken} attempts")
        break

    if turns_taken == max_turns:
        print(f"Sorry, you didn't make it! The word was {word_to_guess}")
        break

    turns_remaining = max_turns - turns_taken
    print(f"You have {turns_remaining} turns left.")


