
class Card(object):

    def __init__(self, damage, health, defense, strength, energy, description):
        self.damage = damage
        self.health = health
        self.defense = defense
        self.strength_buff = strength
        self.energy = energy
        self.description = description

    def print_effects(self):
        if self.health > 0:
            print(f"boosted health by {self.health}")
        if self.defense > 0:
            print(f"gained {self.defense} defense")
        if self.strength_buff > 0:
            print(f"boosted strength by {self.strength_buff}")
        print(f"Used up {self.energy} energy!")

# extra card classes would do special things like make you draw a card or make you discard or stuff like that
