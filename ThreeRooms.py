from random import choice

from simple_colors import *
class Colors:
   BOLD = '\033[1m'
   ITALIC = '\033[3m'


def print_ThreeRooms_nav():
   print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\tWhere would you like to go?"
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bold'))
   print(yellow(Colors.BOLD + " 1. Room 1 \n 2. Room 2 \n 3. Room 3 \n"))
   user_r_choice = input(yellow("Enter your choice... ", 'bold'))
   return user_r_choice

def ThreeRooms_room(character, self=None):
   print((blue("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\t\tThree Rooms\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bright')))
   input()

   print((Colors.BOLD + "\nThe air seems to shift with each step toward the three doors, the faint sound of your breathing filling the "
         "silence. The carvings \non each door become more defined the closer you get. The first door, dark brown, depicts"
         " a savage beast locked in battle with a spear. \nThe second, a khaki brown, is etched with swirling waves and "
         "serpentine figures, almost as if the ocean itself is trapped in the wood. \nThe third door, identical in color "
         "to the first, bears an enigmatic carving of hands—one offering, the other grasping greedily. \nThe hallway "
         "feels longer than it should, stretching endlessly as the doors draw you closer, their presence almost alive.\n"))



#Start Three Rooms
   all_rooms = 0
   while all_rooms < 3:
       ThreeRooms_nav_choice = print_ThreeRooms_nav()
       if ThreeRooms_nav_choice == '1':
           print("\nYou walk over to the first door. The door is dark brown with the carvings of a beast fighting off the "
               "spears that thrust toward its chest. \nThe beast, a massive wolf-like creature with snarling jaws and eyes"
               " that seem to glint with fury, is depicted mid-lunge, its claws outstretched \nas if to strike back at its"
               " attacker. The spear, though seemingly piercing its side, doesn’t appear to weaken the beast—instead, "
               "it looks more enraged, \nits muscles coiled with relentless energy, as though the fight has only just "
               "begun. You turn the knob, it’s open. \n\nWould you "
               "like go... in? \n 1. Yes \n 2. No\n")

           user_choice = int(input(yellow("Enter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print(
                   red("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\tROOM 1: The Beast\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
                       "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bright'))

               input(
                   blue("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress 'Enter' to continue...\t\t\t\n"
                       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))

               print("You push the door open slowly. It groans under the weight of its own fury, the hinges crying out"
                     " as if warning you to turn back. The room beyond is dim, \nilluminated by a faint red glow that "
                     "seems to bleed from the walls themselves. The air is thick, heavy with the scent of iron and fur. "
                     "You hear a low \ngrowl—distant, but near enough to make your skin crawl. A chill runs down your "
                     "spine. Something is watching. Do you step further inside-- wait... You step forward… \nthen freeze."
                     " The growl in the dark grows louder. Your breath hitches. A primal part of you screams to leave. "
                     "You back away slowly, hand still on the doorknob, heart pounding \nlike a drum in your chest. The "
                     "door swings shut behind you, the echo sharp—like a warning. The beast waits.its too late to turn"
                     " back...")

               input(
                   blue(
                       "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress 'Enter' to continue...\t\t\t\n"
                       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))

               print(yellow("\nIn the center of the room, you find a broken spear lying next to a series of scratched symbols on"
                     " the floor. They form a riddle, almost ritualistic in nature:"))
               print(red("To silence rage, speak the truth it fears. What calms the storm when war draws near? You must choose:", 'italic'))
               print("\n 1. Speak a calming word \n 2. Offer the broken spear \n 3. Strike the beast's shadow")
               user_choice = int(input(yellow("\nEnter a number for your choice... ", 'bold')))
               if user_choice == 1:
                   print("The growl fades. A door on the far wall creaks open, revealing a hidden path. The silence "
                         "that follows is almost deafening. You feel the tension in your shoulders \nrelease. You close "
                         "your eyes for a moment, steadying your breath. The growl grows louder, more guttural… but you "
                         "don’t flinch. Then, you whisper something—simple, \nsoft, ancient. Maybe it’s a word from a "
                         "dream, maybe something buried deep inside you. The air stills. The growl pauses. The red "
                         "glow dims to amber. You feel the weight of the beast's \nrage soften, not vanish, but shift—like"
                         " a storm finally breaking after too many nights. A warm breath brushes past your cheek, l"
                         "ike wind through fur. Then silence. Ahead, the wall \nslides open with a dull click, revealing "
                         "a passage cloaked in quiet shadows, pulsing faintly with orange light. \n")

                   print("The hallway beyond the beast's chamber winds downward, the walls now smooth stone instead of "
                         "carved wood. On the floor lies a token—a silver fang-shaped pendant, warm to the touch. \nYou "
                         "feel like it belongs to you. You place it in your pocket. One door down. Two to go.")
                   print(Colors.ITALIC + (red("\nYou’ve collected:Silver fang-shaped Pendent, warm to  the touch. ")))
                   character.add_to_inventory("Silver fang-shaped Pendent")

                   input(
                       blue(
                           "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress 'Enter' to continue...\t\t\t\n"
                           "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))
               elif user_choice == 2:
                   print("The spear vanishes. The beast appears, wounded but no longer hostile, and lets you pass.The "
                         "beast locks eyes with you. For a moment, time holds still. Then it turns, fading into the "
                         "shadows. A new hallway lies behind where it stood, lit by a soft red glow. You continue on, "
                         "quietly changed. You feel lighter. The door to the hallway clicks open behind you, now bearing "
                         "a glowing mark of completion.")
               elif user_choice == 3:
                   print("You swing. Your weapon passes through the air… and the room roars.The room erupts in flames. "
                         "You stumble out of the room, coughing, burned but alive. A force shoves you into the hall, "
                         "the door slamming shut behind you. You've deeply angered the force, a red scar now burns on "
                         "the door. It will not open again.")

       all_rooms += 1

       if ThreeRooms_nav_choice == '2':
           print(
               yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\tROOM 2: The Ocean\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bright'))

           input(green("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress 'Enter' to continue...\t\t\t\n"
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))

           print("The knob refuses to budge, cool and slick beneath your fingers like wet stone. You press your "
                 "ear against the door and hear the sound of waves crashing… \nbut there’s no ocean for miles. "
                 "Suddenly, the carvings shimmer, and the door whispers: “Only the willing may drift into the "
                 "tide.”")

           print(
               blue("\nBelow the door, three seashells rest on a small pedestal—each carved with a different word: ",
                   'italic'))
           print("\n 1. Desire \n 2. Escape \n 3. Truth \nOne must be placed into a hollow at the door’s center.")
           user_choice = int(input(yellow("\nEnter a number for your choice... ", 'bold')))
           if user_choice == 1:
               print("The door unlocks with a hiss, but the room shifts to lure you deeper into illusion.")
               int(input("Would you like to follow? \n1. Yes \n2. No \nTell me: "))
               if user_choice == 1:
                   print("You place the shell etched with Desire into the hollow. The beach glows too brightly. The waves move but there’s no wind. You realize your not"
                         " alone—something watches beneath the surface. \nYou look down to see an array of seashells "
                         "varying in color and shape. You notice that theres different shapes on each of them. \nTo the "
                         "right of you theres a lone stone and a... riddle?? Again?? it reads:\n")

                   print(blue("Triangle of the Tide, complete it to see. You must choose:", 'italic'))
                   while True:
                    solution = input("Place the shells in a shape (circle, triangle, square): ").lower()
                    if solution == 'triangle':
                           print("\nThe shells glow faintly. A drawer opens, revealing a seashell amulet.\n")
                           character.add_to_inventory("amulet")
                           return
                           #figure out how to return back
                    else:
                           print("\nThe shells stay dim. Maybe you should try again. \n")
               elif user_choice == 2:
                   print("You slot in the shell marked Escape. When you step inside, it’s pitch black. Then slowly, "
                         "moonlight filters through stained-glass panels of crashing waves. You are on a ship, broken "
                         "in half, suspended in time. Every creak echoes forever. On the captain’s chair lies a silver "
                         "compass, pointing to nothing.You may take it… or leave it. Either way, the door behind you "
                         "now opens freely.Will you... take it? \n1. Yes \n2. No")
                   int(input("Tell...us:"))
                   if user_choice == 1:
                       character.add_to_inventory("Silver fang-shaped Pendent")
                   else:
                       print("You leave it behind but you cant help but feel like this is the last time you see it...")
               elif user_choice == 3:
                       print("You place the Truth shell. The lock shatters. The illusion lifts, revealing a flooded "
                             "chamber of mirrors and serpent "
                             "eyes.  The mirrors show you things you’ve hidden from yourself. Mirrors cover the walls. "
                             "But your reflection doesn’t follow your movements. Behind one mirror, a whisper: “You "
                             "wanted to know. So remember.” "
                             "The serpents blink once, You reach out—and pull away a mirror. Behind it is a message, "
                             "written in salt: “The serpent sleeps… but not forever.” "
                             "then vanish. A light flickers overhead, revealing a path forward. You carry the truth with"
                             " The water drains, revealing a spiral staircase back to the hall. You leave, uneasy but wiser."
                             "you, even if it stings.")

               input(
                   yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress to 'Enter' to continue...\t\t\t\n"
                       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))


       all_rooms += 1

       if ThreeRooms_nav_choice == '3':
           print(
               green(
                   "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\tROOM 3: Greed? or Generosity\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
                   "~~~~~~~~~~~~~~~~~~~~~~~~~\t\n\t\t\t\t\t\t\t\t", 'bright'))

           input(
               yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\tPress 'Enter' to continue...\t\t\t\n"
                     "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 'bold'))

           print("You touch the door and it swings open without resistance—too easily. The room is gold-lit, walls lined "
                 "with shelves of treasures, trinkets, and offerings. A pedestal sits in the center, holding a glowing "
                 "scale. Above it, carved in stone: “What you give, you may receive. What you take, you may owe.” \nyou "
                 "may owe. You look at what you have in your pocket” Three objects are available to use: \n 1. "
                 "The Gold Coin from your pocket \n 2. A ruby from thw shelf \n 3. The note that says your name")

           int(input("Pick Wisely: "))
           if user_choice == 1:
               print("You place your own coin on the scale. It wobbles, then balances perfectly. A quiet chime echoes "
                     "as the drawer opens. The key feels warm in your hand.You leave the room with a strange peace in "
                     "your chest. Balance, it seems, is rewarded. The door behind you opens. One mark glows upon it—room "
                     "complete. You return to the hall.")
               self.inventory.remove("A Gold Coin")
           elif user_choice == 2:
               print("You ignore the coin in your pocket and instead reach for the ruby sitting on the shelf. You gently place it onto the scale. It sinks violently then you hear a deep deafening voice.")
               print(red("\nYOUR GREED SICKENS ME\n"))
               print("\nSirens wail. "
                     "The room shakes. Gold turns to ash. Walls begin to melt. You run—forced to leap through the now-open "
                     "door as the room implodes behind you. The door slams shut. The glowing mark flickers, half-lit. "
                     "You survived, but not unchanged.\n")
           elif user_choice == 3:
               print("You take the piece of paper out, looking at it as if its about to write your future. They asked "
                     "for an offering and this is what you have. You place it on the scale. Nothing happens. Then… "
                     "everything happens. The air grows cold. Light flickers. You feel something tug at your mind, "
                     "your memories. You feel… smaller. But the way forward is open. You exit slowly, unsure what you "
                     "left behind.")
               self.inventory.remove("A Note")

           all_rooms += 1

       else:
           print("Nuh uh! Dont punk out just yet")


#Tried new system, didnt work
           # if choice.isdigit():
           #     index = int(choice) - 1
           #     if 0 <= index < len(character.inventory):
           #         selected_item: object = character.inventory[index]
           #         print(f"You chose: {selected_item}")
           #         if {selected_item} == selected_item: "A Gold Coin"
           #          print("The scale tips briefly, then rights itself. A hidden drawer opens with a key. "
           #                       "In the corner theres a chess. You use the key on it and open it. Its a bag of gold.")
           #         elif {selected_item} == selected_item: "Pocket Watch"
           #          print("The scale plunges. Alarms sound. The treasure begins to decay. The room trembles. You "
           #                       "snatch the key and run. Outside, the door crumbles behind you. Greed always takes more "
           #                       "than it gives.")
           #         elif {selected_item} == selected_item: "Note"
           #          print("The room dims.  Your breath catches as the letters fade from the note… and from your"
           #                        " mind. The key glows in your hand, but you feel hollow. What did you lose? You leave "
           #                        "the room, unsure what part of yourself stayed behind.")
           #          else:
           #




