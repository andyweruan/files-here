food = (raw_input('What\'s your favorite food?  ')).upper()
outfood = ''
for letter in food:
    if(letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        outfood += letter * 5
    outfood += letter
print outfood
