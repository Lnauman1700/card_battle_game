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

    def attack(self):
        print(f"You did {self.strength + self.item_mod} damage")
        return self.strength + self.item_mod

    # potential add_item function to add an item to our dict inventory


class Enemy(Entity):

    # overrides __init__ but we can specify the strength and health of them, inherits lower_health, attack
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

# in each room, there should be a while loop that loops till one entity is dead
# each iteration of the loop, the player goes first and chooses what to do via an input()
# dealing damage is enemy.lose_health(player.attack())
# if the player dies in combat, then return "death" and send them to the death room

# sample loop of combat
player = Player("Phil")
enemy = Enemy("James", 8, 2)

while player.health > 0 and enemy.health > 0:

    print("You can attack! to attack, just say attack")
    choice = input('> ')

    if "attack" in choice:
        enemy.lower_health(player.attack())
    else:
        # sample for if you chose something else, like running away
        print("You ran!")

    # here the enemy can be influenced depending on what the situation looks like:
    if enemy.health < 5:
        print("Wait, I'll stop fighting! Put your weapon down!")
        decision = input('> ')
        if "stop" in decision:
            print("You left yourself open!")
            player.lower_health(enemy.attack())
            player.lower_health(enemy.attack())
        else:
            print("You managed to get an extra hit in while he was trying to surrender!")
            enemy.lower_health(player.attack())

    else:
        player.lower_health(enemy.attack())

if player.health <= 0:
    # ideally, this'd be a return statement instead of a print, which would influence the next room.
    print("You died")
else:
    print("You won! now let's resume where we left off")
