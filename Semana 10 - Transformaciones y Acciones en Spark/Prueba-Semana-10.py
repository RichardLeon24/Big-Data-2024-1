#1. Cree un RDD llamado lenguajes que contenga los siguientes lenguajes de programación: Python, 
#R, C, Scala, Rugby y SQL.

#       C) Cree un nuevo RDD que solo contenga aquellos lenguajes de 
#         programación que comiencen con la letra R.

#2. Cree un RDD llamado pares que contenga los números pares existentes en el intervalo [20;30].

#       B) Obtenga una lista compuesta por los números pares en el intervalo 
#         [20;30] y sus respectivas raíces cuadradas. Un ejemplo del resultado 
#         deseado para el intervalo [50;60] sería la lista [50, 7.0710678118654755, 52, 7.211102550927978, 
#         54, 7.3484692283495345, 56, 7.483314773547883, 58, 7.615773105863909, 60, 7.745966692414834].

#       C) Eleve el número de particiones del RDD sqrt a 20.

#       D) Si tuviera que disminuir el número de particiones luego de haberlo 
#          establecido en 20, ¿qué función utilizaría para hacer más eficiente su código?

#3. Cree un RDD del tipo clave valor a partir de la lectura del txt de transacciones. 
#Tenga en cuenta que deberá procesar el RDD leído para obtener el resultado solicitado. Supongamos 
#que el RDD resultante de tipo clave valor refleja las transacciones realizadas por número de 
#cuentas. Obtenga el monto total por cada cuenta (Suma).
#Tip: Cree su propia función para procesar el RDD leído.