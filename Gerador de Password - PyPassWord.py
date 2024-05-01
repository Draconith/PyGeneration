#Gerador de Password
import random
#Gerador de senha incluindo 
numeros=['0','1','2','3','4','5','6','7','8','9']

letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
letras_maiusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

simbolos=['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]



print("Bem vindo ao Gerador de Senhas")
#entrada
nr_letras= int(input("Quantas letras você gostaria de incluir na sua senha?"))
nr_numeros= int(input("Quantos numeros você gostaria de incluir na sua senha?"))
nr_letrasMaiusculas=int(input("Quantas letras MAIUSCULAS você deseja inserir na sua senha?"))
nr_simbolos= int(input("Quantos simbolos você gostaria de incluir na sua senha?"))

password_list=[]
for char in range(1,nr_letras,+1):
     password_list.append(random.choice(letras))
for char in range(1,nr_letrasMaiusculas,+1):
    password_list.append(random.choice(letras_maiusculas))
for char in range(1,nr_numeros,+1):
     password_list += (random.choice(numeros))
for char in range(1,nr_simbolos,+1):
     password_list += (random.choice(simbolos))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Sua senha foi criada: {password}")

import time
time.sleep(60)

