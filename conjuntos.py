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






		 	
				

