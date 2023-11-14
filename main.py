def B_esMutante(matriz: list) -> bool:
	contador = 0
	chr_to_srch = ["A"*4,"T"*4,"C"*4,"G"*4]
	columnas = [ "".join([x[y] for x in matriz]) for y in range(len(matriz[0]))]
	# las filas son el propio adn mutante
	diagonales = [["".join([matriz[y+i][x+i] for i in range(4)]) for x in range(3)] for y in range(3)]
	#print(diagonales) #esta es la cosa mas nefasta que jamas nadie va a ver
	
	for i in range(3):
		for col in columnas:
			if(col[0+i:4+i] in chr_to_srch):
				contador+=1

	for i in range(3):
		for row in matriz:
			if(row[0+i:4+i] in chr_to_srch):
				contador+=1

	for x in diagonales:
		for j in x:
			if(j in chr_to_srch):
				contador+=1
	if(contador >= 2):
		return True
	else:
		return False





if __name__ == "__main__": 

	adn_mutante = []

	print("Debe ingresar 6 cadenas de ADN (6 caracteres cada una)")
	while True:
		if len(adn_mutante) == 6:
			break
		cadena = input().upper()
		if (len(cadena) != 6):
			print("cadena de adn invalida, ingresela de nuevo")
			continue
		adn_mutante.append(cadena)
	print("--------------------------")
	for i in adn_mutante:
		for j in i:
			print(j,end=" ")
		print("")
	print("--------------------------")
	if(B_esMutante(adn_mutante)):
		print("el paciente es un mutante")
	else:
		print("el paciente no es un mutante")
	print("--------------------------")
	# basicamente tener que buscar 4 en raya pero con las letras 
	# (A,T,C,G)
	
	
	#arreglo con todas las posibles columnas donde buscar

	#print(columnas)