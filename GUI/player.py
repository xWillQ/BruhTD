

class Player():
    def __init__(self, hp, gold):
        self.hp = hp
        self.gold = gold
        self.alive = True

    def hp_loss(self, mob):
        self.hp -= mob.damage

    def gold_add(self, mob):
        self.gold += mob.reward
