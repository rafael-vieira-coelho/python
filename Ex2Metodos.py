class D(object): 
	multiplier = 2

	@classmethod 
	def f(cls, x):
		return cls.multiplier * x

	@staticmethod 
	def g(name):
		print("Hello, %s" % name)

if __name__ == '__main__':
	print(D.f) # <bound method type.f of <class '__main__.D'>> D.f(12)
	D.g # <function D.g at ...>
	D.g("world") # Hello, world

	d = D()
	d.multiplier = 1337
	print((D.multiplier, d.multiplier))
	# (2, 1337)
	print(d.f) # <bound method D.f of <class '__main__.D'>> d.f(10)
