class Spaceship(object):
    """docstring for """
    def __init__(self, name, planet, nPeople):
        self.name = name
        self.planet = planet
        self.npeople = nPeople

    def fly(self, newplanet):
        self.planet = newplanet
        print '{} flew to {} with {} members on deck.'.format(
            self.name, self.planet, self.npeople
        )

    def dropoff(self):
        self.npeople -= 1
        print '{} dropped someone off and now has {} members.'.format(
            self.name, self.npeople
        )

a = Spaceship('Joe', 'Earth', 5)
b = Spaceship('Lalw', 'Mars', 2)

a.fly('Pluto')
a.dropoff()
