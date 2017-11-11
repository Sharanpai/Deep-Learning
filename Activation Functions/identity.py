class Identity():
	def __call__(self, x):
        return (x)

    def gradient(self, x):
        return 1