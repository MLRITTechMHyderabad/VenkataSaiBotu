import random

class Character():
    def __init__(self,name,health,attack_power,defense,speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    
    def attack(self,target):
        damage = max(self.attack_power - target.defense, 1)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def take_damage(self,amount):
        self.health -= amount
        if self.health < 0 :
            print(f"{self.name} has been defeated.")

    def is_alive(self) :
        return self.health > 0

class Warrior(Character) :
    def __init__(self,name,health,attack_power,defense,speed):
        super.__init__(name,health,attack_power,defense,speed)
        self.rage = 0

    def special_ability(self) :
        if self.health < 0.3*self.health :
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode!")

class Mage (Character) :
    def __init__(self,name,health,attack_power,defense,speed):
        super.__init__(name,health,attack_power,defense,speed)
        self.mana = 100
    
    def special_ability(self,target):
        if self.mana >= 20 :
            damage = self.attack_power*2
            target.take_damage(damage)
            self.mana -= 5
            self.take_damage(5)
            print(f"{self.name} casts Fireball on {target.name} for {damage} damage.")
        else:
            print(f"{self.name} doesn't have enough mana for Fireball.")

class Archer (Character) : 
    def __init__(self,name,health,attack_power,defense,speed):
        super.__init__(name,health,attack_power,defense,speed)
        self.critical_chance = 0.3
    
    def special_ability(self,target):
        if random.random() < self.critical_chance :
            damage = self.attack_power * 2
            target.take_damage(damage)
            print(f"{self.name} lands a Critical Hit on {target.name} for {damage} damage.")
        else:
            self.attack(target)
