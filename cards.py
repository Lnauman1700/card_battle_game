
class Card(object):

    def __init__(self, damage, health, defense, strength, energy):
        self.damage = damage
        self.health = health
        self.buff = defense
        self.strength = strength
        self.energy = energy

    def apply(self):
        return [self.damage, self.health, self.defense, self.strength, self.energy]
