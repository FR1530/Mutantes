# Mutantes

* alumno: Fabrizio Racigh
* Email: racighfabriziouni@gmail.com
* legajo: 51624

## Trabajo practico mutantes

El siguiente trabajo permite detectar cadenas de "mutantes" dada una matriz de strings, dicha matriz tiene que cumplir con:
* debe contener 6 elementos
* cada secuencia debe tener 6 caracteres de largo

la secuencia no es sensible a las mayúsculas.
El programa mismo verificara el largo de cada
cadena al ser introducida, si no conduerda en largo
se informará de ello al usuario para que la reintroduzca

## como utilizar el programa
una vez descargado el archivo debe abrir una terminal en el mismo directorio, luego tiene que ejecutar el archivo main.py
el programa le pedira cargar su matriz de adn fila por fila
```
py main.py
```

## Como funciona? 

a travez de comprension de listas y splices (recortes), la lista se separa en cadenas de 4 caracteres de diagonales, columnas y filas,
una vez hecho se compara con las 4 incidencias de ADN
usando un bucle simple

## ejemplos de matrices de adn
Caso mutante:
```
A T G C G A
C A G T G C
T T A T G T
A G A A G G
C C C C T A
T C A C T G
```
caso no-mutante: 
```
T C A C T G
A T G C G A
C A G T G C
T T A T T T
A G A C G G
G C G T C A
```
