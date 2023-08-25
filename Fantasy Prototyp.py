print('''
  ad88                                                                 
  d8"                           ,d                                      
  88                            88                                      
MM88MMM ,adPPYYba, 8b,dPPYba, MM88MMM ,adPPYYba, ,adPPYba, 8b       d8  
  88    ""     `Y8 88P'   `"8a  88    ""     `Y8 I8[    "" `8b     d8'  
  88    ,adPPPPP88 88       88  88    ,adPPPPP88  `"Y8ba,   `8b   d8'   
  88    88,    ,88 88       88  88,   88,    ,88 aa    ]8I   `8b,d8'    
  88    `"8bbdP"Y8 88       88  "Y888 `"8bbdP"Y8 `"YbbdP"'     Y88'     
                                                               d8'      
                                                              d8'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")




