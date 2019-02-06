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
        if isinstance(damage, int):
            self.health -= damage
            if damage > 0:
                print(f"{self.name} lost {damage} health.")

    # attack method which takes self, returns number = self.strength + any item modifier. may require another param of item
    def attack(self):
        return self.strength

    def my_turn(self):
        pass

class Player(Entity):

    # dictionary (?) with all items currently in posession.

    # inherits __init__, lower_health, and attack (attack may need changed to suit item use)
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.draw_pile = [
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(0,3,0,0,1, 'Costs 1 energy. Heals 3 health'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(0,0,0,2,2, 'Costs 2 energy. Buffs strength by 2'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
            cards.Card(2,0,0,0,1, 'Costs 1 energy. Deals 2 damage'),
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
        self.strength = 0

    # allows the player to draw all the cards they need at beginning of turn
    def draw(self):
        iterations = 0

        # while loop signifying how many times we draw cards from our hand
        while iterations < 4:
            # as long as the draw pile has cards in it, we draw from it
            if len(self.draw_pile) > 0:
                self.hand.append(self.draw_pile.pop(0))
                iterations += 1
            #if the draw pile doesn't have cards in it...
            else:
                # shuffles discard pile and adds it to the draw pile
                random.shuffle(self.discard_pile)
                for card in self.discard_pile:
                    self.draw_pile.append(card)
                #clears discard pile
                self.discard_pile = []




    # allows the player to draw one card
    def draw_one(self):
        if len(self.draw_pile) > 0:
            self.hand.append(self.draw_pile.pop(0))
        else:
            random.shuffle(self.discard_pile)
            for card in self.discard_pile:
                self.draw_pile.append(card)
            #clears discard pile
            self.discard_pile = []
            self.hand.append(self.draw_pile.pop(0))

    # allows player to use card at the index in their hand
    def use(self, index):
        if index < len(self.hand):
            played_card = self.hand[index]

            if self.energy < played_card.energy:
                print("You don't have enough energy to use that card!")
                print(f"remaining energy: {self.energy}")
                return 0;
            else:
                # apply played_card's health buffs to the player's health
                self.health += played_card.health
                # apply played_card's defense buffs

                # apply played_card's strength buffs (how does this one work?)
                self.strength += played_card.strength_buff
                # remove energy from player based on card's energy
                self.energy -= played_card.energy
                # let the user know what the card they just played did.
                played_card.print_effects()
                # pop the card from your hand, add it to the front of discard pile
                self.discard_pile.insert(0, self.hand.pop(index))
                # return the damage
                if played_card.damage > 0:
                    return played_card.damage + self.strength
                else:
                    return played_card.damage

        else:
            print("That card doesn't exist. It might've been used up or you might've put in the wrong number")
        # I'd like to give the player a list of cards they can use, but it doesn't work if we return a value

    # gives player the option to end their turn early
    def end_turn(self):
        print("You ended your turn")
        # resets the energy back to default, we don't want our player farming energy after all
        self.energy = 3
        # we need to discard all cards in the hand
        while len(self.hand) > 0:
            self.discard_pile.insert(0, self.hand.pop(0))


    # prints out the curent hand and what each card does. Also shows what you'd enter to play a card.
    def current_hand(self):

        index = 0
        for item in self.hand:
            print(f"{index}. {item.description}")
            index += 1

    # prints player's current health
    def get_current_health(self):
        print(f"Current health is {self.health}")

    # allows the player to make their decisions during their turn
    def my_turn(self, enemy):
        # player draws their hand
        self.draw()
        # show the player their hand
        self.current_hand()

        # allows for the player to do everything they need to
        while len(self.hand) > 0 and enemy.health > 0:

            choice = input('> ')

            val = 1000
            try:
                val = int(choice)
            except ValueError:
                pass

            if val < len(self.hand):
                enemy.lower_health(self.use(val))
            elif "hand" in choice:
                self.current_hand()
            elif "health" in choice:
                self.get_current_health()
            elif "end" in choice:
                # also makes the player discard all cards in hand, so it should end the loop
                self.end_turn()
            elif "energy" in choice:
                print(f"You have {self.energy} energy remaining")
            else:
                print("couldn't understand that.")


    # potential add_item function to add an item to our dict inventory

    # shuffles the list (pile) we sent in
    def shuffle_pile(self, pile):
        random.shuffle(pile)

    # returns all cards to the draw pile and shuffles them.
    def reset_piles(self):

        while len(self.discard_pile) > 0:
            self.draw_pile.append(self.discard_pile.pop(0))
        while len(self.hand) > 0:
            self.draw_pile.append(self.hand.pop(0))

        self.shuffle_pile(self.draw_pile)


class Enemy(Entity):

    # overrides __init__ but we can specify the strength and health of them, inherits lower_health, attack
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    # my_turn function, which will determine how the enemy acts. By default, they'll simply attack
    def my_turn(self, player):
        player.lower_health(self.attack())


# more enemy classes will override Enemy's my_turn to do specific things on specific turns
# for instance, maybe we'll have a goblin that, during their turn, has a chance to try and steal a card from you
