class Entity(object):

    # init function which takes self, name

    # lower_health function which takes self, damage and lowers health by damage

    # attack method which takes self, returns number = self.strength + any item modifier. may require another param of item


class Player(Entity):

    # dictionary (?) with all items currently in posession.

    # inherits __init__, lower_health, and attack (attack may need changed to suit item use)

    # potential add_item function to add an item to our dict inventory


class Enemy(Entity):

    # inherits __init__, lower_health, attack

# in each room, there should be a while loop that loops till one entity is dead
# each iteration of the loop, the player goes first and chooses what to do via an input()
# dealing damage is enemy.lose_health(player.attack())
# if the player dies in combat, then return "death" and send them to the death room
