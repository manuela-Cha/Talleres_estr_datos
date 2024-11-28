import re as re
"""with open('test_pr2.txt', 'r') as archivo:
    contenido = archivo.read()



# en con espacios
def en_con_espacios(contenido):
    contador = 0
    for i in range(len(contenido)-3):
        if contenido[i]+contenido[i+1]+contenido[i+2]+contenido[i+3]==" en " or contenido[i]+contenido[i+1]=="En" :
            contador+=1 

    print(contador)

#en sin espacios
def en_sin_espacios(contenido):
    contador = 0
    for i in range(len(contenido)-3):
        if contenido[i]+contenido[i+1]=="en" or contenido[i]+contenido[i+1]=="En":
            contador+=1 
    print(contador)


en_con_espacios(contenido)
en_sin_espacios(contenido)"""

count=0
file= open('test_pr2.txt','r')
for line in file:
    lista = line.lower().split(" ")
    for i in lista:
        if i == "en":
            count+=1

file.close()
print(count)

