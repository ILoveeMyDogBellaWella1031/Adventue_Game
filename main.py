import person as ch
import rooms as r
import Kitchen as k
import LivingRoom as l
from simple_colors import *
class Colors:
   BOLD = '\033[1m'
   ITALIC = '\033[3m'


def print_nav():
   user_first_choice = int(input(cyan("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\tWhere would you like to"
                  " go first hehehe~?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\n 1. The "
                  "Kitchen\n 2. The Living Room\n 3. The 'Three' Rooms *UnderConstruction*\n 4. Exit\n Whats your choice young soul? ", 'bold')))
   return user_first_choice


def start_game ():
   print(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWelcome to Dying Path *DEMO GAMEPLAY*\t\t\t\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 'bold'))
   print(f"{ch.Character.name}, wakes up in a mysterious cabin in the middle of the woods. The sun is barely shining "
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
