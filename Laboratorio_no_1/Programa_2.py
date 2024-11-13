with open('test_pr2.txt', 'r') as archivo:
    contenido = archivo.read()

# en con espacios
def en_con_espacios(contenido):
    contador = 0
    for i in range(len(contenido)-3):
        if contenido[i]+contenido[i+1]+contenido[i+2]+contenido[i+3]==" en ":
            contador+=1 
    print(contador)

#en sin espacios
def en_sin_espacios(contenido):
    contador = 0
    for i in range(len(contenido)-3):
        if contenido[i]+contenido[i+1]=="en":
            contador+=1 
    print(contador)


en_con_espacios(contenido)
en_sin_espacios(contenido)