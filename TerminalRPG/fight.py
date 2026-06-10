import time
def player_turn(player,enemy):
            start = time.time()
            action = input(">>>Attack\n<press enter>")
            end = time.time()
            delay = end-start
            if delay > 1:
                    print("too slow!!")
                    damage = max(0,enemy.harm(player))
                    return f"you've been hit\nHp: {damage}"
            else:
                    if not any(c.strip() for c in action):
                        harm = max(0,player.attack(enemy))
                        return f"Enemy Hp:{harm}"
                    else:
                        return "press enter"
                    
def enemy_turn(player,enemy):
            begin = time.time()
            choice = input(">>>Defend\n<press enter>")
            stop = time.time()
            lag = stop-begin
            if lag > 1:
                    hurt = max(0,enemy.harm(player))
                    print("Too slow, you were hit")
                    return f"Hp:{hurt}"
            else:
                    if not any(c.strip() for c in choice):
                        return "you blocked attack!"
                    else:
                        return "press enter"
                                      
def attack_sequence(player,enemy):
    fighting = True
    while fighting is True:
        print(player_turn(player,enemy))
        if enemy.killed():
            player.kill_count+=1
            return True
        else:
                if player.death():
                    return False
        print(enemy_turn(player,enemy))
        
    
    
    