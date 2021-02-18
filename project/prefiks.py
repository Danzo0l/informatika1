def tesking():
	class Pre:
		"""docstring for Pre"""
		def __init__(self, operation, par1, par2):
			super(Pre, self).__init__()
			self.operation = operation
			self.par1 = par1
			self.par2 = par2
	
		def operating(self):
			''' Calculate 2 elements of tree'''
			if self.operation == '+':
				return int(self.par1) + int(self.par2)
			elif self.operation == '-':
				return int(self.par1) - int(self.par2)
			elif self.operation == '/':
				return int(self.par1) / int(self.par2)
			elif self.operation == '*':
				return int(self.par1) * int(self.par2)
	
	
	def prog():
		print('Task 3')
		result = 0
		inp = input('   Input ')
		mas = []#['-','-','*','+',4,5,6,8,2]
		for i in inp:
			mas.append(i)
		gag = []
		for i in range(((len(mas)-3)//2)+1):
			gag.append( Pre(mas[i],mas[i*2+1],mas[i*2+2]))
			#print(gag[i].operation, gag[i].par1, gag[i].par2)
		#print()
		for i in range(len(gag)):
			for j in range(len(gag)):
				if gag[len(gag)-i-1].operation == gag[j].par1:
					gag[j].par1 = gag[len(gag)-i-1].operating()
				elif gag[len(gag)-i-1].operation == gag[j].par2:
					gag[j].par2 = gag[len(gag)-i-1].operating()
	
			#print(gag[i].operation, gag[i].par1, gag[i].par2)
	
	
		print('   Output ',gag[0].operating())
	
	
