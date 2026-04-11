class Character:
    def __init__(self,playerName,character, health,inventory):
        self.health = health
        self.inventory = inventory
    def printInventory(self):
        print(f"As a {self.character} you have {self.inventory}")
    def takeDamage(self, damage):
        self.health -= damage
        print(f"You took damage, you have {self.health} HP")
        if (self.health <= 0):
            print("Wasted")