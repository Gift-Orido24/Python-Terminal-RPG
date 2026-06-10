class Player:
    def __init__(self,db,username):
        self.db = db
        self.username = username
        self.damage = self.db.plyer_data[username]["Progression"]["Damage"]
        self.hp = 6
        self.kill_count = 0
    def load_player(self):
        data = self.db.get(self.username)
        return data
    def player_stats(self):
        status = [ ]
        stats = self.load_player()
        status.append(stats["Progression"])
        status.append(stats["Stats"])
        return status
    def attack(self,enemy):
            enemy.hp-=self.damage
            return enemy.hp
    def level_up(self):
        levelup = self.load_player()
        if self.kill_count == 1:
            levelup["Progression"]["Level"]+=1
            levelup["Stats"]["Strength"]+=1
            levelup["Stats"]["Agility"]+=1
            self.db.save()
            return True
        else:
            False
    def highscore(self):
        base = self.load_player()
        score = base["Progression"]["Highscore"]
        if self.kill_count > score:
            base["Progression"]["Highscore"]=self.kill_count
            self.db.save()
            return True
        else:
            False
    def update_status(self):
        self.level_up()
        self.highscore()
        return "status updated"
    def death(self):
        if self.hp == 0:
            return True
        else:
            False
        
        


