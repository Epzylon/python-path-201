# Listas
milista = [0,1,2,3,"ABC"]

print(milista[4])

#Append

milista.append("DEF")

print(milista)

# Remove

milista.remove(5)

print(milista)

milista.sort()
milista.count(2)
milista.index("ABC")

# for
for item in milista:
    print(item)

##########################
#### Ejercicio 1 #########
##########################

semana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
for dia in semana:
    print(dia)

semana.remove('Domingo')
semana.remove('Sabado')

c = len(semana)

d = 0
for i in semana:
    d += 1

###############################
#### Apertura de Archivos  ####
###############################

file = 'fifa2019.csv'

file_descriptor = open(file)
for line in file_descriptor:
    print(line.split(',').strip('\n'))

###########################
#### Ejercicio 2 ##########
###########################

file = 'fifa2019.csv'
file_descriptor = open(file)
lineas_contador = 0
edades = 0
fuerza_mayor = 0
file_descriptor.readline()

for line in file_descriptor.readlines():
    print(line)
    lineas_contador += 1
    l = line.strip('\n').split(',')
    edades += int(l[3])
    if l[28] != '':
        if float(l[28]) > 95:
            fuerza_mayor += 1

###########################
###### Matrices ###########
###########################

milista = [[1,2,3],[4,5,6],[7,8,9]]

for i in milista:
    for x in i:
        print(x)


milista = [ [“A”,”B”,”C”], [“D”,”E”,”F”], [“G”,”H”,”I”] ]

milista[0][2]
milista[1][3]
milista[2][1]

############################
####### Ejercicio 2 bis ####
############################

# a
file = 'fifa2019.csv'
file_descriptor = open(file)
matriz = []

file_descriptor.readline()

for line in file_descriptor.readlines():
    l = line.strip('\n').split(',')
    matriz.append(l)


# b
edades = 0
for mline in matriz:
    edades += int(mline[3])

print(edades/len(matriz))

# c
fuerza_mayor = 0
for mline in matriz:
    if mline[28] != '':
        if float(mline[28]) > 95:
            fuerza_mayor += 1


############################
##### Diccionarios #########
############################

diccionario = { ‘key’: ‘value’, ‘lista’: [1,2,3]. ‘num’: 99 }
diccionario[‘key’]
diccionario[‘num’]

diccionario = {
‘domingo’: 1,
‘lunes’: 2,
‘martes’: 3,
‘miercoles’: 4,
jueves’: 5,
‘viernes’: 6,
‘sabado’: 7
}
diccionario.keys()
diccionario.values()
diccionario.items()

############## NumPy #############
import numpy as np
a1 = np.array((1,2,3,4,5,6))
a.shape
a.size
a.sort()
a.sum()
a.mean()
a.max()
a.min()


a2 = np.array( ([1,2,3],[4,5,6],[7,8,9]) )
a2.shape
a2.size

a2.sort()
a2.transpose()
a2.sum()
a2.mean()
a2.max()
a2.min()
a2.diagonal()

a3 = np.array((
([1,2,3],[4,5,6],[7,8,9]),
([10,11,12],[13,14,15],[16,17,18]),
([1,3,4],[1,3,3],[3,3,3])))

a3.sum(axis=0)
a3.sum(axis=1)
a3.sum(axis=2)

a3[0]
a3[0, 0]
a3[0, 0, 0]

###### Ejercicio 3 #########
# 1
a3[1,0,2]

# 2
a3[2,1,0]

###### Matriz Slicing ######

a3[0:2]
a3[0, 0:2]
a3[0, 0, 0:3]

####### Ejercicio 4 ######

# 1
a3[1,1:3]

# 2
a3[0:3,0:1]
a3[:,0:1]

# 3
a4 = a3[0:3,0:1,0:2]
a4 = a3[:,0:1,0:2]


####### Operaciones con arrays ######

a4 * 10
a4 + 1
a4 + [1,2]
a4 - [2,3]
a4 + [1,2,3]


######################################
####### Ejercicio 5 ##################
######################################

import numpy as np
file = 'fifa2019.csv'
matriz = []

fd = open(file)
fd.readline()

#### Cargo cada linea como un vector dentro de la matriz
for line in fd.readlines():
    matriz.append(line.strip('\n').split(','))

fd.close()

#3
array1 = np.array(matriz,dtype=np.float)

#5
prom_edad = array1.sum(axis=0)[3] / array1.shape[0]

#6
((array1[:,28] > 95)*1).sum()


