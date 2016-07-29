text = '''
Success is counted sweetest
By those who ne'er succeed.
To comprehend a nectar
Requires sorest need.

Not one of all the purple Host
Who took the Flag today
Can tell the definition
So clear of victory

As he defeated - dying -
On whose forbidden ear
The distant strains of triumph
Burst agonized and clear!
'''
words = text.lower().split()

counts = {}

for word in words:
    print word
    if word in counts:
        #add a count to the value.
        counts[word] += 1
    else:
        #add the word to counts.
        counts[word] = 1

print counts
