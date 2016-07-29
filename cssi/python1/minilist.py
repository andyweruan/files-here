some_numbers =[2, 52, 19, 46, 1000]
for i in range(0, len(some_numbers)):
    some_numbers[i] = (some_numbers[i] + 10) / 2
print some_numbers

presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams"]
presidents.reverse()
for i in range(0, len(presidents)):
    print presidents[i]

presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams"]
for i in range(0, len(presidents)):
    presidents[i].reverse()
    print presidents[i]


for i in range (10, 0, -1):
    print str(i) + " bottles of milk on the wall"

# \ <-- this backslash will escape it and cancel it because ""Andy"" does not work or you can also do '"Andy"'
