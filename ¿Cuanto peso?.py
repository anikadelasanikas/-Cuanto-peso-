peso = float(input("Pon tu peso en kg:"))
altura = float(input("Pon tu altura en Metros:"))

imc = peso / (altura ** 2)
if imc < 18.5:
    print ("Tienes un bajo peso procura comer mas y hacer ejercicio para ganar musculo")
elif imc < 25:
       print ("Tienes un peso normal sigue con tu dieta pero si quieres puedes tonificar y realzar tu musculo")
       
elif imc < 30 :
       print ("Tienes sobrepeso cambia tu dieta: Cambiando los dulces por frutas y la comida chatarra en comida saludable y haz cardio por 30 y ejercicio pa que cuando pierdas peso no se caiga la piel")
       
else:
       print ("Tienes obesidad  cambia por completo tu dieta ponte a hacer cardio todo los dias y ejercicio pa tonificar")