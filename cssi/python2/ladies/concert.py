#import musician; #importing a file i.e module.
from musician import Musician      #Musician
class Concert(object):
    '''This is a class for Concert.'''

    def __init__(self, instruments, size, seats, celebrities):
        self.instruments = instruments
        self.size = size
        self.seats = seats
        self.celebrities = celebrities

    def get_promotion_text(self):
        musician_text = ''
        for musician in self.celebrities:
            musician.text = musician.name + ' ' + musician_text
        self.celebrities
        text = ('Student discount alert! Shoreline {} Concert will have {} seats with ' +
        'capacity of {}, permforming by {}').format(
            ' '.join(self.instruments), len(seats), self.size, musician_text
        )
        return text

instruments = ['Triangle', 'Guitar']
seats = ['VIP', 'Student']
ts = Musician('Taylor Swift', 'female', 'pop', 'singer')
by = Musician('Beyonce', 'female', 'R&B', 'singer')

s_concert = Concert(instruments, 300, seats, [ts, by])
print s_concert.get_promotion_text()
