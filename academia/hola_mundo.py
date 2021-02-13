class curso:

	def __init__(self, titulo, descripcion,precio):
		self.titulo = titulo
		self.descripcion = descripcion
		self.precio = precio

	def NombrePrecio(self):
		print('Este curso se llama: ' + self.titulo + ' y tu aprendes: ' + self.descripcion + ' y tiene un precio de: ' + str(self.precio))

	def Descuento(self, porcentaje):
		self.precio = self.precio * porcentaje / 100 

	def __str__(self):
		return self.titulo
		
curso_enero = curso('rosas','Cultivo de rosas',12.34)

print(curso_enero)

curso_enero.Descuento(10)

# print(curso_enero.NombrePrecio())		

print(curso_enero.titulo)