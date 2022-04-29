rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
Game_Start=[rock,paper,scissors]
User_Choice= int(input("Enter which symbol you want to perform 0 fo rock,1 for paper and 2 for scissors : "))
print("User_Choice")
print(Game_Start[User_Choice])
print("Computer Choice")
Computer_Choice=random.randint(0,2)
print(Game_Start[Computer_Choice])
if User_Choice==Computer_Choice:
    print("Draw")
elif User_Choice == 0 and Computer_Choice==2:
    print("You won")
elif User_Choice == 2 and Computer_Choice == 0:
    print("You lose")
elif User_Choice > Computer_Choice:
    print("You won")
elif Computer_Choice > User_Choice:
    print("You lose")
else:
    print("You entered a invalid entry")