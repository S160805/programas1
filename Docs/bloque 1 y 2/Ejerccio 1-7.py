# Este programa imprimira el perimetro y area de un circulo,
#teniendo el radio
radio = float(input("¿Cual es el radio del circulo?"))
print("Radio", radio)
# Obtener el area del circulo con el radio
valor_pi = 3.1416
area = valor_pi * radio ** 2
perimetro = valor_pi * 2 * radio
print("El area es: ", area)
print("El perímetro es: ", perimetro)