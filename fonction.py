def detection(message, cle):
    cles = {}
    indice = 0
    for letter in cle:
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
    