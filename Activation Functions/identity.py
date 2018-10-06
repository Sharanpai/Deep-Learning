class Identity():
	def __call__(self, x):
        return (x)

    def gradient(self, x):
	y = x+1
        return 1
