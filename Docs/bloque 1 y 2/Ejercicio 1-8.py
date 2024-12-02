#Realice un programa que calcule el número de minutos, horas y meses,
#dado el número de días por el usuario.
# 16 de octubre del 2024
#Samantha Naomi Vital Flores IT1
dias=int(input("Ingresar los dias:"))
horas= dias *24
minutos= horas*60
meses= dias / 30

print("Los minutos son: " + str(minutos))
print("Las horas son: " + str(horas))
print("Los meses son: " + str(meses))
