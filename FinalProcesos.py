
import numpy as np 
import random


print("Digita la probabilidad de contagio entre 0 y 1")
Probabilidad = float(input())
print("Digita la cantidad de pasos entre 1 y 3")
Pasos = int(input())
PasosHelp = Pasos

v = 0
Poblacion = [0,0,0,0,'Enfermo']
sanos = 0
enfermos = 0
"""Se pone de esta manera la lista para garantizar que al menos uno 
de la poblacion esta enfermo"""

for x in range (0,4):
    Estado = random.randint(0, 1)
    Poblacion[x]= Estado
    if Poblacion[x] == 1:
        Poblacion[x] = "Sano"
        sanos += 1
    else: 
        Poblacion[x]="Enfermo"
        enfermos += 1

print("                                                                  ")       
print("                           POBLACION INICIAL                      ")
print("                                                                  ")
print("         " + str(Poblacion))
print("                                                                  ")
print("                                                                  ")
print("la probabilidad de que haya seleccion de un sano y un enfermo es: " + " (1/5*(1/" +str(sanos)+")+0.25(*1/" +str(enfermos)+"))")
Probabilidad = (Probabilidad*10)

while v< Pasos:
    print("                                                                  ")
    print("----------------------------PASO--------------------------------------")
    y = random.randint(0,4)
    z = random.randint(0,4)
    if y != z:    
        if Poblacion[y] != Poblacion[z]:
            print("Puede haber contagio " + " Persona:"+ str(y+1) + " y "+ "Persona:" + str(z+1))
            
            p = float(random.random())
           
            p=(p*10)
            print("                                                                  ")
            
            if p <= Probabilidad:
                sanos -=1
                enfermos+=1
                print("Se contagio.")
                print("                                                                  ")
                print("la probabilidad de que haya seleccion de un sano y un enfermo es: " + " (1/5*(1/" +str(sanos)+")+0.25(*1/" +str(enfermos)+"))")
                if Poblacion[y] == "Sano":
                    Poblacion[y] = "Enfermo"
                else:
                    Poblacion[z]="Enfermo"
            else: 
                
                print("No se contagio")
                print("                                                                  ")
                print("la probabilidad de que haya seleccion de un sano y un enfermo es: " + " (1/5*(1/" +str(sanos)+")+0.25(*1/" +str(enfermos)+"))")
        else: 
            print("No hay contagio " + " Persona:"+ str(y+1) + " y "+ "Persona:" + str(z+1))
            print("                                                                  ")
            
    else: 
        Pasos += 1
        print("Se selecciono la misma persona, no hay contagio")
    
    
   
    v += 1
    
    
    
print("                                                                  ")
print("                              POBLACION FINAL                     ")    
print(Poblacion)
# print (Probabilidad) 
MatTra = np.array([[Probabilidad/10,0], [1-(Probabilidad/10),0]])
sima = 0
resultMatTra = MatTra
PasosHelp -= 1

while sima<PasosHelp: 
    resultMatTra = resultMatTra.dot(MatTra)
    sima += 1
    
print("                                                                  ")
print("Matriz de transicion P^n: ")
print(resultMatTra[:,0])



