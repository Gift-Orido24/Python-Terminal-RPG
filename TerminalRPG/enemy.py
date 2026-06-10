class Enemy:
    def __init__(self):
        self.hp = 6
        self.damage = 2
    def harm(self,player):
        player.hp-=self.damage
        return player.hp
    def killed(self):
        if self.hp == 0:
            return True
        else:
            return False