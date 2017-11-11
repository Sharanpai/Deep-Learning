class Bent():
	def __call__(self,x):
		return (np.sqrt(np.square(x) + 1 ) - 1)/ 2 + x

	def gradient(self,x):
		return x / (2*(np.sqrt(np.square(x) + 1))) + 1