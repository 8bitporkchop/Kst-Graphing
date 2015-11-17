from pykst import Client

class Graphing(Client):
	def __init__(self):
		#Initates class with pykst library
		Client.__init__(self)
		self.clear()
	def create_vector(self,start,end):
		#Creates a Vector with range (Start - End)
		#Vector filled with intermediate points for smooth curve
		Range = end - start
		return self.new_generated_vector(start, end, Range*500)

	def show_plot(self):
		#plots given function on kst
		v1 = self.create_vector(0,5)
		e1 = self.new_equation(v1, "cos(e^x)")
		c1 = self.new_curve(e1.x(), e1.y())
		p1 = self.new_plot()
		p1.add(c1)

k = Graphing()

k.show_plot()
#Hi Github
#Asafsilman@gmail.com