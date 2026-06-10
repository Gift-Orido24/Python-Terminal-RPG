from fight import attack_sequence
attack = attack_sequence
def game_story():
    return "The world has lost it's battle against the invaders, all was thought lost. But the catastrophe brought about the birth of heroes with superhuman abilities who would rise up and reclaim our world. AND YOU ARE ONE OF THEM!!"

def intermission():
    while True:
            pause = input("Enemy killed, press n to continue\n>").lower()
            if pause == 'n':
                return
            else:
                print("invalid input")
            
def action(db,player,enemy):
            if attack(player,enemy):
                print(intermission())
                player.update_status()
                print(db.loading())
                return True
            else:
                print("you were killed")
                return False
            
def level_one(db,player,enemy):
    while True:
        print("you're in a dark house, your eyes aren't affected, theres a noise around the corner, you saw a goblin...")
        choice = input("<<1.attack>>\n<<2.avoid>>\n>")
        if choice == '1':
            if action(db,player,enemy):
                return
            else:
                return "Game over"
        elif action == '2':
            return False
        else:
            print("invalid option")
    