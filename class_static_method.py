class Myclass:
	def method(self):
		self.instance = 'instance method called'
		return (self.instance)

	@classmethod
	def classmethod(cls):

		cls.mtd = 'class method called'
		return cls.mtd

	@staticmethod
	def staticmethod():
		static = 'static method called'
		return static


#call instance of class 
mon_class = Myclass()
print(mon_class.method())

print('#---------------------------#')
print(Myclass.classmethod())

print('#---------------------------#')
print(Myclass.staticmethod())
