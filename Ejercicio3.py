def LEER_HORASTRABAJADAS():
	horasTrabajadasStr = 'N'
	while (not(horasTrabajadasStr.isdigit())):
		horasTrabajadasStr=input('Introduzca horas trabajadas:')
		if(not(horasTrabajadasStr.isdigit())):
			print("ERROR: Debes introducir un número ENTERO positivo")
			print()
	return horasTrabajadasStr;

def LEER_TARIFA():	
	tarifaFloat = -1.1

	while(tarifaFloat < 0):
		try:
			tarifaStr=input('Introduzca tarifa (>= 0€):')
			tarifaFloat = float(tarifaStr)
			if (tarifaFloat <0):
				print("ERROR: Debes introducir un número ENTERO O FLOTANTE positivo")
				print()
		except ValueError:
			print("ERROR: Debes introducir un número ENTERO O FLOTANTE positivo")
			print()

	return tarifaFloat;

def EJERCICIO_PRINCIPAL():
	print()
	HORASTRABAJADAS=int(LEER_HORASTRABAJADAS())
	print()
	TARIFA=LEER_TARIFA()

	TARIFAPLUS= TARIFA * 1.5

	if (HORASTRABAJADAS>40):
		resultado = (40 * TARIFA)+(HORASTRABAJADAS-40)*TARIFAPLUS
	else:
		resultado = HORASTRABAJADAS * TARIFA

	print()
	print(f'Sueldo correspondiente: {resultado}€')
	input()

EJERCICIO_PRINCIPAL()