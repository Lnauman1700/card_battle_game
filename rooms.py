
import entities
import cards
# each room has a battle in it, what the battle is depends on how deep you go

# each room stems from a room class
class Room(object):

    # room class probably has a method which plays a battle. Takes param of enemy which is fought
    def battle(self, enemy, player):

        while player.health > 0 and enemy.health > 0:

            player.my_turn(enemy)
            # some sort of variation on enemy attack
            player.lower_health(enemy.attack())

        if player.health <= 0:
            print("You died")
        else:
            print("You win!")

    # each room returns a string which should represent the next room
jimbo = entities.Player("Jimbo")
Room().battle(entities.Enemy('Bill', 16, 4), jimbo)
print(jimbo.health)
