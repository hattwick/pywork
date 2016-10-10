from random import shuffle
from .moves import *

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend(("2","2","2","2","2","2","3","3","3","3","3","3","4","4","4","4","5","5","6"))

class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.blockers = []
        self.lands = []
        self.dpile = []
        self.deck = Deck

    def draw(self):
        x = self.deck.pop()
        self.hand.append(x)

p1 = player('P1')
p2 = player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1

def prompt():
    choice = raw_input("It's your turn. What will you do? \n LAND SUMMON ATTACK DONE\n")
    if choice.upper() == "LAND":
        playland()
    elif choice.upper() == "SUMMON":
        summon()
    elif choice.upper() == "ATTACK":
        attack()
    elif choice.upper() == "DONE":
        print "Turn End.\n Opponent's Turn"
        p1.blockers = list(p1.field)
        opturn()

    elif choice.upper() == "QUIT":
        exit()

    else:
        print "That's not even a thing"
        prompt()

def whoblocks():
    choice = raw_input("Will you block? Y or N\n")
    if choice.upper() == "Y":
        print p1.blockers
        y = raw_input("Who will you block with?\n")
        if y in p1.blockers:
            if y > ms[x]:
                z = p2.field.index(ms[x])
                c = p2.field.pop(z)
                p2.dpile.append(c)
                print "OP's ", ms[x], " was destroyed"
            elif ms[x] > y:
                z = p1.field.index(y)
                c = p1.field.pop(z)
                p1.dpile.append(c)
                print "Your ", y, " was destroyed"
            else:
                z = p2.field.index(ms[x])
                c = p2.field.pop(z)
                p2.dpile.append(c)
                h = p1.field.index(y)
                g = p1.field.pop(h)
                p1.dpile.append(g)
                print "It's a draw, both creatures were destroyed"

        elif y in p1.field:
            print "You can't block with that"
            whoblocks()
        else:
            print "That's not even a thing"
            whoblocks()
    elif choice.upper() == "N":
        p1.life = p1.life - int(ms[x])
        print "LP: ", p1.life


    else:
        print "That's not even a thing"
        whoblocks()

def opland():
    x = 0
    while x < len(p1.hand):
        if p2.hand[x] == "l":
            print "x: ", x
            y = p2.hand.pop(x)
            p2.lands.append(y)
            opmana = len(p2.lands)
            print "OP has ", opmana, " lands"
            break
        else:
            x+=1
    opsummon()

def opsummon():
    print "in summon phase test"
    ms = p2.field
    global ms
    mhand = [x for x in p2.hand if x != "l"]
    opmana = len(p2.lands)
    rhand = sorted(mhand, reverse=True)
    x = 0
    while x < len(rhand) and opmana > 0:
        if int(rhand[x]) <= opmana:
            a = rhand[x]
            b = p2.hand.index(a)
            c = p2.hand.pop(b)
            rhand.pop(x)
            print "OP summons ", a
            p2.field.append(c)
            opmana = opmana - int(a)
        else:
            x = x + 1

    print "OP's field: ", p2.field
    if not ms:
        print "End of OP's turn"
        plturn()
    else:
        print "Attack Phase"
        x = 0
        while x < len(ms):
            print "A", ms[x], "is attacking you."
            if not p1.blockers:
                p1.life = p1.life - int(ms[x])
                print "LP: ", p1.life
                x = x + 1
            else:
                whoblocks()
                x = x + 1

def plturn():
    global mana
    mana = len(p1.lands)
    p1.blockers = list(p1.field)
    p1.draw()
    print "Hand: ", p1.hand
    print "Field: ", p1.field
    print "Mana: ", mana

    prompt()

def opturn():
    print "Opponent's Turn"
    p2.draw()
    print "OP has ", len(p2.hand), " cards in hand"
    opland()


plturn()