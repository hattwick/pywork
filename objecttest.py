# Example for slope computation using objects

class Line(object):

	def __init__(self,coordinate1,coordinate2):
		self.coor1 = coordinate1
		self.coor2 = coordinate2

	def distance(self):
		x1, y1 = self.coor1
		x2, y2 = self.coor2
		return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

	def slope(self):
		x1, y1 = self.coor1
		x2, y2 = self.coor2
		return float((y2-y1))/(x2-x1)


# Test values

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print (li.distance())