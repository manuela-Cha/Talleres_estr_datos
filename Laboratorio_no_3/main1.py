from Laboratorio_no_2.Usuario import Usuario
from Laboratorio_no_3.Agenda import Agenda

agenda1 = Agenda(5)

usuarios = [
    Usuario("manu", 1, "1990-01-01", "Medellin", "123456789", "manu@unal.com", "Calle 123"),
    Usuario("javier", 2, "2022-05-15", "Bogota", "987654321", "javier@unal.com", "Avenida 456"),
    Usuario("karla", 3, "2003-09-10", "Cali", "456789123", "karla@unal.com", "Calle Falsa 789"),
    Usuario("carolina", 4, "2005-03-20", "Barranquilla", "789123456", "carolina@unal.com", "unidad 101"),
    Usuario("alejanda", 5, "1994-07-25", "Pereira", "321654987", "aleja@unal.com", "Barrio 742")
]

for usuario in usuarios:
    agenda1.agregar(usuario)

posicion = agenda1.buscar(3)
print(f"El usuario con ID {3} está en la posición: {posicion}")

agenda1.toFile()
