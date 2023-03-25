print("---------------------------------------------")
print("------------UIS-BIKE-RENTAL------------------")
print("---------------------------------------------")

print("BIENVENIDO ESTUDIANTE UIS. ")
print(" ")
CODIGO = int(input("INGRESE SU CODIGO ESTUDIANTIL: "))
NOMBRE = input("INGRESE SU NOMBRE: ")
PROGRAMA = input("INGRESE SU PROGRAMA: ")
SEDE = int(input("INGRESE SU SEDE: \n1.BARRANCA\n2.SOCORRO\n3.MALAGA\n4.BARBOSA\n"))


if 1<= SEDE <=4:
    if SEDE == 1:
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("ESTUDIANTE:" ,NOMBRE, "\nCODIGO:" ,CODIGO, "\nPROGRAMA:" ,PROGRAMA, "\nSEDE BARRANCA.\nPUEDE ACCEDER A LA RENTA DE UNA BICICLETA.")
        print("---------------------------------------------------------------------------------------------------------------------------------")
    elif SEDE == 2:
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("ESTUDIANTE:" ,NOMBRE, "\nCODIGO:" ,CODIGO, "\nPROGRAMA:" ,PROGRAMA, "\nSEDE SOCORRO.\nPUEDE ACCEDER A LA RENTA DE UNA BICICLETA.")
        print("---------------------------------------------------------------------------------------------------------------------------------")
    elif SEDE ==3:
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("ESTUDIANTE:" ,NOMBRE, "\nCODIGO:" ,CODIGO, "\nPROGRAMA:" ,PROGRAMA, "\nSEDE MALAGA.\nPUEDE ACCEDER A LA RENTA DE UNA BICICLETA.")
        print("-------------------------------------------------------------------------------------------------------------------------------")
    elif SEDE == 4:
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("ESTUDIANTE:" ,NOMBRE, "\nCODIGO:" ,CODIGO, "\nPROGRAMA:" ,PROGRAMA, "\nSEDE BARBOSA.\nPUEDE ACCEDER A LA RENTA DE UNA BICICLETA.")
        print("--------------------------------------------------------------------------------------------------------------------------------")

else: 
    print("ERROR! VALOR INVALIDO. \nESCOGA UN DE LAS OPCIONES. ")

print("PUEDE PASAR POR LOS PUNTOS AUTORIZADOS DE LA UIS PARA RECOGER SU BICICLETA.")