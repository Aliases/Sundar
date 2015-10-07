

class Parent():
	def __init__(self,a,b):
		print("Parent constructor called")
		self.last_name=a
		self.eye_color= b

	def show_info(self):
		print("last name: "+self.last_name)

class Child (Parent):
	def __init__(self,a,b,c):
		print("Child constructor called")
		Parent.__init__(self,a,b)
		self.no_of_toys=c

	def show_info(self):
		print("no of toys "+str(self.no_of_toys))

billy= Parent("Cyrus", "blue")
#print(billy.last_name)

Miley=Child("Cyrus","blue",5)
#print(Miley.last_name)
#print(Miley.no_of_toys)
Miley.show_info()
