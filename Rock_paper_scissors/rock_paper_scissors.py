import random

# handle input will take the inputted string and return a numerical placeholder
def handle_input(choice):
   if choice == 'rock':
      return 1
   elif choice == 'paper':
      return 2
   elif choice == 'scissors':
      return 3
   else:
      return 0

# output computer choice will tell the user what the computer's choice was
def output_computer_choice(choice):
   if choice == 1:
      print("The computer chose... rock!")
   elif choice == 2:
      print("The computer chose... paper!")
   elif choice == 3:
      print("The computer chose... scissors!")

# check tie will inform the user if they have tied
def check_tie(computer, user):
   if computer == user:
      return True

# check loss will inform the user if they have lost
def check_loss(computer, user):
   if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
      return True

# check win will inform the user if they have won
def check_win(computer, user):
   if (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
      return True


# body of the program
run = True
while (run):
   user_choice = input("Choose rock, paper, or scissors: ")
   num_user_choice = handle_input(user_choice)

   while num_user_choice == 0:
      user_choice = input("Please choose only rock, paper, or scissors: ")
      num_user_choice = handle_input(user_choice)

   num_computer_choice = random.randrange(1,4)

   output_computer_choice(num_computer_choice)

   if check_tie(num_computer_choice, num_user_choice):
      print("It's a tie!")

   if check_loss(num_computer_choice, num_user_choice):
      print("You lost!")

   if check_win(num_computer_choice, num_user_choice):
      print("You won!")

   play_again = input("Input any key to play again, q to quit: ")
   if play_again == 'q':
      run = False