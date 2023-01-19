import random
import time 

def space():
    time.sleep(2)



class stats():
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor
    
class mage(stats):
    def stats(self):
        self.armor = 5
        self.damage = 13
        self.health = 20
    def showStats(self):
        print(f"""You are choose the Mage. Your stats are; 
        Armor {self.armor}
        Damage {self.damage}
        Health {self.health}
        """)

class tank(stats):
    def stats(self):
        self.armor = 20
        self.damage = 5
        self.health = 30
    def showStats(self):
        print(f"""You are choose the Tank. Your stats are; 
        Armor {self.armor}
        Damage {self.damage}
        Health {self.health}
        """)

class fighter(stats):
    def stats(self):
        self.armor = 10
        self.damage = 15
        self.health = 10
    def showStats(self):
        print(f"""You are choose the Fighter. Your stats are; 
        Armor {self.armor}
        Damage {self.damage}
        Health {self.health}
        """)


# Charcter Chooser
def charcterChoose():
    global user1Character
    global user2Character

    user1input = int(input("""
        1- Mage (armaor = 5, damage = 13, health = 20)
        1- Tank (armaor = 20, damage = 5, health = 30)
        1- Fighter (armaor = 10, damage = 15, health = 10)
        
        """))
    # Character choose for user1
    if user1input == 1:
        user1Character = mage(20, 13, 5)
        user1Character.showStats()
    elif user1input == 2:
        user1Character = tank(30, 5, 20)
        user1Character.showStats()
    elif user1input == 3:
        user1Character = fighter(10, 15, 10)
        user1Character.showStats()
    # Character choose for user2
    user2input = int(input("""
        1- Mage (armaor = 5, damage = 13, health = 20)
        2- Tank (armaor = 20, damage = 5, health = 30)
        3- Fighter (armaor = 10, damage = 15, health = 10)
        
        """))
    if user2input == 1:
        user2Character = mage(20, 13, 5)
        user2Character.showStats()
    elif user2input == 2:
        user2Character = tank(30, 5, 20)
        user2Character.showStats()
    elif user2input == 3:
        user2Character = fighter(10, 15, 10)
        user2Character.showStats()
    


charcterChoose()