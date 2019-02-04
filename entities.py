import cards
import random

class Entity(object):

    # init function which takes self, name
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.strength = 2

    # lower_health function which takes self, damage and lowers health by damage
    def lower_health(self, damage):
        self.health -= damage

    # attack method which takes self, returns number = self.strength + any item modifier. may require another param of item
    def attack(self):
        print(f"{self.name} did {self.strength} damage")
        return self.strength

class Player(Entity):

    # dictionary (?) with all items currently in posession.


    # inherits __init__, lower_health, and attack (attack may need changed to suit item use)
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.item_mod = 0
        self.draw_pile = [
            cards.Card(2,0,0,0,1),
            cards.Card(2,0,0,0,1),
            cards.Card(2,0,0,0,1),
            cards.Card(2,0,0,0,1),
            cards.Card(2,0,0,0,1),
            cards.Card(2,0,0,0,1)
        ]
        self.discard_pile = []
        self.hand = []
        self.energy = 3

    def draw(self):
        iterations = 0

        while iterations < 4:
            if len(self.draw_pile) > 0:
                self.hand.append(self.draw_pile.pop(0))
                iterations += 1
            else:
                while len(self.discard_pile) > 0:
                    rando = random.randint(0, len(self.discard_pile))
                    self.draw_pile.append(discard_pile.pop(rando))



    def attack(self):
        print(f"You did {self.strength + self.item_mod} damage")
        return self.strength + self.item_mod

    def get_current_health(self):
        print(f"Current health is {self.health}")

    # potential add_item function to add an item to our dict inventory


class Enemy(Entity):

    # overrides __init__ but we can specify the strength and health of them, inherits lower_health, attack
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

player = Player('Bill')
player.draw()
print(len(player.hand))
