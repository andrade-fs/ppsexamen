#Escribe un programa para crear y gestionar un diccionario para tus contraseñas generadas automáticamente. El diccionario debe pertenecer a un único usuario, de modo que si buscamos nuestra contraseña para el correo, email o facebook. Debe devolvernos valores diferentes. Las funcionalidades que permitiremos serán:

#añadir una entrada nueva al diccionario (0.5 puntos)

#listar todo el diccionario (0.5 puntos)

#buscar una entrada en el diccionario (0.5 puntos)
import json


a_file = open("passwords.json", "r")
diccionario = json.load(a_file)
a_file.close()

doit = int(input('what yo want to do it (1: see paswords, 2 add password, 3 edit passwords): '))



if(doit == 1):
    print('Your credentialas:passwords')
    for clave in diccionario:
        print(clave+" : "+diccionario[clave])
elif(doit == 2):
    email = input('Your email: ')
    password = input('Your password: ')
    diccionario[email] = password
    print('Password addes succesfuly!')
    
elif(doit == 3):
    email = input('What account, you want to edit? Search by your email: ')
    if(diccionario[email] != None):
        print('Okeeeey letsgoo')
        password = input('Your password: ')
        diccionario[email] = password
        print('Password edited succesfuly!')
    else:
        print('Oops! We can´t find your email, are you sure we have it?')
else:
    print('oops, at the moment we can´t have more tha 3 functions... try again')
a_file = open("passwords.json", "w")
json.dump(diccionario, a_file)
a_file.close()