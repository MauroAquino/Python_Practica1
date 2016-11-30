#Compatible Python 3

class conjuntos:

	#Constructor, genera un diccionario vacio y un contador como atributos de instancia
	def __init__(self):
		self._conj = {}
		self._cont = 0

	#Constructor, genera un diccionario vacio y un contador como atributos de instancia
	def __init__(self,*param):
		
		self._conj = {}
		self._cont = 0

		for value in param:
			self.agregar_valor(value)	

	def __str__(self):
		
		print ("Esta clase emula los sets"+self)

	#Metodo que agrega un valor a la coleccion del diccionario validando que no sea repetida	
	def agregar_valor(self,par):
		
		for key, value in self._conj.items():
			if value == par:
				return
			else:
				continue
		
		self._conj[self._cont]=par

		self._cont+=1

	#Metodo que remueve el valor del diccionario
	def remover_elemento(self,par):

		for key, value in self._conj.items():
			if value == par:
				del self._conj[key]
				return
			else:
				continue	

	#Metodo de clase que resta el segundo conjunto al primero por medio de una variable de validacion
	@classmethod			
	def diferencia_conjuntos(cls,seta,setb):
		
		dic_retorno = conjuntos()
		validacion = 1

		for key, value in seta._conj.items():
			validacion = 1
			for key_dos, value_dos in setb._conj.items():
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
		
		dic_retorno = conjuntos()

		for key, value in seta._conj.items():
			for key_dos, value_dos in setb._conj.items():
				if value == value_dos:
					dic_retorno.agregar_valor(value)										
		return dic_retorno		

	#Metodo de clase que valida los valores del segundo conjunto con el primero e imprime si esta incluido	
	@classmethod			
	def validar_inclusion(cls,seta,setb):
		
		dic_retorno = conjuntos()
		contador=0
		validacion=1

		for key, value in seta._conj.items():
			validacion = 1
			for key_dos, value_dos in setb._conj.items():
				if value == value_dos:
					validacion=0				
			if validacion == 1:
				continue
			else:
				contador+=1

		if contador == len(setb._conj):
			print("El segundo set esta incluido en el primero")
		else:
		 	print("El segundo set no esta inlcuido en el primero")

	#Metodo de clase que crea un tercer conjunto con todos los elementos del primero y segundo	 	
	@classmethod			
	def producto_cartesiano(cls,seta,setb):
		
		dic_retorno = conjuntos()

		for key, value in seta._conj.items():
			for key_dos, value_dos in setb._conj.items():
				dic_retorno.agregar_valor(value_dos)
			dic_retorno.agregar_valor(value)	

		return dic_retorno	 	

class matriz:

	def __init__(self,f,c,*args):
		
		j=0


		self._list = [[0]*c for x in range(f)]

		if len(args)==f*c:
			
			for x in range(f):
				for y in range(c):
					self._list[x][y] = args[j]
					j+=1 
	
	@classmethod
	def suma_matrices(cls,m1,m2):

		if len(m1._list) == len(m2._list) and len(m1._list[0]) == len(m1._list[0]):

			m3 = matriz(len(m2._list),len(m2._list[0]))

			for x in range(len(m2._list)):
				for y in range(len(m2._list[0])):
					m3._list[x][y] = m1._list[x][y]+m2._list[x][y]

		return m3

	@classmethod
	def resta_matrices(cls,m1,m2):

		if len(m1._list) == len(m2._list) and len(m1._list[0]) == len(m1._list[0]):

			m3 = matriz(len(m2._list),len(m2._list[0]))

			for x in range(len(m2._list)):
				for y in range(len(m2._list[0])):
					m3._list[x][y] = m1._list[x][y]-m2._list[x][y]

		return m3							

	@classmethod
	def multiplicar_escalar(cls,m1,esc):

		m3 = matriz(len(m1._list),len(m1._list[0]))

		for x in range(len(m1._list)):
			for y in range(len(m1._list[0])):
				m3._list[x][y] = esc*m1._list[x][y]

		return m3

	@classmethod
	def multiplicar_matrices(cls,m1,m2):

		result = 0

		if(len(m1._list)==len(m2._list[0])):
			m3 = matriz(len(m1._list),len(m2._list[0]))

			for x in range(len(m1._list)):
				for j in range(len(m2._list[0])):
					for y in range(len(m1._list[0])):
						m3._list[x][j] += (m1._list[x][y]*m2._list[y][j])
				

		return m3	

	@classmethod
	def trasponer_matrices(cls,m1):

		m3 = matriz(len(m1._list[0]),len(m1._list))

		for x in range(len(m1._list)):
			for y in range(len(m1._list[0])):
					m3._list[y][x] = m1._list[x][y]

		return m3	
	
			






		 	
				

