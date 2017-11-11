class Softsign():
	def __call__(self,x):
		return x / (1 + np.absolute(x))

	def gradient(self,x):
		return 1 / (np.square((1 + np.absolute(x))))