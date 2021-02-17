import random

possible_choices = ['Rock','Paper','Scissors']

# User Selection -- get info from user

user_selection = input('What is your selection? (Rock, Paper, Scissors): ')
#TODO Validate user selection
print ('You chose', user_selection)

# Computer Selection -- find way for computer to select options
# computer_selection = random.choices(possible_choices) # TODO uncomment for production

#TODO remove this temp test
computer_selection = "Paper"

print ('Computer chose', str(computer_selection))

# Evaluate the results -- Conditional statement 
if user_selection == computer_selection:
    print('It is a tie')

#------Rock-----
elif user_selection == 'Rock':
    # computer selects Paper
    if computer_selection == 'Paper':
        print('User loses')
    # computer selects Scissors
    else:
        print('User wins')

#------Paper-----
elif user_selection == 'Paper':
    # computer selects Rock
    if computer_selection == 'Rock':
        print('User wins')
    # computer selects Scissors
    else:
        print ('User loses')
    
      
#------Scissors-----      
elif user_selection == 'Scissors':
    # computer selects Rock
    if computer_selection == 'Rock':
        print ('User loses')
    # computer selects Paper
    else:
        print ('User wins')

# Declare a winner

