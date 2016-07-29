import string
num = '(415)734-7203'
#num = raw_input('Input Phone Number:    ')
'''
all = string.maketrans('','')
nodigs=all.translate(all, string.digits)
dig = num.translate(all, nodigs)
'''


dig = 0
for val in num :
    if (val.isdigit()) :
        dig += 1

if(len(num) == 13 and dig == 10 and num[0] == '(' and num[4] == ')' and num[8] == '-'):
    print 'Number formatted correctly'
else:
    print 'Number not formatted corectly'
