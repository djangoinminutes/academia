perros = ['pastor','doberman','collie','golden']
print(perros)
print(perros[2])

print(perros[3])
print(perros[-1])

mascota = f"tengo una mascota de raza {perros[2].title()}"
mascota = "tengo una mascota de raza " + perros[2].title()
print (mascota)

perros[3] = 'boxer'
print(perros)

perros.append('labrador')
print(perros)

perros.insert(10,'dogo')
print(perros)

del perros[3]
print(perros)

print('lista original ',perros)
perro_inteligente = perros.pop()
print('Lista con pop ', perros)
print('elemento popped ', perro_inteligente)

print('Original antes de mover el 0 ', perros)
perro_guardian = perros.pop(0)
print('Original despues de mover el 0 ', perros)
print('item popped ', perro_guardian)

print('Original antes de mover collie ', perros)
perro_fantasia = perros.remove('collie')
print('Original despues de mover collie ', perros)
print('item popped ', perro_fantasia)

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
print(perros)
perros.sort()
print(perros)

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
print('Ordenamos temporalmente ',sorted(perros))
print(perros)

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
perros_ordenados = sorted(perros)
print(perros)
print(perros_ordenados)

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
print(perros)
perros.reverse()
print(perros)

print(len(perros))

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
for perro in perros:
	print(perro)

for i in range(1,5):
	print(i)

for i in range(15,25):
	print(i)

numeros = list(range(5,12))
print(numeros)

for i in range(2,22,2):
	print(i)

numeros = []
for i in range(2,22):
	numeros.append(i)
	print(i)

print(numeros)

print(' el minimo es ',min(numeros))
print(' el maximo es ',max(numeros))
print(' la suma es ',sum(numeros))

numeros = [i for i in range(2,22)]
print(numeros)

cuadrados = [i**2 for i in range(2,22)]
print(cuadrados)

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
dos_perros = list(perros[2:])
print(dos_perros)

for perro in perros[:4]:
	print (perro)

print(perros[:])

perros = ['pastor', 'doberman', 'collie', 'boxer', 'labrador', 'dogo']
flores = ['margarita','rosa','clavel']

temas = [perros,flores]
print(temas[1][:])

perros.reverse()
print(perros[0:3])