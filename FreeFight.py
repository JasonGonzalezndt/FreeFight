from Player_Settings import Player
from npc_settings import npc
from Combat_Settings import Combat_Loop

enemy = npc(100, 100, {'Health Potion': 1}, 5, 10, 10, "Goblin")
#user input to create a name and assign it to your character
player_name = input("What is the name of your fighter?")     
player = Player(100, 100, {'Health Potion': 1}, 10, 15, 13, player_name)

combat_loop = Combat_Loop(player, enemy)
combat_loop.start_combat()