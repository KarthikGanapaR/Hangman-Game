import random
from hangman_art import stages,logo
from hangman_words import list

word = random.choice(list)

end = False
lives = 6


display =[]
for _ in word:
  display += "_"

print(logo)
while not end :
  guess = input("Guess a letter ").lower()
  if guess in display:
    print(f"You have already guessed {guess}")
  
  for position in range(len(word)):
    letter = word[position]
    if letter == guess:
      display[position] = letter
    
  if guess not in word:
    print(f"You guessed {guess}, That's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end = True
      print("You lose...")
      print(f"Actuall word is {word}...")
    
  print(f"{' '.join(display)}")
  if "_" not in display:
    end = True
    print("You Win!!!!")

  print(stages[lives])




























































#Created by Karthik Ganapa R