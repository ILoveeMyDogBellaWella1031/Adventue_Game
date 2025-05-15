# Jariyah Guy + Samiyah Sookdar
# November 18th, 2024
# Project: Adventure Game (Dying Path)


# User/Main character info.
# Step 2: Would start in a cabin that requires the user to find ways to escape by different rooms
# Step 3: Some of the keys we find aren't the right keys + can't move on in different rooms until we find a matching key to a door (Ex. requires specific color of key to unlock another door)
# Step 4 After, 1 path to a lagoon including sirens/mystical creatures who we can buy/give offerings to work with us or could be a threat) *Jariyah's focus*)
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
   all_rooms_solved = 0
   while all_rooms_solved < 4:
       # Print room menu
       user_room_choice = print_nav()
       if user_room_choice == 1:
           k.Kitchen_room(mc)
           all_rooms_solved += 1
       elif user_room_choice == 2:
           l.LivingRoom_room(mc)
       elif user_room_choice == 4:
           print(f"Well done {mc.name}, You've finished with exploring this odd cabin\nand you notice something lies out there in the woods..."
               "it's calling you're\nname. The sirens await will you dare to engage with them? come back nex time for yhe full game. Thank you for playing!")
           quit()




#Introduction


def print_kitchen_nav():
   print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWhere would you like to look first?"
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold'))
   print(Colors.BOLD + " 1. Counter top \n 2. Sink \n 3. Top cupboard \n 4. Fridge \n")
   user_choice = input(yellow("Enter your choice... ", 'bold'))
   return user_choice


def Kitchen_room(character):
   print("As you stand in the center of the cabin, the faint glow of sunlight slipping through the curtains, you take in your surroundings. \nThe kitchen lies to your left, the living room to your right, and ahead of you stand three doors, each beckoning in its own strange way.")
   input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
             "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))




   print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\t\tKitchen\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
             "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold' ))
   print(Colors.BOLD + "\nYou step into the kitchen, the faint creak of the floorboards beneath you breaking the oppressive stillness. "
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
                 "it is a dull knife. \nUpon closer inspection, the knife has strange symbols and a faint line that looks to be in the shape of a key etched into it but what could it be used for? ")
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


#LivingRoom


