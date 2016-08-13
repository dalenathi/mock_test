class NameGetter(object):
""" adding doc string to this is cool"""
""" see if this can be committed by me """ 
	def get_name(self):
		self.name = raw_input('enter your name: ')

	def greet(self):
		print 'Hello there' , self.name

	def run(self):
		self.get_name()
		self.greet()

""" different comment on local """ 

if __name__ == '__main__':
	m = NameGetter()
	m.run()
