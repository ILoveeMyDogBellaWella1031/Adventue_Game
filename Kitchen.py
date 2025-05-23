# Kitchen
from simple_colors import *
class Colors:
   BOLD = '\033[1m'
   ITALIC = '\033[3m'




def print_kitchen_nav():
   print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWhere would you like to look first?"
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold'))
   print(Colors.BOLD + " 1. Counter top \n 2. Sink \n 3. Top cupboard \n 4. Fridge \n")
   user_choice = input(yellow("Enter your choice... ", 'bold'))
   return user_choice


def Kitchen_room(character):
   print("As you stand in the center of the cabin, the faint glow of sunlight slipping through the curtains, you take "
         "in your surroundings. \nThe kitchen lies to your left, the living room to your right, and ahead of you stand "
         "three doors, each beckoning in its own strange way.")
   input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
             "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))




   print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\t\tKitchen\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
             "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold' ))
   print(Colors.BOLD + "\nYou step into the kitchen, the faint creak of the floorboards beneath you breaking the "
                       "oppressive stillness. "
         "The counter tops \nare spotless, yet they seem unnervingly sterile, as though no one has ever used them. "
         "The fridge door hangs slightly ajar, \na soft dripping sound emanating from within. On the counter, a loaf "
         "of bread sits half-sliced next to a dull knife, \nas if someone abandoned their task mid-action. A faint smell "
         "of salt lingers in the air, mixed with something metallic, \nbut you can’t pinpoint its source. The eerie quiet "
         "presses against your ears, making you wonder if you really are alone")
   # Starts Kitchen
   all_rooms = 0
   while all_rooms < 4:
       kitchen_nav_choice = print_kitchen_nav()
       if kitchen_nav_choice.lower() == '1':
           print("\nYou look on the counter top. It looks untouched, except for the half sliced loaf of bread. Next to "
                 "it is a dull knife. \nUpon closer inspection, the knife has strange symbols and a faint line that "
                 "looks to be in the shape of a key etched into it but what could it be used for? ")
           print(Colors.ITALIC + (red("\nYou’ve collected:A Dull Knife out of curiosity")))
           character.add_to_inventory("A Dull Knife")


           input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                 "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1




       elif kitchen_nav_choice == '2':
           print("\n\nThe sink is filed with murky water, the surface rippling even though nothing seems to disturb it. Would you like to reach in? \n 1. Yes \n 2. No\n")
           user_choice = int(input(yellow("Enter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(Colors.ITALIC + (red("\nYou’ve collected: A Gold Coin")))
               character.add_to_inventory ("A Gold Coin")
           elif user_choice == 2:
               print("\nI mean, im not shocked, who would stick their hands in that water? You nor i know whats in it, however you might regret that later...")
           input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
             "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1


       elif kitchen_nav_choice == '3':
           print("\n\nA cupboard on the far wall catches your attention. You reach up to grab it, its handle is slightly "
                 "warm to the touch, \nyou open it and you see a few cans of food, canned peas, canned corn, some sardines, would you like to take them? \n 1. Yes \n 2. No")
           user_choice = int(input(yellow("\nEnter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(Colors.ITALIC + (red("\nYou’ve acquired: Canned food x4")))
               character.add_to_inventory("canned food x4")
           elif user_choice == 2:
               print("\nOkay so no food? you might need it but oh well, lets move on")
           input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                 "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1




       elif kitchen_nav_choice == '4':
           print("\n\nYou hesitantly open the fridge door wider. Inside, the dripping seems to echo out to you but "
                 "where is it coming from? \nInstead of food there’s a box on the top shelf. Would you like to take a look? \n 1. Yes \n 2. No")
           user_choice = int(input(yellow("\nType your choice... ", 'bold')))
           if user_choice == 1:
               print("\nYou take the box out, it’s room temperature, along with the rest of the fridge. Inside of the"
                     " box you find a \nphotograph of a place you don’t recognize but from the looks of it, \nit "
                     "seems to be of a lagoon. It looks creepy to you, it has this eerily familiar but haunting \n feeling to it, like you cat look away from it")
               print(Colors.ITALIC + (red("\nYou’ve acquired: Photo")))
               character.add_to_inventory("Photo")
           elif user_choice == 2:
               print("\nYou immediately close the fridge, you get this weird feeling from it all and believe \nits best to leave it there but was that really the best option?")
           all_rooms += 1
