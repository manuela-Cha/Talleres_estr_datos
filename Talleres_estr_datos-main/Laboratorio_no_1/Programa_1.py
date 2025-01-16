class operaciones:
    @staticmethod
    def entrada():
        while True:
            try:
                n = int(input("Ingrese el numero de entradas: ")) 
                if n > 0:
                    break
                else:
                    print("La entrada no es válida. Ingrese un número n entero positivo.")
            except ValueError:
                print("La entrada no es válida:")
        coleccion = []
        iterador = 0
        while iterador != n:
            try:
                num = int(input("Ingrese un número entero positivo: ")) 
                if n > 0:
                    coleccion.append(num)
                    iterador+=1
                else:
                    print("La entrada no es válida. Ingrese un número entero positivo.")
            except ValueError:
                print("La entrada no es válida.")
        return coleccion, n

    @staticmethod
    def valor_maximo(coleccion):
        mayor = coleccion[0]
        for i in range(len(coleccion)):
            if coleccion[i]>mayor:
                mayor = coleccion[i]
        print("mayor:",mayor)
        return mayor
    
    @staticmethod
    def valor_minimo(coleccion):
        menor =  coleccion[0]
        for i in range(len(coleccion)):
            if coleccion[i]<menor:
                menor = coleccion[i]
        print("menor:",menor)
        return menor
    
    @staticmethod
    def suma(coleccion):
        suma = 0
        for i in coleccion:
            suma+=i
        print("suma:",suma)
        return suma

    @staticmethod
    def promedio(coleccion,n):
        suma = 0
        for i in coleccion:
            suma+=i
        promedio = suma/n
        print("Promedio:",promedio)
        return promedio
    
    def main():
        coleccion,n =operaciones.entrada()
        operaciones.valor_maximo(coleccion)
        operaciones.valor_minimo(coleccion)
        operaciones.suma(coleccion)
        operaciones.promedio(coleccion,n)

ejecucion = operaciones
ejecucion.main()