def construye(*aditamentos):
	print(aditamentos)

construye('asientos de cuero')
construye('asientos de cuero', 'aire','color rojo')

def construye_ademas(aros, cubierta_volante,*aditamentos):
	print(aros,cubierta_volante,aditamentos)

construye_ademas('cromados','lisa','asientos de cuero')
construye_ademas('cromados','lisa','asientos de cuero', 'aire','color rojo')

def direccion(pais, departamento, **info):
	info['pais'] = pais	
	info['departamento'] = departamento	
	return info

print(direccion('Argentina', 'Buenos Aires', street='Defensa 123'))
print(direccion('Estados Unidos', 'Nueva York', street= '5th Avenida 234', building= 'Building Tower Sky'))


