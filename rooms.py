
import entities
import cards
# each room has a battle in it, what the battle is depends on how deep you go

# each room stems from a room class
class Room(object):

    # making multiple enemies in the future is a possibility. Would have to figure out *args for the enemy param
    # and would have to add a for loop for the enemy turns in battle()
    def __init__(self, enemy, next_room):
        self.enemy = enemy
        self.next_room = next_room

    # room class probably has a method which plays a battle. Takes param of enemy which is fought
    def battle(self, player):


        player.reset_piles()
        # battle loop, determines that the battle continues if player and enemy are both still alive
        while player.health > 0 and self.enemy.health > 0:

            # player makes their deccisions/attacks
            player.my_turn(self.enemy)
            # enemy makes their decisions/attacks
            # seems like this may be happening even after the enemy dies
            self.enemy.my_turn(player)

        # ends turn as a safety measure incase you defeated the enemy before your turn was over
        # also functions as a way to restore energy after the battle
        player.end_turn()
        if player.health <= 0:
            self.next_room = "death"
        else:
            print("You win!")

    # each room returns a string which should represent the next room

    # default, pre-battle interaction with room. By default, only describes the room
    def interact(self, player):
        print("default room")

    def get_next_room(self):
        return self.next_room

class Death(Room):

    # in this case, description simply describes that you died
    def __init__(self):
        pass

    def interact(self):
        print("You have fallen....")

class FirstRoom(Room):

    def interact(self, player):
        print("""
Your adventure is just beginning.
On the way through the town, somebody slips by you a little bit too closely
Upon further inspection, it seems like he took your wallet
You locate him, but it looks like he's not going down without a fight
        """)
        self.battle(player)
        return self.get_next_room()

class ThiefBand(Room):

    def interact(self, player):
        print("""
You proceed, your wallet now back in your hands, towards the dungeon.
You feel like you're being followed...
Soon before you enter the dungeon, it becomes apparent who you were followed by
It seems that pickpocket had friends. A band of thieves emerges
The leader presents himself, and initiates a fight!
        """)
        self.battle(player)
        return self.get_next_room()

class Dungeon(Room):

    def interact(self, player):
        print("""
Now that those bandits are taken care of, It's time to go into the dungeon!
Uh-oh. That sounds like a Dragon
Yup, it's a dragon. Time to fight.
        """)
        self.battle(player)
        return self.get_next_room()


class Map(object):

    def __init__(self, player):
        self.player = player
        self.rooms = {
            'start room': FirstRoom(entities.Enemy("Pickpocket", 14, 3), 'thief band'),
            'thief band': ThiefBand(entities.Enemy("Bandit Leader", 20, 4), 'dungeon'),
            'dungeon': Dungeon(entities.Enemy("Dragon", 30, 5), 'end'),
            'death': Death()
        }

    def run(self):

        # we should run the start room first
        next = self.rooms['start room'].interact(self.player)
        while next != 'end' and next != 'death':
            next = self.rooms[next].interact(self.player)
        if next == 'end':
            print("That's all for the game right now")
        else:
            # lets you interact with the death room
            self.rooms[next].interact()
