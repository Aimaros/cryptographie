#coding:utf-8
import os

def detection(message, cle):
    cles = {}
    indice = 0
    space_cle=''
    for letter in cle:
        if letter == ' ':
            space_cle += ' '
        cles[indice] = ord(letter)-65
        #print(ord(letter)-65)
        indice += 1
    cryptage = ''
    indexe = 0
    char = 0
    dif = 0

    
    for letter in message :
        if letter == ' ':
            #print(ord(letter))
            cryptage += ' '
        else:
            if indexe == len(cle):
                indexe = 0
            if ord(letter) + cles[indexe] > 90:
                dif = ord(letter) + cles[indexe] - 90
                char = 64 + dif
            else :
                char = ord(letter) + cles[indexe]
            cryptage += chr(char)
            indexe += 1
    return cryptage
    
#detection('BONJOUR','FEU')

message = input("Entrer votre message :")
message = message.upper()

cle = input("Entrer la cle de cryptage :")
cle = cle.upper()
print(detection(message, cle))
    

os.system("pause")
