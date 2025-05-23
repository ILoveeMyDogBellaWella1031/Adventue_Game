#Samiyah Sookdar
# November 18th, 2024
# Project: Adventure Game (Dying Path)


# import all files to rooms.py

import person as ch
import Kitchen as k
import LivingRoom as l
import ThreeRooms as r3
from simple_colors import *


class Colors:
   BOLD = '\033[1m'
   ITALIC = '\033[3m'

#Navigation directory

def print_nav():
   user_first_choice = int(input(cyan("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\tWhere would you like to"
                  " go first hehehe~?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\n 1. The "
                  "Kitchen\n 2. The Living Room\n 3. The 'Three' Rooms *UnderConstruction*\n 4. Exit\n Whats your choice young soul? ", 'bold')))
   return user_first_choice

#Introduction

def start_game ():
   print(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWelcome to Dying Path *DEMO GAMEPLAY*\t\t\t\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 'bold'))
   print(f"{ch.Character(username)}, wakes up in a mysterious cabin in the middle of the woods. The sun is barely shining "
         f"through the little creek of \nthe window, curtains are tattered and faded, their edges fraying as if they’ve"
         f" been hanging there for decades, and the \ncabin feels both empty and alive, with shadows flickering across "
         f"the wooden walls. To the left, the kitchen is eerily \npristine, its counter tops gleaming despite the age "
         f"of the cabin, but the living room, however, is shrouded in darkness, \nits furniture draped in dust-covered"
         f" sheets. Three doors stand on the far wall, each unique—one dark brown with the carving \nof a beast, another "
         f"a khaki brown with intricate wave patterns, and the third matching the color of the first but with an \nenigmatic "
         f"craving that pulls at the heart. You look around the room. Whose cabin is this? And why are you here? \nIs there a reason as to why you were put here? Hm...")
   print()


   # Start the game!
if __name__ == '__main__':
   username = input("Welcome young soul, please enter your name :  ")
   start_game()


   mc = ch.Character(username)
   # Start letting user choose room
   all_rooms_solved: int = 0
   while all_rooms_solved < 4:
       # There are 3 different paths and an exit, when all of those rooms are completed itll print the last print statement
       # Print room menu
       user_room_choice = print_nav()
       if user_room_choice == 1:
           k.Kitchen_room(mc)
           all_rooms_solved += 1
       elif user_room_choice == 2:
           l.LivingRoom_room(mc)
           all_rooms_solved += 1
       elif user_room_choice == 3:
           r3.ThreeRooms_room(mc)
           all_rooms_solved += 1
       elif user_room_choice == 4:
           if all_rooms_solved == 4:
               #if all of the rooms are completed and you decide to leave you win but if not itll print the bellow
            print(f"Well done {mc.name}, You've finished with exploring this odd cabin\nand you notice something lies "
                  f"out there in the woods..."
               "it's calling you're\nname. The sirens await will you dare to engage with them? come back nex time for "
                  "the full game. Thank you for playing!")
            #DEMO Version
            quit()
           elif all_rooms_solved < 4 or all_rooms_solved > 1:
               print("\nYou started it you MUST finish... What did you think this was? You cant leave until you finish... ")
               #If you haven't completed all the rooms but youve completed more than one you cant leave

               input(
                   red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))

               user_room_choice = print_nav()




