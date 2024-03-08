import random

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
            print(f"Victory! {self.enemy.name} has been defeated")
            return False
        return True


    #create a list of different flavor texts to make the combat more exciting
    def combat_text(self, hit_success, attacker, defender):

        #creating a list for both a hit confirm and a miss to store values depending on whether or not roll_for_damage returns a hit confirm or a miss (True or False)
        hit = [f"{attacker.name} charges forward and slashes the {defender.name} for {attacker.damage} damage! {defender.health} HP left!",
                f"{attacker.name} side steps the enemys attack and counters with a quick stab for {attacker.name} damage! {defender.health} HP left!",
                f"{attacker.name} spots a gap in the {defender.name}'s defenses and expertly attacks for {attacker.damage} damage! {defender.health} HP left!",
                f"Look over there! {attacker.name} catches the {defender.name} by surprise and slashes for {attacker.damage} damage. What a fool! {defender.health} HP left!",
                f"With a herculean effort we cover ground in an instant taking the {defender.name} by surprise and gashing their torso for {attacker.damage} damage, {defender.health} HP left!",
                f"Raising their weapon high, {attacker.name} brings it down with thunderous force, striking {defender.name} squarely and dealing a powerful {attacker.damage} damage. {defender.health} HP left!",
                f"With a wild battle cry, {attacker.name} lunges forward, delivering a savage strike to {defender.name} and inflicting {attacker.damage} damage. {defender.health} HP left!",
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
                f"{defender.name} feints at the last second, startling {attacker.name} and causing their attack to miss its intended target.",
                f"With a powerful swing, {attacker.name} aims at {defender.name}, but the timing is off, leading the strike to pass harmlessly aside."
            
        ]

        if hit_success:
            print(random.choice(hit))
        else:
            print(random.choice(miss))

    def player_turn(self):
        action = self.player.turn_select()
        if action == "Attack":
            if self.player.roll_for_hit(self.enemy):
                self.enemy.receive_attack(self.player)
                self.combat_text(True, self.player, self.enemy)
            elif not self.player.roll_for_hit(self.enemy):
                self.combat_text(False, self.player, self.enemy)
        elif action == "Heal":
            self.player.use_health_potion()

    def enemy_turn(self):
        if self.enemy.health <40 and self.enemy.inventory['Health Potion'] >= 1:
            self.enemy.use_health_potion()
        if self.enemy.roll_for_hit(self.player):
            self.player.receive_attack(self.enemy)
            self.combat_text(True, self.enemy, self.player)
        elif not self.enemy.roll_for_hit(self.player):
            self.combat_text(False, self.enemy, self.player)

    def start_combat(self):
        print("Combat starts!")
        while self.player.check_if_alive() and self.enemy.check_if_alive():
            if not self.combat_round():
                break