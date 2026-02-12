""" 1 tuEresMayorDeEdad
    vamos a trabajar con "if" y "switch"
"""
""" 2 diasDeLaSemana y cuantoGanas
    si tiene un salario:
        si el salario es menor de 2 slmv tiene una boificacion del 70%
        sino la binificacion es del 30%
    imprimir salario , bonificacion y neto a pagar
"""
""" 3 ganasteLaMateria 
nota - 0 -> 5 = validar

0.0 - 1.99 = perdio
2.0 - 2.99 = recuperar
3.0 - 3.99 = raspao
4.0 - 4.5 = vas bien
4.5 - 5 = ganaste 

"""

def tuEresMayorDeEdad(edad) :
    def validacion_edad(edad):
        if edad > 17 :
            print("eres mayor de edad")
            print("y tienes "+edad)
        else:
            print("bb a dormir")

    mensaje = validacion_edad(edad)
    return mensaje

def cuantoGanas(gano) :

    salario_minimo_legal_vigente = 1750905 * 2

    if gano <= salario_minimo_legal_vigente:
        bonificacion = salario_minimo_legal_vigente * 70/100
        print("bono: te ganaste el 70% " , bonificacion)
    else :
        bonificacion = salario_minimo_legal_vigente * 30/100
        print("bono: te gasnaste el 30% " ,bonificacion)

    neto = gano + bonificacion

    return ("en total ",neto)

def diasDeLaSemana(semana):
    if semana < 1 or semana > 7 :
        return(F"el {semana} no 😒 solo es del 1 al 7 / no entres")
    else :

        match semana :
            case 1:
                 return(F"el {semana} corresponde al lunes")
            case 2 :
                 return(F"el {semana} corresponde al martes")
            case 3 :
                 return(F"el {semana} corresponde al miercoles")

            case 4 :
                 return(F"el {semana} corresponde al jueves")

            case 5 :
                 return(F"el {semana} corresponde al viernes ")

            case 6 :
                 return(F"el {semana} corresponde al sabado")

            case 7 :
                 return(F"el {semana} corresponde al domingo")

            case _ :
                 return(F"el {semana} no 😒 solo es del 1 al 7")
    
def ganasteLaMateria(nota) :
    if nota >= 0.0 and nota <= 5 :
        if nota <= 1.99 :
            return(F"{nota} perdiste asta el recreo")
        elif nota >= 2.0 and nota <= 2.99 :
            return(F"{nota} esta bien, puedes recuperar ")
        elif nota >= 3.0 and nota <= 3.99 :
            return(F"{nota} joa pasaste con la barriga por el piso (-raspao-) ")
        elif nota >= 4.0 and nota <= 4.5 :
            return(F"{nota} vas bien , sigue asi campeon")
        else :
            return(F"{nota} exelente - ganaste")
    else :
        return(F"solo es del 0.1 al 5.0 y tu pusiste {nota}")


# indice de masa muscular 


peso = 20
altura = 1.60

def calcularIMC(peso , altura):
    imc = peso / (altura * altura)
    return imc

def estadoDelImc(imc):
    if imc >= 18.5 and  imc <= 24.9 :
        return("normal")
    elif imc >= 25 and  imc <= 29.9 :
        return("sobre peso")
    elif imc >= 30 and imc <=  34.9 :
        return("obesidad 1")
    elif imc >= 35 and imc <=  39.9 :
        return("obesidad 2")
    elif imc >= 40 :
        return("obesidad 3")
    else :
        return("desnutricion")
    
indice1 = calcularIMC(20 , 1.74)
indice2 = estadoDelImc(indice1)
print(indice1)
print(indice2)