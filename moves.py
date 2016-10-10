# Library of gametest moves for Nick Hattwick project

def playland():
    x = 0
    while x < len(p1.hand):
        if p1.hand[x] == "l":
            print "x: ", x
            y = p1.hand.pop(x)
            p1.lands.append(y)
            mana = len(p1.lands)
            print "Mana: ", mana
            prompt()
        else:
            x+=1
    print "No lands in hand"
    prompt()

def summon():
    mhand = [x for x in p1.hand if x != "l"]
    mana = len(p1.lands)
    print "Monsters: ", mhand
    mchoice = raw_input("Which monster would you like to summon?\n")
    if int(mchoice) <= mana:
        y = p1.hand.index(mchoice)
        z = p1.hand.pop(y)
        p1.field.append(z)
        p1.blockers.append(z)
        print p1.field
        prompt()
    elif mchoice in p1.hand:
        print "You can only play monsters less than or equal to your mana"
        prompt()
    else:
        print "That's not a card in your hand"
        prompt()

def block():
    print "Block-test: Success"

def attack():
    p1.blockers = list(p1.field)
    print p1.blockers
    if not p1.blockers:
        print "there's nothing there"
        opturn()
    else:
        x = raw_input("Which creature would you like to attack with?\n")
        if str(x) in p1.blockers:
            block()
            y = p1.blockers.index(x)
            p1.blockers = p1.blockers.pop(y)
            secatkchoice()
        elif x in p1.field:
            print "You can't attack with that"
            prompt()
        elif not p1.blockers:
            print "There's nothing there"
            prompt()
        else:
            print "That's not even a thing"
            prompt()

def secatkchoice():
    choice = raw_input("Would you like to attack with another monster?\nY or N\n")
    if choice.upper() == "Y":
        attack()
    elif choice.upper() == "N":
        opturn()
    else:
        print "That's not a thing..."
        secatkchoice()

def main():
	print('Main from Moves has been executed.  How did that happen?')

if __name__ == "__main__": main()