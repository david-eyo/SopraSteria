class Persona:
    EDAD = 0
    SEXO = 'X'
    def __init__(self, EDAD, SEXO):
        self.EDAD = EDAD
        self.SEXO= SEXO


def LEER_PERSONAS():
	PERSONAS = [] 
	while (len(PERSONAS) < 50):
		EdadStr = 'P'
		while (not(EdadStr.isdigit())):
			EdadStr=input('Introduzca edad:')

		SexoStr = 'P'
		while ((SexoStr != 'F') and (SexoStr != 'M')):
			SexoStr= input('Introduzca sexo (F para femenino y M para masculino): ')

		PERSONAS.append(Persona(int(EdadStr), SexoStr))
		print('Persona añadida correctamente!')
		print()
	return PERSONAS;

def EJERCICIO_PRINCIPAL():
	PERSONAS=LEER_PERSONAS();
	res=[0,0,0,0]
	#[0]->Para las mujeres menores de edad
	#[1]->Para los hombres menores de edad
	#[2]->Para las mujeres mayores de edad
	#[3]->Para los hombres mayores de edad
	i=0
	while (i<len(PERSONAS)):
		if (PERSONAS[i].EDAD<18):
			if(PERSONAS[i].SEXO=='F'):
				res[0]+=1
			else:
				res[1]+=1
		else:
			if(PERSONAS[i].SEXO=='F'):
				res[2]+=1
			else:
				res[3]+=1
		i+=1

	respuesta1= res[2]+res[3]
	respuesta2= res[0]+res[1]
	respuesta3= res[3]
	respuesta4= res[2]
	respuesta5= ((res[0]+res[2])/len(PERSONAS))*100

	print()
	print ('***************************************RESULTADO***************************************')
	print(f'Cantidad de personas mayores de edad (18 años o más): {respuesta1}')
	print(f'Cantidad de personas menores de edad: {respuesta2}')
	print(f'Cantidad de personas masculinas mayores de edad: {respuesta3}')
	print(f'Cantidad de personas femeninas menores de edad: {respuesta4}')
	print(f'Porcentaje que representan las mujeres respecto al total de personas: {respuesta5}%')
	print ('***************************************************************************************')

EJERCICIO_PRINCIPAL()