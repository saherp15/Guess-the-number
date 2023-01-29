import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
game=True
while game:
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts=0
  if difficulty=="easy":
    attempts=10
    comp=random.randint(1,101)
    while attempts>0:
      print(f"You have {attempts} attempts remaining to guess the number")
      user=int(input("Make a guess:"))
      if user>comp:
        print("Too high")
        print("Guess again.")
        attempts-=1
        if attempts==0:
          print("You've run out of guesses.You lose!")
          game=False
      elif user<comp:
        print("Too low")
        print("Guess again.")
        attempts-=1
        if attempts==0:
          print("You've run out of guesses.You lose!")
          game=False
      elif comp==user:
        print(f"You got it! The answer was {comp}. You guessed it in {attempts} attempts")
        break
  
  elif difficulty=="hard":
    attempts=5
    comp=random.randint(1,101)
    while attempts>0:
      print(f"You have {attempts} to guess the number")
      user=int(input("Make a guess:"))
      if user>comp:
        print("Too high")
        print("Guess again.")
        attempts-=1
        if attempts==0:
          print("You've run out of guesses.You lose!")
          game=False
          break
      elif user<comp:
        print("Too low")
        print("Guess again.")
        attempts-=1
        if attempts==0:
          game=False
          print("You lose!")
      elif comp==user:
        game=False
        print(f"You got it! The answer was {comp} .You guessed it in {attempts} attempts")
        break
  else:
    game=False
    print("Invalid Input")
    break
    
    