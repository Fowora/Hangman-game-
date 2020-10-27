import random
f = open('words.txt')
words=[]
for word in f.read().split():
  words.append(word)

def get_guess():
  
  print("Welcome to HANGMAN! Let's have some fun")
  print("Guess the word:")
  dashes = "-" * len(sec_word)
  guesses_left = 10
  
  #while guesses_left > -1 and dashes != sec_word:
  while guesses_left > -1 and not dashes == sec_word:
  # Prints the amount of dashes and guesses left
    print(dashes)
    print (str(guesses_left)) 
  # Asks the user for input  
    guess = input("Guess:") 
  #Tells the user when he inputs more than one character   
    if len(guess) != 1:
      print ("Your guess must have exactly one character!") 
  #Replaces the dashes with letters at the appropriate index of the correct word    
    elif guess in sec_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(sec_word, dashes, guess) 
  #If the guess is wrong, it displays a message to the user and subtracts one from the number of guesses    
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
  #if the dashes end up being the secret word then You win and the correct word are printed and if it is wrong You lose and the correct word are printed  
  if guesses_left < 0:
    print ("You lose. The word was: " + str(sec_word)) 
  
  else:
    print ("Congrats! You win. The word was: " + str(sec_word))
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  #This function updates dashes and matches it up with the correct word if the user ends up getting it right
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess #Adds the guess to string if guess is correct    
      
    else:
      result = result + cur_dash[i] # Add the dash at index i to result if it doesn't match the guess
      
  return result
    
sec_word = random.choice(words)
get_guess()
