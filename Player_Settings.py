import random

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
    def roll_for_hit(self, enemy):
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
            
    #this will allow us to select our next action
    def turn_select(self):
        actions = ["Attack", "Heal"]
        actions_string = "\n".join(actions)  # Join each action with a newline character
        choice = input(f"Choose your action:\n{actions_string}\n> ")
        return choice


    #function which checks if fighter is alive
    def check_if_alive(self):
        if self.health > 0:
            return True
        else:
            return False
