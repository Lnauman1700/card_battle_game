
import entities
import rooms

user = entities.Player(input('What is your name?: '))
map = rooms.Map(user)
map.run()
