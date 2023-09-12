print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print('''
#       __
#      /  l
#    .'   :               __.....__..._  ____
#   /  /   \          _.-"        "-.  ""    "-.
#  (`-: .---:    .--.'          _....J.         "-.
#   """y     \,.'    \  __..--""       `+""--.     `.
#     :     .'/    .-"""-. _.            `.   "-.    `._.._
#     ;  _.'.'  .-j       `.               \     "-.   "-._`.
#     :    / .-" :          \  `-.          `-      "-.      \
#      ;  /.'    ;          :;               ."        \      `,
#      :_:/      ::\        ;:     (        /   .-"   .')      ;
#        ;-"      ; "-.    /  ;           .^. .'    .' /    .-"
#       /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'
#      /  /      `,\.  .'   "":'  /-"   .'       \__.'
#     :  :         ,\""       ; .'    .'      .-""
#    _J  ;         ; `.      /.'    _/    \.-"
#   /  "-:        /"--.l-..-'     .'       ;
#  /     /  ""-..'            .--'.-'/  ,  :
# :`.   :     / :             `-i" ,',_:  _ \
# :  \  '._  :__;             .'.-"; ; ; j `.l
#  \  \          "-._         `"  :_/ :_/
#   `.;\             "-._
#     :_"-._             "-.
#       `.  l "-.     )     `.
#         ""^--""^-. :        \
#                   ";         \
#                   :           `._
#                   ; /    \ `._   ""---.
#                  / /   _      `.--.__.'
#                 : :   / ;  :".  \
#                 ; ;  :  :  ;  `. `.
#                /  ;  :   ; :    `. `.
#               /  /:  ;   :  ;     "-'
#              :_.' ;  ;    ; :
#                  /  /     :_l
#                  `-'                                          ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You get to a crossroad, in one direction is a tropical forest that may lead to a hidden treasure,")
choice1 = input(
    "and on the right it's a temple in which you see already a shiny chest. Which direction will you go? Left or Right? "
).lower()
if choice1 != ('left'):
    print("You fall into a hole.Game Over.")
else:
    print(
        "You go into the deep fierce green forest, you're surrounded by wild animals and their menacing sounds at every step, even when you don't see anything, you should keep your step safe..."
    )
    choice2 = input(
        "You come across a river, and further away you see a golden house. Do you swim or wait until a boat comes? "
    ).lower()
    if choice2 != "wait":
        print("You get attacked by trout. Game Over.")
    else:
        choice3 = input(
            "You arrive in front of the Golden House. In front of you there are 3 doors: Red, Yellow and Blue. Which one do you dare open?"
        ).lower()
        if choice3 == ("yellow"):
            print(
                "You win! You find the treasure full of gold and jewels! Good job!"
            )
        elif choice3 == ("blue"):
            print(
                "A three headed dragon greeted you with flames growling from each head. Game over."
            )
        elif choice3 == ("red"):
            print(
                "A gnome threw its pointy hat towards you, you start to see black. Game over."
            )
        else:
            print(
                "Are you giving up that easily on the Golden House? Game over."
            )
