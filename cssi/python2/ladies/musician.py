class Musician(object):
    '''This is a class for Musicians.'''

    #constructor - The method to create an instance from a class.
    def __init__(self, name, gender, genre, mtype):
        #The name of the Muscian
        #properties of the class
        self.name = name
        #The gender of the Muscian
        self.gender = gender
        #The genre of the Muscian
        self.genre = genre
        #The type of the Muscian
        self.type = mtype

    def print_description(self):
        print self.get_description()


    def get_description(self):
        return '{} is a {} {} {}.'.format(
            self.name, self.gender, self.genre, self.type
        )
ts = Musician('Taylor Swift', 'female', 'pop', 'singer')
by = Musician('Beyonce', 'female', 'R&B', 'singer')

#print ts.name
#print by.gender
#print ts.type
#ts.print_description()
#by.print_description()
#print type(ts)
#print type(by)
#print dir(ts)
#print help(ts.__module__)


#If the quote under it is something words, you can get it with Musician.words
