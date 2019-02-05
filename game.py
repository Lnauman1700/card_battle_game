
import entities
import cards
# in each room, there should be a while loop that loops till one entity is dead
# each iteration of the loop, the player goes first and chooses what to do via an input()
# dealing damage is enemy.lose_health(player.attack())
# if the player dies in combat, then return "death" and send them to the death room

# sample loop of combat
player = entities.Player("Phil")
enemy = entities.Enemy("James", 8, 2)


while player.health > 0 and enemy.health > 0:

    # player draws their hand
    player.draw()

    # allows for the player to do everything they need to
    while len(player.hand) > 0 and enemy.health > 0:

        choice = input('> ')

        val = 1000
        try:
            val = int(choice)
        except ValueError:
            pass

        if val < len(player.hand):
            enemy.lower_health(player.use(val))
        elif "hand" in choice:
            player.current_hand()
        elif "health" in choice:
            player.get_current_health()
        elif "end" in choice:
            # also makes the player discard all cards in hand, so it should end the loop
            player.end_turn()
        elif "energy" in choice:
            print(f"You have {player.energy} energy remaining")
        else:
            print("couldn't understand that.")

    player.lower_health(enemy.attack())

if player.health <= 0:
    print("You died")
else:
    print("You win!")
