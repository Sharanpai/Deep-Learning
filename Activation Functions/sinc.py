class SinC():
	def __call__(self,x):
		if x == 0:
			return 1
		else:
			return np.sinc(x)

	def gradient(self,x):
		if x == 0:
			return 0
		else:
			return np.cosc(x) - np.sinc(x)/x