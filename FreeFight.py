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
        if self.health < 0:
            self.health = 0
        print(f'{self.name} took a brazen slash from {enemy.name} for {damage_taken} (reduced from {enemy.damage}) leaving the hero with {player.health}hp left!')
        return self.health
    
    #method to determine if player hits the enemy or misses
    def roll_for_hit(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > enemy.ac:
           time.sleep(1)
           return True
        else:
            time.sleep(1)
            return False
        
    #create a list of different flavor texts to make the combat more exciting
    def combat_text(self,enemy):
        #creating a list for both a hit confirm and a miss to store values depending on whether or not roll_for_damage returns a hit confirm or a miss (True or False)
        hit = [f"{self.name} charges forward and slashes the {enemy.name} for {self.damage} damage! {enemy.health} HP left!",
                f"{self.name} side steps the enemys attack and counters with a quick stab for {self.damage} damage!{enemy.health} HP left!",
                f"{self.name} spots a gap in the {enemy.name}'s defenses and expertly attacks for {self.damage} damage!{enemy.health} HP left!",
                f"Look over there! {self.name} catches the {enemy.name} by surprise and slashes for {self.damage} damage. What a fool!{enemy.health} HP left!",
                f"With a herculean effort we cover ground in an instant taking the {enemy.name} by surprise and gashing their torso for {self.damage} damage, {enemy.health} HP left!",
                f"Raising their weapon high, {self.name} brings it down with thunderous force, striking {enemy.name} squarely and dealing a powerful {self.damage} damage.{enemy.health} HP left!",
                f"With a wild battle cry, {self.name} lunges forward, delivering a savage strike to {enemy.name} and inflicting {self.damage} damage.{enemy.health} HP left!",
                f"{self.name} swings their weapon in a wide arc, cleaving through the air and landing a heavy blow on {enemy.name}, dealing {self.damage} damage.{enemy.health} HP left!",
                f"With a look of determination, {self.name} delivers an unyielding strike to {enemy.name}, overpowering their defenses and dealing {self.damage} damage.{enemy.health} HP left!",
                f"In a display of pure martial skill, {self.name} unleashes a rapid flurry of blows, each one landing hard on {enemy.name}, culminating in {self.damage} total damage.{enemy.health} HP left!",
                f"{self.name} steps in close, delivering a brutal uppercut with the hilt of their weapon to {enemy.name}, causing a staggering {self.damage} damage.{enemy.health} HP left!"
        ]
        miss = [f"{self.name} swings mightily at {enemy.name}, but they nimbly dodge aside, evading the attack.",
                f"With a quick maneuver, {enemy.name} parries {self.name}'s strike, deflecting the weapon away at the last second.",
                f"{self.name} lunges forward, but misjudges the distance. The attack falls short, missing {enemy.name}.",
                f"As {self.name} aims their blow, {enemy.name} slips away like a shadow, making the strike miss its mark.",
                f"{self.name}'s attack comes crashing down, but {enemy.name} raises their shield just in time, blocking the attack.",
                f"Just as {self.name} strikes, {enemy.name} unexpectedly shifts position, causing the attack to whiff through empty air.",
                f"{self.name}'s weapon connects, but only glances off {enemy.name}'s sturdy armor without causing harm.",
                f"{enemy.name} feints at the last second, startling {self.name} and causing their attack to miss its intended target.",
                f"With a powerful swing, {self.name} aims at {enemy.name}, but the timing is off, leading the strike to pass harmlessly aside."
            
        ]
        #if the roll_for_damage method returns True then this will select a random hit confirm line, otherwise it will print a random miss line
        if self.roll_for_hit():
            message = random.choice(hit)
        else:
            message = random.choice(miss)
        print(message)



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


#user input to create a name and assign it to your character
player_name = input("What is the name of your fighter?")     
player = Player(100, 10, 15, 10, player_name)
enemy = npc(100, 5, 7, 10, "Goblin")

#core game loop is here. While all fighters are alive the game loop continues, else it's game over
while player.check_if_alive() and enemy.check_if_alive():
    #if player is still alive execute attack
    if player.check_if_alive():
        if player.roll_for_hit():#checks if player was sucessfully able to hit the enemy
            player.combat_text(enemy)# if roll_for_damage returns true this will print a hit confirm 
            enemy.receive_attack(player) #enemy is hit and receives damage
            time.sleep(1.5)
        else:
            player.combat_text(enemy) #if roll_for_damage returns false this will print a miss message
            time.sleep(1.5)
    if enemy.check_if_alive():
        if enemy.roll_for_hit():
            player.receive_attack(enemy)
            time.sleep(1.5)
    else:
        print("Game Over")

        

    
            


       