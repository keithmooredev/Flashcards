from sys import argv

script, filename = argv

cards = open(filename, 'r')

print "================================================================================="
print "Welcome to the flashcards study aid. Type 'quit' at any time to exit the program."
print "================================================================================="

for line in cards:
    card = line.split('\t')
    print "\n%s" %card[1]
    wrong = True
    while wrong:
        ans = raw_input("What is the term being defined? (type 'give' to show the answer) > ")
        if ans.lower() == "give":
            print "The correct answer was %s." %card[0].upper()
            wrong = False
        elif ans.lower() == card[0]:
            print "%s is correct." %ans.upper()
            wrong = False
        else:
            print "%s is incorrect. Try again." %ans.upper()