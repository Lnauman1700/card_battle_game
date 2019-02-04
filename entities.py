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
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(0,3,0,0,1, 'Costs 1 energy. Heals 3 health'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(0,0,0,2,2, 'Costs 2 energy. Buffs strength by 2'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage')
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

        self.current_hand()

    def draw_one(self):
        if len(self.draw_pile) > 0:
            self.hand.append(self.draw_pile.pop(0))
        else:
            while len(self.discard_pile) > 0:
                rando = random.randint(0, len(self.discard_pile))
                self.draw_pile.append(discard_pile.pop(rando))
            self.hand.append(self.draw_pile.pop(0))

    def use(self, index):
        if index < len(self.hand):
            played_card = self.hand[index]

            if self.energy < played_card.energy:
                print("You don't have enough energy to use that card!")
                print(f"remaining energy: {self.energy}")
            else:
                # apply played_card's health buffs to the player's health
                self.health += played_card.health
                # apply played_card's defense buffs

                # apply played_card's strength buffs (how does this one work?)
                self.strength += played_card.strength_buff
                # remove energy from player based on card's energy
                self.energy -= played_card.energy
                # pop the card from your hand, add it to the front of discard pile
                self.discard_pile.insert(0, self.hand.pop(index))
                # let the user know what the card they just played did.
                played_card.print_effects()
                # return the damage
                return played_card.damage

        else:
            print("That card doesn't exist. It might've been used up or you might've put in the wrong number")
        # I'd like to give the player a list of cards they can use, but it doesn't work if we return a value

    # gives player the option to end their turn early
    def end_turn(self):
        print("You ended your turn")
        # resets the energy back to default, we don't want our player farming energy after all
        self.energy = 3


    # prints out the curent hand and what each card does. Also shows what you'd enter to play a card.
    def current_hand(self):

        index = 0
        for item in self.hand:
            print(f"{index}. {item.description}")
            index += 1


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
player.use(0)
player.use(0)
player.use(0)
print(len(player.hand))
print(player.energy)
player.end_turn()
