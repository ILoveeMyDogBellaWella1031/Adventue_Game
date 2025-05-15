class Character:

   def __init__(self, name):
       self.name = name
       self.health = 100
       self.score = 0
       self.inventory = []


   def __str__(self):
    return f"{self.name}"
           # f"\t\t\tHealth: {self.health}'\t\t\tScore: {self.score}")


   def dec_health(self, health):
       self.health -= health
       if self.health <= 0:
           print(f"You died!")


   def add_to_health(self, amount):
       self.health += amount
       print(f"You have {self.health} health left! Great Job.")


   def add_to_inventory(self, item):
       self.inventory.append(item)
       print(f"\nYou have {self.inventory} in inventory!")


   def remove_from_inventory(self, item):
       self.inventory.remove(item)
       print(f"You have removed {item}")


   def retrieve_inventory(self):
       return self.inventory


