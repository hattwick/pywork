# Quicktest working
# Test snippet to see value of mana

mana = 0


def increaser(x):
	y = x + 3
	print(y)
	return(y)

print("Mana at start:", format(mana))
newmana = increaser(mana)
print("Mana after increaser function:", format(newmana))
