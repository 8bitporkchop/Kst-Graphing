import pykst as kst
from pykst import Client

class Graphing(Client):
	def __init__(self):
		#Initates class with pykst library
		try:
			Client.__init__(self)
		except WindowsError:
			raise Exception('Make sure KST is running.')

		#These libraries will hold all variables and curves to plot later
		self.list_of_sources = {}
		self.list_of_variables = {}
		self.list_of_curves = []

		#sets up a clean screen
		self.clear()

	def new_source(self,tag,file_location):
		#Sets the Delimiter for the csv file
		self.set_datasource_option("Column Delimiter", "," ,file_location)
		self.set_datasource_option("Column Type", 2, file_location)
		#Sets up the date/time format
		self.set_datasource_option("Index", "Column 1", file_location)
		self.set_datasource_option("Default INDEX Interpretation", 4, file_location)
		self.set_datasource_option("ASCII Time format", 'hh:mm:ss',file_location)
		#Sets update format (Change detected has some bugs)
		self.set_datasource_option("updateType",0,file_location)

		#adds source to library 
		try:
			assert tag == str(tag)
			self.list_of_sources[tag] = file_location
		except AssertionError:
			raise Exception("Invalid Tag")

	def new_variable(self,field,reference,tag = '',start = -1, num_frames = 100, skip = 0, boxcarFirst = False, name = ''):
		if tag == '':
			tag = str(field) #giving a dummy tag if none provided

		source = self.list_of_sources[reference] #taking the source object from list of sources

		#sets up the vector
		temp_variable = self.new_data_vector(source ,field, start, num_frames, skip, boxcarFirst)
		temp_variable.set_name(name)

		#adds vector to library
		try:
			self.list_of_variables[tag] = temp_variable
		except:
			raise Exception('Error adding variable to list, try add a unique tag')

	def create_curve(self,x_variable,y_variable,colour = 'Blue'):
		#sets up the curve
		temp_curve = self.new_curve(x_variable,y_variable)
		#fancy settings
		temp_curve.set_color(colour)
		temp_curve.set_line_width(2)
		temp_curve.set_has_points()
		temp_curve.set_point_type(3)
		temp_curve.set_point_size(8)
		#adds curve to library
		self.list_of_curves.append( temp_curve )

	def show_single_plot(self,name):
		plot = self.new_plot()
		plot.set_x_no_spike()
		plot.add(self.list_of_curves[name])

	def show_all_plots_together(self):
		#shows all curves on a single graph
		plot = self.new_plot()
		for i in self.list_of_curves:
			plot.set_x_no_spike()
			plot.add(i)

	def show_all_plots_alone(self):
		#shows all curves on individual graphs
		for i in self.list_of_curves:
			plot = self.new_plot()
			plot.set_x_no_spike()
			plot.add(i)


k = Graphing()

k.new_source('file1',"C:/Users/Asaf/Desktop/Python/Work/Graphing/Kst-Graphing/Test1.csv")
k.new_source('file2',"C:/Users/Asaf/Desktop/Python/Work/Graphing/Kst-Graphing/Test2.csv")
#k.new_source('file3',"C:/Users/Asaf/Desktop/Python/Work/Graphing/Kst-Graphing/Test3.csv")

k.new_variable("Column 1",'file1','file1x', name = 'TimeStamp')
k.new_variable("Column 2",'file1','file1y',name = 'Time (Milliseconds/10)')

k.new_variable("Column 1",'file2','file2x', name = 'TimeStamp')
k.new_variable("Column 2",'file2','file2y', name = 'Time (Milliseconds/10)')

#k.new_variable("Column 1",'file3','file3x', name = 'TimeStamp')
#k.new_variable("Column 2",'file3','file3y', name = 'Time (Milliseconds/10)')

k.create_curve( k.list_of_variables['file1x'] , k.list_of_variables['file1y'] )
k.create_curve( k.list_of_variables['file2x'] , k.list_of_variables['file2y'] ,colour = 'red')
#k.create_curve( k.list_of_variables['file3x'] , k.list_of_variables['file3y'] ,colour = 'green')

k.show_all_plots_alone()