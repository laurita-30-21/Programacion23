# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RD75M8_P6pZcLFXh5pJUex89Vw5EXGov
"""

# Default Input() = str
salario = int(input("Digite el salario base: "))
print("\nEl salario base es= {}".format(salario))
vent1 = float(input("Digite el valor de la venta No.1: "))
vent2 = float(input("Digite el valor de la venta No.2: "))
vent3 = float(input("Digite el valor de la venta No.3: "))
suma = vent1 + vent2 + vent3
print("\nEl resultado total de las ventas es= {:.0f}".format(suma))
comisión = suma * 0.10
print("\nEl resultado total de la comisión= {:.0f}".format(comisión))
total=salario + comisión
print("\nEl pago total es:= {:,.0f}".format(total))

"""Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de tres exámenes parciales."""

calif1 = float(input("Digite la callificación No. 1: "))
calif2 = float(input("Digite la calificación No. 2: "))
calif3= float(input("Digite la calificación No.3: "))
prom = (calif1 + calif2 + calif3)/3
print("\nEl promedio de su nota es= {:.0f}".format(prom))

"""Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de tres exámenes parciales."""

# Default Input() = str
compra = int(input("Digite el valor total de la compra: "))
print("\nEl valor total de la compra= {:,.0f}".format(compra))
descuento=compra * 0.15
print("\nEl valor del descuento es:= {:,.0f}".format(descuento))
total= compra - descuento
print("\nEl valor final a pagar es:= {:,.0f}".format(total))

"""Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes"""

# Default Input() = str
hombres = float(input("Digite el numero de hombres: "))
mujeres = float(input("Digite el numero de mujeres: "))
suma = hombres + mujeres
print("\nEl total de personas es= {:.0f}".format(suma))
porc_hombres = hombres * 100 / suma
porc_mujeres = mujeres * 100 / suma
print("\nEl porcentaje total de hombres es= {:.3f}".format(porc_hombres))
print("\nEl porcentaje total de mujeres es= {:.3f}".format(porc_mujeres))



"""Un vendedor recibe un sueldo base más un 10% extra por 
comisión de sus ventas, el vendedor desea saber cuánto 
dinero obtendrá por concepto de comisiones por las tres 
ventas que realiza en el mes y el total que recibirá en 
el mes tomando en cuenta su sueldo base y comisiones.

Una tienda ofrece un descuento del 15% sobre el total 
de la compra y un cliente desea saber cuánto deberá 
pagar finalmente por su compra.

3. Un alumno desea saber cuál será su calificación final en 
la materia de Algoritmos. Dicha calificación se compone 
de tres exámenes parciales.

4. Un maestro desea saber qué porcentaje de hombres y que 
porcentaje de mujeres hay en un grupo de estudiantes
"""



"""Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico."""

edad = int(input("Digite su edad: "))

if edad > 55:
  print(f"El Disfrutaras de un bono del cinco porciento")
else :
  print(f"No disfrutas del bono")

"""Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre"""

casado = input("Es casado: ")
usubd = "SI"

hij = input ("Tiene hijos")
hijos = "SI"

if casado == usubd and hij == hijos:
  print("Disfruta el paseo!")
else:
  print("No puedes disfrutar del paseo")

"""Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión."""

sueldo = float (input("Digite el sueldo básico: "))

if sueldo >= 1000000 and sueldo <= 1500000:
  print("Obtuviste comisión sobre el dos porciento del sueldo")
elif sueldo >= 1005001 and sueldo <= 2000000:
  print("Obtuviste comisión sobre el cinco porciento del sueldo")
else:
  print("No obtuviste comisión")

"""Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación."""

dias = float (input("Cuantos días trabajó: "))
salario = float (input("Cuánto es su salario: "))

if dias >= 20 and salario < 1000000:
  print("Obtuviste un bono por alimentación")
else:
  print ("No obtuviste bono")