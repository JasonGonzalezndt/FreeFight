import random

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
    
    def roll_for_hit(self, player):
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