def print_LR_nav():
   print(magenta("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWhere would you like to look now?"
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold'))
   print(Colors.BOLD + " 1. BookShelf \n 2. Under the sheets of the couch \n 3. Under the Rug \n 4. In the cushions \n")
   user_choice = input(magenta("Enter your choice... ", 'bold'))
   return user_choice
# Importance of character to apply things in inventory




def LivingRoom_room(character):
   print("The living room feels heavier as you step inside, the air colder than the rest of the cabin. Dust coats "
             "everything, dulling the once-vibrant colors \nof the furniture. Sheets drape over misshapen forms—furniture, "
             "perhaps, but their outlines suggest something \nmore. A fireplace sits against the far wall, it embers glowing faintly despite no visible.")


   # if user_first_choice == 2:
   all_rooms = 0
   while all_rooms < 4:
       living_room_nav_choice = print_LR_nav()
       if living_room_nav_choice == '1':
           print("\nYou look at the bookshelf and you find a leather book. The journal is worn out,its dark brown cover "
                 "cracked and weathered with age. A tarnished clasp \nholds it shut, but the lock appears broken. "
                 "Inside, the yellowed pages are filled with cryptic handwriting and sketches of symbols you don’t "
                 "recognize—some \nresembling the carvings on the cabin’s doors. Smudges and stains suggest it’s been"
                 " handled with urgency or fear. Several pages are torn out, leaving jagged \nedges and an unsettling "
                 "sense of incompleteness. The faint scent of old ink clings to it, as if the thoughts recorded within are still alive."
                 "\nWould you like to take it? \n 1. Yes \n 2. No\n")


           user_choice = int(input(yellow("Enter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(Colors.ITALIC + (red("\nYou’ve acquired: A Journal")))
               character.add_to_inventory("A Leather-Bound Journal")


           elif user_choice == 2:
               print("\nAre you SLOW?? pun intended, anyways you cant take that back and you might regret that later...")


           input(
               red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1


       elif living_room_nav_choice == '2':
           print("You look under the sheets, As you lift the sheet, a cloud of dust billows \ninto the air, making you "
                 "cough. Beneath it is a couch with deep claw marks etched into the \nfabric, as though something feral"
                 " had been here. The cushions are sunken in odd shapes, \nand one corner is darkened with a stain that"
                 " looks suspiciously fresh. The air around it feels colder\n, and the faint impression of a hand lingers "
                 "on the armrest, though no one \nhas been here for a long time.\n\n There's a key! The key is small, "
                 "delicate, and made of a strange \nmetal that seems to shimmer faintly in the dim light. Its head is "
                 "shaped like a \nflower, with intricate vines etched into its surface. Holding it, you feel an odd "
                 "\nwarmth, as though it’s been waiting for someone to use it. The grooves \nare too unique to fit an "
                 "ordinary lock—it’s clear this key has a very specific purpose. \nAs you hold it, a faint, distant "
                 "melody seems to echo in your ears, almost pulling you toward something unseen. \nWould you like to take it? \n 1. Yes \n 2. No\n")


           user_choice = int(input(yellow("Enter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(Colors.ITALIC + (red("\nYou’ve collected: Flower Key")))
               character.add_to_inventory("Flower Key")
           elif user_choice == 2:
               print("\nWhy wouldn't you take this beautiful flower key?? crazy crazy person, Anyways lets move on")


           input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1


       elif living_room_nav_choice == '3':
           print("You look under the carpet, Theres a trapdoor and its made of dark, weathered wood that doesn’t match"
                 " the floorboards around it. Its edges are \nreinforced with iron bands, pitted with rust, as though "
                 "it hasn’t been opened in decades. A thick, heavy padlock holds it shut, its surface cold \nand covered "
                 "in scratches, as if someone—or something—tried to force it open long ago. The faint scent of damp"
                 " earth seeps through the cracks, \nand the sound of faint dripping water can be heard when you press "
                 "your ear against it. You probably wont be able to open it, its not like they wanted you to anyways. \n\nLets uh... move on...")
           input(
               red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))


           all_rooms += 1


       elif living_room_nav_choice == '4':
           print("Reaching into the cushions, your fingers brush against something cold and metallic,\nbut when you pull "
                 "your hand back, its a pocket watch?\nThe pocket watch is ornate but tarnished, its silver casing scratched "
                 "and dull.\nThe glass face is cracked, with jagged lines running across it like a\nspider’s web. The hands "
                 "are frozen at 3:33, and the inner\nmechanisms are exposed, ticking faintly even though the watch clearly "
                 "shouldn’t work.\nAn inscription on the back reads:\n")
           print(Colors.ITALIC + (red(" \t\t'Time waits for no one, but here it stood still.'\n")))
           print("Holding it, you feel a strange coldness creep up your arm, as though the watch is more than it seems.\n"
                 "The cushions themselves are oddly heavy, as though stuffed with more than "
                 "just padding. A faint hum \nemanates from deep within, barely audible but unmistakable. The longer you "
                 "sit near it, \nthe more you feel a strange pressure building in your ears, like the room itself is trying "
                 "to \npush you away. \nWould you like to take it? \n 1. Yes \n 2. No\n\n\n")


           user_choice = int(input(yellow("Enter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(Colors.ITALIC + (red("\nYou’ve acquired: A Pocket Watch-stuck in time?")))
               character.add_to_inventory("Pocket watch")


           elif user_choice == 2:
               print("\nThis pocket watch could've been used for uh...important things but oh well, lets move on.")


           input(red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
           all_rooms += 1
