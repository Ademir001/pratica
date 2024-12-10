class rodar:
	def __init__(self,marca,modelo):
		self.marca = marca
		self.modelo = modelo
	def move(self):
		print("autobostes rodar")
class carro(rodar):
	pass

class planador(rodar):
	def move(self):
		print("vamos voar")
class barco(rodar):
	def move(self):
		print("navegar vamo navegar")
        
car1 = carro("Ford", "Mustang") #Create a Car object
boat1 = barco("Ibiza", "Touring 20") #Create a Boat object
plane1 = planador("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
	print(x.marca)
	print(x.modelo)
	x.move()
    