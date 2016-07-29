my_juice = ['green', 'rubby', 'carrot']
whole_food_price = [9.99, 15.0, 5.0]
print '{} juice costs ${}'.format(my_juice[0], whole_food_price[0])

juice_dic = {}
juice_dic = {'green': 9.99, 'rubby': 15.0, 'carrot': 5.0}

juice_dic['green'] = 2.99
print juice_dic

my_juice.append('orange') #making new thing into the dictionary
juice_dic['orange'] = 1.99
print juice_dic

is_in = 'apple' in my_juice

'apple' in juice_dic #do the same for string, list, and dictionary

1.99 in juice_dic.values() #can check if key or values exist in your dictionary

print '{} juice costs ${}'.format('orange', juice_dic['orange'])

for juice in juice_dic:
    print '{} juice costs ${}'.format(juice, juice_dic[juice])



    city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
    'population' : 8337000,
    'website' : "http://www.nyc.gov"
    },
    'los_angeles' : { 'mayor' : "Eric Garcetti",
    'population' : 3884307,
    'website' : "http://www.lacity.org"
    },
    'miami' : { 'mayor' : "Tomás Regalado",
    'population' : 419777,
    'website' : "http://www.miamigov.com"
    },
    'chicago' : { 'mayor' : "Rahm Emanuel",
    'population' : 2695598,
    'website' : "http://www.cityofchicago.org/"
    }
    }

def print_name():
    print 'Andy Ruan'

print_name()


def print_name(name):
    print 'Hello, ' + name + ' Are you sleepy?'
    print 'Hello, %s . Are you sleey?' % (name)
    print 'Hello, {}.Are you sleepy?'.formant(name)
    
    sentence = print_name('Andy')
