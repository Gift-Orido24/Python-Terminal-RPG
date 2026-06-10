from player import Player
from plyerdata import Player_data
from enemy import Enemy
from fight import attack_sequence
from gameplay import level_one
db = Player_data()
enemy = Enemy()
player = Player(db,username=input("username: "))
print(level_one(db,player,enemy))


       
    