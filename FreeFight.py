import random
import time

#creates the player class where we will set up new characters
class Player:
    def __init__(self, health, armor, damage):
        self.health = health
        self.armor = armor
        self.damage = damage
    #method to determine if player hit's the enemy and if they do how much damage they deal
    def roll_for_damage(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > enemy.armor:
            damage = self.damage
            enemy.health -= damage
            return enemy.health
        else:
            print('The Hero missed the attack')
    #function which checks if both characters are alive, if so, combat continues
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False


#creates NPC's that we will be able to interact with
class npc:
    def __init__(self, health, armor, damage):
        self.health = health
        self.armor = armor
        self.damage = damage

    def roll_for_damage(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > player.armor:
            damage = self.damage
            player.health -= damage
            return player.health
        else:
            print('The enemy missed the attack')
    #function which checks if both characters are alive, if so, combat continues
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False
     

player = Player(100, 10, 10)
enemy = npc(100, 7, 8)

while player.check_if_alive() and enemy.check_if_alive():
    if player.check_if_alive():
        player.roll_for_damage()
        print(f'Hero slashed the enemy for {player.damage} and left the enemy with {enemy.health}')
        time.sleep(1)
    if enemy.check_if_alive():
        enemy.roll_for_damage()
        print(f'The Enemy slashed the hero for {enemy.damage} and left the hero with {player.health}')
        time.sleep(1)
    else: 
        print('Game Over')