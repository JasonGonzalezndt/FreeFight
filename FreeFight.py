import random
import time

#creates the player class where we will set up new characters
class Player:
    def __init__(self, max_hp, health, inventory, armor, damage, ac, name):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.ac = ac
        self.name = name
        self.inventory = inventory
        self.max_hp = max_hp

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
        return self.health
    
    #method to determine if player hits the enemy or misses
    def roll_for_hit(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > enemy.ac:
           return True
        else:
            return False
        
    
    #heal if player has potion in their inventory
    def use_health_potion(self):
        if self.inventory['Health Potion'] >= 1:
            if self.health >= (self.max_hp - 25): #check if hp is less than the total potion healing
                self.health = self.max_hp #if so set health to max health to prevent overhealing from a health potion
            else:
                self.health += 25
            print(f'{self.name} healed to {self.health} HP!')
            self.inventory['Health Potion'] -=1
            return self.health
            
        else:
            print('Out of healing potions!')
            

    #function which checks if fighter is alive
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False


#creates NPC's that we will be able to interact with
class npc:
    def __init__(self,max_hp, health, inventory, armor, damage, ac, name):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.ac = ac
        self.name = name
        self.inventory = inventory
        self.max_hp = max_hp


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
    
    def roll_for_hit(self):
        attack_chance = random.randint(1, 20)
        if attack_chance > player.armor:
            return True
        else:
            return False
        
    def use_health_potion(self):
        if self.inventory['Health Potion'] >= 1:
            if self.health >= (self.max_hp - 25):
                self.health = self.max_hp
            else:
                self.health += 25
            print(f'{self.name} healed to {self.health} HP!')
            self.inventory['Health Potion'] -=1
            return self.health
            
        else:
            print('Out of healing potions!')
            

    #function which checks if fighter is alive
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False


#user input to create a name and assign it to your character
player_name = input("What is the name of your fighter?")     
player = Player(100, 100, {'Health Potion': 1}, 10, 15, 13, player_name)
enemy = npc(100, 100, {'Health Potion': 1}, 5, 10, 10, "Goblin")


        
class Combat_Loop:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def combat_round(self):
        if self.player.check_if_alive():
            self.player_turn()
        
        if self.enemy.check_if_alive():
            self.enemy_turn()

        if not self.player.check_if_alive():
            print(f"Game over. {self.player.name} has been defeated!")
            return False
        elif not self.enemy.check_if_alive():
            print(f"Victory! {enemy.name} has been defeated")
            return False
        return True


    #create a list of different flavor texts to make the combat more exciting
    def combat_text(self, hit_success, attacker, defender):

        #creating a list for both a hit confirm and a miss to store values depending on whether or not roll_for_damage returns a hit confirm or a miss (True or False)
        hit = [f"{attacker.name} charges forward and slashes the {defender.name} for {attacker.damage} damage! {defender.health} HP left!",
                f"{attacker.name} side steps the enemys attack and counters with a quick stab for {attacker.name} damage! {defender.health} HP left!",
                f"{attacker.name} spots a gap in the {enemy.name}'s defenses and expertly attacks for {attacker.damage} damage! {defender.health} HP left!",
                f"Look over there! {attacker.name} catches the {defender.name} by surprise and slashes for {attacker.damage} damage. What a fool! {defender.health} HP left!",
                f"With a herculean effort we cover ground in an instant taking the {defender.name} by surprise and gashing their torso for {attacker.damage} damage, {defender.health} HP left!",
                f"Raising their weapon high, {attacker.name} brings it down with thunderous force, striking {defender.name} squarely and dealing a powerful {attacker.damage} damage. {defender.health} HP left!",
                f"With a wild battle cry, {attacker.name} lunges forward, delivering a savage strike to {defender.name} and inflicting {attacker.damage} damage. {enemy.health} HP left!",
                f"{attacker.name} swings their weapon in a wide arc, cleaving through the air and landing a heavy blow on {defender.name}, dealing {attacker.damage} damage. {defender.health} HP left!",
                f"With a look of determination, {attacker.name} delivers an unyielding strike to {defender.name}, overpowering their defenses and dealing {attacker.damage} damage. {defender.health} HP left!",
                f"In a display of pure martial skill, {attacker.name} unleashes a rapid flurry of blows, each one landing hard on {defender.name}, culminating in {attacker.damage} total damage. {defender.health} HP left!",
                f"{attacker.name} steps in close, delivering a brutal uppercut with the hilt of their weapon to {defender.name}, causing a staggering {attacker.damage} damage. {defender.health} HP left!"
        ]
        miss = [f"{attacker.name} swings mightily at {defender.name}, but they nimbly dodge aside, evading the attack.",
                f"With a quick maneuver, {defender.name} parries {attacker.name}'s strike, deflecting the weapon away at the last second.",
                f"{attacker.name} lunges forward, but misjudges the distance. The attack falls short, missing {defender.name}.",
                f"As {attacker.name} aims their blow, {defender.name} slips away like a shadow, making the strike miss its mark.",
                f"{attacker.name}'s attack comes crashing down, but {defender.name} raises their shield just in time, blocking the attack.",
                f"Just as {attacker.name} strikes, {defender.name} unexpectedly shifts position, causing the attack to whiff through empty air.",
                f"{attacker.name}'s weapon connects, but only glances off {defender.name}'s sturdy armor without causing harm.",
                f"{enemy.name} feints at the last second, startling {attacker.name} and causing their attack to miss its intended target.",
                f"With a powerful swing, {attacker.name} aims at {defender.name}, but the timing is off, leading the strike to pass harmlessly aside."
            
        ]

        if hit_success:
            print(random.choice(hit))
        else:
            print(random.choice(miss))

    def player_turn(self):
        if self.player.health <40:
            self.player.use_health_potion()
        if self.player.roll_for_hit():
            self.enemy.receive_attack(player)
            self.combat_text(True, player, enemy)
        elif not self.player.roll_for_hit():
            self.combat_text(False, player, enemy)
        time.sleep(1)

    def enemy_turn(self):
        if self.enemy.health <40:
            self.player.use_health_potion()
        if self.enemy.roll_for_hit():
            self.player.receive_attack(enemy)
            self.combat_text(True, enemy, player)
        elif not self.enemy.roll_for_hit():
            self.combat_text(False, enemy, player)
        time.sleep(1)

    def start_combat(self):
        print("Combat starts!")
        while self.player.check_if_alive() and self.enemy.check_if_alive():
            if not self.combat_round():
                break

combat_loop = Combat_Loop(player, enemy)
combat_loop.start_combat()