def LEER_NUMERO():
	notInt = False;

	while (notInt == False) :
		print()
		res = input("Introduzca el número ENTERO (Introduzca letra <E> para salir): ")
		if (res != 'E'):
			notInt = res.lstrip("-").isdigit()
			if (notInt == False) :
				print("ERROR: No ha introducido un número entero. Vuelva a introducirlo.")
			else:
				res = int(res)
		else:
			notInt = True
	return res

def EJERCICIO_PRINCIPAL():

	funcionamiento = True

	while(funcionamiento):
	
		NUMERO = LEER_NUMERO()

		if (NUMERO != 'E'):
			print()
			print ('***************************************RESULTADO***************************************')

			if ((NUMERO % 2)==0):
				print ('Tipo de número: Par')
				print (f'Números pares menores que {NUMERO}:')
				aux=NUMERO
				while (aux!=0):	
					print(str(aux)+', ', end= '')
					if (NUMERO > 0):
						aux -= 2
					else:
						aux += 2
				print ('0')
			else:
				print ('Tipo de número: Impar')
				print (f'Número impares menores que {NUMERO}:')
				aux=NUMERO
				while ((aux!=1) and (aux!= -1)):	
					print(str(aux)+', ', end= '')
					if (NUMERO > 0):
						aux -= 2
					else:
						aux += 2
				if (NUMERO > 0):
					print ('1')
				else: 
					print ('-1')

			print ('***************************************************************************************')
		else:
			funcionamiento=False

EJERCICIO_PRINCIPAL()