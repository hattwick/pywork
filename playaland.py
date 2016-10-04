from random import shuffle

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend((2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6))

class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
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

print "P1: ", p1.hand

def plturn():
    choice = raw_input("It's your turn. What will you do? \n LAND SUMMON ATTACK HELP\n")
    if choice.upper() == "LAND":
        x = 0
        while x < len(p1.hand):
            if p1.hand[x] == "l":
                print "x: ", x
                y = p1.hand.pop(x)
                p1.lands.append(y)
                break
            else:
                x+=1
    else:
        print "..."

plturn()

print p1.hand
print p1.lands