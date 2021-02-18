
'''
La siguiente funcion tiene como objetivo verificar si el usuario ha 
ingresado ha ingresado un dato tipo string, en el caso que no se 
ha ingresado un dato se le mostrará una exepcion y en el caso 
contrario se mostrará el resultado con la primera letra en capitalizada
'''
def UpperFirstLetter(your_string):
    if your_string is '':
        raise ("La cadena no puede ser vacia. Intenta de nuevo.")

    result_string = your_string[0].upper() + your_string[1:]
    print("Resultado de tu cadena de texto: ",result_string)

if __name__=="__main__":
    your_string = input("Por favor, ingresa tu cadena de texto: ")
    UpperFirstLetter(your_string)
