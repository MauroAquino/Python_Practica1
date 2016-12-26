#Compatible Python 3

class Conjunto:

	#Constructor, genera un diccionario vacio y un contador como atributos de instancia
	def __init__(self):
		self._conj = []
		

	#Constructor, genera un diccionario vacio y un contador como atributos de instancia
	def __init__(self,*param):
		
		self._conj = []

		for value in param:
			self.agregar_valor(value)	

	def __str__(self):
		
		print ("Esta clase emula los sets"+self)

	#Metodo que agrega un valor a la coleccion del diccionario validando que no sea repetida	
	def agregar_valor(self,par):
		
		for value in self._conj:
			if value == par:
				return
			else:
				continue
		
		self._conj.append(par)

	#Metodo que remueve el valor del diccionario
	def remover_elemento(self,par):

		self._conj.remove(par)

	#Metodo de clase que resta el segundo conjunto al primero por medio de una variable de validacion
	@classmethod			
	def diferencia_conjuntos(cls,seta,setb):
		
		dic_retorno = Conjunto()
		validacion = 1

		for value in seta._conj:
			validacion = 1
			for value_dos in setb._conj:
				if value == value_dos:
					validacion=0			
			if validacion == 0:
				continue
			else:
				dic_retorno.agregar_valor(value)


		return dic_retorno				

	#Metodo de clase que compara el segundo conjunto al primero creando un tercer conjunto
	@classmethod			
	def interseccion_conjuntos(cls,seta,setb):
		
		dic_retorno = Conjunto()

		for value in seta._conj:
			for value_dos in setb._conj:
				if value == value_dos:
					dic_retorno.agregar_valor(value)										
		return dic_retorno		

	#Metodo de clase que valida los valores del segundo conjunto con el primero e imprime si esta incluido	
	@classmethod			
	def validar_inclusion(cls,seta,setb):
		
		dic_retorno = Conjunto()
		validacion=1

		for value in seta._conj:
			validacion = 1
			for value_dos in setb._conj:
				if value == value_dos:
					validacion=0				
			if validacion == 1:
				continue


		if validacion == 1:
			print("El segundo set esta incluido en el primero")
		else:
		 	print("El segundo set no esta inlcuido en el primero")

	#Metodo de clase que crea un tercer conjunto con todos los elementos del primero y segundo	 	
	@classmethod			
	def producto_cartesiano(cls,seta,setb):
		
		import itertools
		for i in itertools.product(seta._conj,setb._conj): 
			print (i)


	#Metodo de clase que crea un tercer conjunto solo con los exclusivos	
	@classmethod			
	def diferencia_simetrica_conjuntos(cls,seta,setb):
		
		dic_retorno = Conjunto()
		validacion = 1

		for value in seta._conj:
			validacion = 1
			for value_dos in setb._conj:
				if value == value_dos:
					validacion=0			
			if validacion == 0:
				continue
			else:
				dic_retorno.agregar_valor(value)

		for value in setb._conj:
			validacion = 1
			for value_dos in seta._conj:
				if value == value_dos:
					validacion=0			
			if validacion == 0:
				continue
			else:
				dic_retorno.agregar_valor(value)		


		return dic_retorno	

	#Metodo de clase que crea un tercer conjunto potencia	 
	def conjunto_potencia(self):
		
		n = len(self._conj)
		for x in range(1 << n):
			print([self._conj[y] for y in range(n) if (x & (1 << y))])

class Matriz:

	def __init__(self,lista=[]):
		
		self._list = lista


	@classmethod
	def suma_matrices(cls,m1,m2):

		return Matriz.suma_resta(m1,m2,"suma")
	
	@classmethod
	def resta_matrices(cls,m1,m2):

		return Matriz.suma_resta(m1,m2,"resta")	
			

	@classmethod		
	def suma_resta(cls,m1,m2,que_hacer):
		
		if len(m1._list) == len(m2._list) and len(m1._list[0]) == len(m1._list[0]):

			if (que_hacer == "suma"):
				return Matriz([[m1._list[x][y]+m2._list[x][y] for y in range (len(m2._list[0]))] for x in range(len(m2._list))])
			else:
				return Matriz([[m1._list[x][y]-m2._list[x][y] for y in range (len(m2._list[0]))] for x in range(len(m2._list))])

		else:

			 return "Error de dimensiones matriz"		

	@classmethod
	def multiplicar_escalar(cls,m1,esc):

		return Matriz([[esc*m1._list[x][y] for y in range(len(m1._list[0]))]for x in range(len(m1._list))])	
			
	@classmethod
	def multiplicar_matrices(cls,m1,m2):

		return [[sum(a*b for a,b in zip(m1_list_row,m2_list_col)) for m2_list_col in zip(*m2._list)] for m1_list_row in m1._list]

	@classmethod
	def trasponer_matrices(cls,m1):

		return Matriz([[ m1._list[x][y] for x in range(len(m1._list))] for y in range(len(m1._list[0]))])

	def retornar_filas(self,*args):
		
		set_args=set(args)

		for x in range(len(set_args)):
			print(str(self._list[args[x]]))

	def retornar_columnas(self,*args):
		
		string = "["

		valor = list(set(args))

		for y in range(len(valor)):
			for x in range(len(self._list)):
				
				if x>0:
					string=string+","
				
				string=string + str(self._list[x][valor[y]])

			string = string + "]"
		
			if y != len(valor)-1:
				string = string + ",["	
					
		print(string)	
	
	def mostrar_matriz(self):

		for x in range(len(self._list)):
				print(self._list[x])	
	
	def extracto_matriz(self,ref,f,c):

		if ref+c < len(m3._list):
			return Matriz([[self._list[x][ref+y] for y in range(c)]for x in range(f)])

			






		 	
				

