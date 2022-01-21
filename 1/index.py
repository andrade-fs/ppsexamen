#Crea un programa que tome como entrada una contraseña y devuelva su grado complejidad. 
# Se considerará una contraseña fuerte si posee una combinación de caracteres mayor que 8, además debe incluir caracteres especiales, caracteres en minúscula, mayúsculas y números. Si cumple todas las condiciones pero su extensión es menor o igual a 8 se considerará una contraseña de fortaleza media. Si la contraseña tiene una extensión mayor a 8 y cumple todos los requisitos a excepción de uno, también será considerada de fortaleza media. En cualquier otro caso, se considerará una contraseña débil. (1 puntos)

import re
password = input('Holaa, dame una contraseña para comprobar: ')

def checkPassword(password):
    length = len(password)
    #media
    errores = []
    if(length <=8):
        errores.append('No cumples con la longitud!')
    
    loweer_regex        = '([a-z])'
    upper_regex         = '([A-Z])'
    special_chars_regex = '([^A-Za-z0-9])'
    numbers_regex       = '\d+'    
    #Check lowwer
    if(re.search(loweer_regex, password)):
        print('Req. Minusuclas aprobado')
    else: 
        errores.append('Faltan minusculas')
    #check upper
    if(re.search(upper_regex, password)):
        print('Req. Mayusculas aprobado')
    else: 
        errores.append('Faltan Mayusculas')
        
    if(re.search(special_chars_regex, password)):
            print('Req. Caracteres especiales aprobado')
    else: 
        errores.append('Faltan Caracteres especiales')
        
    if(re.search(numbers_regex, password)):
            print('Req. Numeros aprobado')
    else: 
        errores.append('Faltan Numeros')
    
    if(len(errores) >= 2):
        print('prueba otra vez contraseña debil')
    
   
    if(len(errores) == 0):
        print('\nContraseña Seguridad Fuerte')    
    else:
        if(len(errores) == 1 and errores[0] == 'Faltan minusculas'):
            print('Seguridad Contraseña Media')
        elif(len(errores) == 1):
            print('seguridad Contrasñe Media')
        elif(len(errores) > 1):
            print('Seguridad Contrasñe Debil')
            
        for i in range(len(errores)):
            print(errores[i])
   
 
       
checkPassword(password)


