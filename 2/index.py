#Crea un programa generador de contraseñas aleatorias. Toma como entrada el número de caracteres que ha de tener. El programa siempre devuelve contraseñas fuertes (entendiendo por fuerte el criterio especificado en el ejercicio anterior). (1.5 punto)

import string
import random
import re
legth_password = int(input('Tamaño de la contraseña deseada?: '))

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def checkPassword(password):
    length = len(password)
    #media
    errores = []
    if(length < 7):
        errores.append('No cumples con la longitud!')
    
    loweer_regex        = '([a-z])'
    upper_regex         = '([A-Z])'
    special_chars_regex = '([^A-Za-z0-9])'
    numbers_regex       = '\d+'    
    #Check lowwer
    if(not re.search(loweer_regex, password)):
        errores.append('Faltan minusculas')
    #check upper
    if(not re.search(upper_regex, password)):
        errores.append('Faltan Mayusculas')
        
    if(not re.search(special_chars_regex, password)):
        errores.append('Faltan Caracteres especiales')
        
    if(not re.search(numbers_regex, password)):
        errores.append('Faltan Numeros')
    
    if(len(errores) == 0):
       print('Your password is: ' +str(password))
       return True  
    else:
       return False
   
 



def generate_temp_password(length):
  	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))  
	random.shuffle(password)

	return "".join(password)

if(legth_password > 7):
    generate_temp_password(legth_password)
    while not checkPassword(generate_temp_password(legth_password)):
        generate_temp_password(legth_password)
    
else:
    print('Longitud invalida')
