import random

def guess_the_number():

     number_to_guess = random.randint(1,20)
     attempt=0

     print("guess the number between 1 to 20")

     while True:
      guess=int(input("enter your guess:"))
      attempt+=1
    
      if guess < number_to_guess:
        print("no is too low try again.")
    
      elif guess > number_to_guess:
        print("no is too high try agian.")
        
      else:
        print(f"Congratulations! you have guess the number in {attempt} attempts.")  
    
      break 

guess_the_number()
   
              