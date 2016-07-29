my_list = range(1, 10)

my_juice = ['green', 'ruby', 'ginger']

my_number = [1, 2, 3]

my_juice.append('carrot')

del my_juice[2]

my_juice[1:2] #only ruby

my_juice.extend(my_number)
#it combines the two list even tho it is two different types

is_in = 'apple' in my_juice  #false because it is not in the list

my_juice.sort()

my_juice.remove('carrot')

dir(0) #dir look at the end because you can look at the methods at the end
#help(..) look at how it can help u

name = 'Jenny Lo'
name.replace('Jenny', 'Nicole').replace('Lo', 'Griffith') #this is call chaining because we keep doing the things, also returns a str


new_new_name = 'Andy Ruan               '
new_new_name.strip() #remove the empty spaces

firstn = 'Andy'
lastn = 'Ruan'
print '%s %s' % (firtn, lastn)  #expect 'Andy Ruan'

print '{} {}'.format(lastn, firstn)

print '{fn} {ln}'.format(ln = lastn,fn = firstn)


my_list = list(name) #This makes name the string into a list
#A string is really treated as a array of characters
