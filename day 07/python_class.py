'''class NameOfClass(object):
	"""docstring for NameOfClass"""
	def name_of_method(self):
		things to do

class ClassName(object):
			"""docstring for ClassName"""
			def __init__(self, arg):
				super(ClassName, self).__init__()
				self.arg = arg
'''
		
class Character():
	lives = 5
	def __init__(self, name):
		self.name = name

	def punch(self,name):
		name.lives-=1

class Boss(Character):
	lives = 10			
