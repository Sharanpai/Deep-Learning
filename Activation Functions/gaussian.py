class Gaussian():
	def __call__(self,x):
		return np.exp(np.square(-x))

	def gradient(self,x):
		retrun -2*x*np.exp(np.square(-x))