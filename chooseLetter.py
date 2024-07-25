import random
import os
from hangman_words import *
from hangman_art import *
print(logo)
chosen_word = random.choice(word_list)
list=[]
randomList=[]
print(chosen_word)
wordLen =len(chosen_word)
for i in range(wordLen):
    list += "_"
end_of_game=False
lives =len(stages)-1
temp=0
while not end_of_game:    
    guess = input("guess a letter: ").lower()
    os.system('cls')
    if guess in list:
        print("you have already entered this output")
    for position in range(wordLen):
        letter =chosen_word[position]
        if letter==guess:
            list[position]= letter
    
    if guess not in chosen_word and guess not in list:
        randomList.append(temp)
    if guess not in chosen_word:
        if guess in randomList:
            print(f"you entered wrong letter again! {guess} is not in the chosen letter... Try again...")        
        elif lives==0:
            print(stages[lives])
            print("Game Over!!")
            break
        elif lives!=0 and guess not in randomList:
            print("The entered letter is not in the chosen word")
            # temp=guess
            print(stages[lives])
            lives=lives-1
        temp=guess
    
        
    print(" ".join(list))
    if "_" not in list:
        end_of_game=True
        print("You Won!!")





# Angela's code:
# #Step 5

# import random

# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# from hangman_words import word_list

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo
# print(logo)

# #Testing code
# # print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from hangman_art import stages
#     print(stages[lives])
