
'''
En esta función se toma el string que el usuario ha ingresado
y lo convierte en un arreglo de caracteres
'''

def split(word):
    return [char for char in word]


'''
En esta funcion se toma el arreglo de caracteres y los concatena
para postereiormente hacer la comparación
'''
def uni(array):
    result = ""
    for char in array:
        result = result+char
    return result

'''
Por ultimo, en esta función se compara si el string es igual a una palabra
que ya está definida que en este caso es "hola" y se verifica si cada caracter
cumple con la condición.
'''


def ChatValidHello(your_string):
    if your_string is '':
        raise ("La cadena no puede ser vacia. Intenta de nuevo.")

    my_string_array =  list(dict.fromkeys(split(your_string)))

    if uni(my_string_array).lower() == 'hola':
        print ('VERDADERO')
    else:
        print ('FALSO')

if __name__=="__main__":
    your_string = input("Por favor, ingresa tu cadena de texto: ")
    ChatValidHello(your_string)
