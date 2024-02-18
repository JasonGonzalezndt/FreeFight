import random
import time
import math
#creates the player class where we will set up new characters
class Player:
    def __init__(self, health, armor, damage, ac, name):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.ac = ac
        self.name = name

    #Create an attack method that we can then use in the roll_for_damage method right underneath
    
    def calculate_damage_taken(self, incoming_damage):
        #armor reduces damage by a 1.5% per point of armor
        reduction_percentage = self.armor * 1.5
        reduced_damage = incoming_damage * (100 - reduction_percentage) / 100
        #round the damage total up to prevent floats in health / damage
        rounded_damage = round(reduced_damage)
        #prevent situations where high armor values would return negative damage and heal the player
        final_damage = max(0, rounded_damage)
        return final_damage
    
    #this receives the damage and applies it to our hp bar. It also shows the effectiveness of armor so we have more feedback
    def receive_attack(self, enemy):
        damage_taken = self.calculate_damage_taken(enemy.damage)
        self.health -= damage_taken
        print(f'{self.name} took a brazen slash from {enemy.name} for {damage_taken} (reduced from {enemy.damage}) leaving the hero with {player.health}hp left!')
        return self.health
    
    #method to determine if player hits the enemy or misses
    def roll_for_damage(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > enemy.ac:
           time.sleep(1)
           return True
        else:
            print(f'The quick slash narrowly missed the {enemy.name}')
            time.sleep(1)
            return False

    #function which checks if fighter is alive
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False


#creates NPC's that we will be able to interact with
class npc:
    def __init__(self, health, armor, damage, ac, name):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.ac = ac
        self.name = name

    def calculate_damage_taken(self, incoming_damage):
        #armor reduces damage by a 1.5% per point of armor
        reduction_percentage = self.armor * 1.5
        reduced_damage = incoming_damage * (100 - reduction_percentage) / 100
        #round the damage total up to prevent floats in health / damage
        rounded_damage = round(reduced_damage)
        #prevent situations where high armor values would return negative damage and heal the player
        final_damage = max(0, rounded_damage)
        return final_damage
    
    def receive_attack(self, player):
        damage_taken = self.calculate_damage_taken(player.damage)
        self.health -= damage_taken
        if self.health < 0:
            self.health = 0
        print(f'{self.name} is charged by {player.name} and brutally slashed for {damage_taken} (reduced from {player.damage}) the {enemy.name} only has {enemy.health} hp left!')
        return self.health
    
    def roll_for_damage(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > player.armor:
            time.sleep(1)
            return True
        else:
            print(f'The wild swing from {enemy.name} narrowly missed {player.name}')
            time.sleep(1)
            return False

    #function which checks if fighter is alive
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False
     
player = Player(100, 10, 15, 10, "PK")
enemy = npc(100, 5, 7, 10, "Goblin")

#core game loop is here. While all fighters are alive the game loop continues, else it's game over
while player.check_if_alive() and enemy.check_if_alive():
    #if player is still alive execute attack
    if player.check_if_alive():
        if player.roll_for_damage():#checks if player was sucessfully able to hit the enemy
            enemy.receive_attack(player) #enemy is hit and receives damage
            time.sleep(1.5)
    if enemy.check_if_alive():
        if enemy.roll_for_damage():
            player.receive_attack(enemy)
            time.sleep(1.5)
    else:
        print("Game Over")

        
    
            


       