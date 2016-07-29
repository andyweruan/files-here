'''Monster game.'''
import random

class Player(object):
    def __init__(self, team):
        self.team = team
        self.monsters = []

    def catch(self, monster):
        my_guess = random.randint(0, len(self.monsters) + 1)
        monster_guess = random.randint(0, monster.level)
        print 'You guessed {}, monster guessed {}'.format(my_guess, monster_guess)
        if my_guess >= monster_guess:
            print 'You caught {}'.format(monster.name)
            self.monsters.append(monster)
        else:
            print 'You did not catch {}'.format(monster.name)
    def dex(self):
        for monster in self.monsters:
            print '{}: Level {}'.format(
                monster.name, monster.level
            )

class Monster(object):
    def __init__(self, new_name, level):
        self.name = new_name
        self.level = level

monster_guide = {
    'Digimon': 2,
    'Splashtoise': 300,
    'Tyrex': 301,
    'Springy': 42,
    'Squirtle': 75,
    'LapBottom': 0,
    'Zappy': 47,
    'Artsycone': 9,
}

def round(player):
    #choose a random monster.
    monster_name = random.choice(monster_guide.key())
    monster_level = monster_guide[monster_name]
    new_monster = Monster(monster_name, monster_level)
    print 'A wild {} appears!'.format(monster_name)
    #have the player try to catch the monster.
    player.catch(new_monster)
    #

monster1 = Monster('Plantosaur', 1)
monster2 = Monster('Firezard', 3)
print monster1.name


player = Player('Blue')
print player.monsters

player.catch(monster1

round(player)
