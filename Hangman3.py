a = ''
def updateText(guessed_letters,secretWord):
  display = ""
  for letter in secretWord:
      if letter.lower() in guessed_letters:
          display += letter
      else:
          display += "_"
  print(display)
    
def hangman(secretWord):
  chances = 6
  guessed_letters = []
  while chances > 0:
      guess = input("Guess a letter in my secret word: ")
      if len(guess) != 1:
          print("Please give me one letter.")
      elif not guess.isalpha():
          print("Please give me a letter.")
      elif guess.lower() in guessed_letters:
          print("You already guessed that letter.")
      else:
          guessed_letters.append(guess.lower())
          if guess.lower() in secretWord.lower():
              print("Congrats, you guessed a letter!")
          else:
              chances -= 1
              print("Better luck next time. You have {} chances left.".format(chances))
          updateText(guessed_letters,secretWord)
          if updateText(guessed_letters) == secretWord:
            print("Congratulations! You guessed the word:", secretWord)
            break

secretWord = 'Rahasia'
hangman(secretWord)