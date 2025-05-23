from simple_colors import *
class Colors:
   BOLD = '\033[1m'
   ITALIC = '\033[3m'


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


("Well done {self.name}, Your finished with exploring this odd cabbin\nand you notice something lies out there in the woods..."
"it's calling you're\n name. The sirens await will you dare to engage with them\n What secrets, challenges, or ")
