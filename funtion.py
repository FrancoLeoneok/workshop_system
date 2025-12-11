def validacion(mensaje_entrada:str,mensaje_salida:str,opciones:list[str]):
    variable_control = False
    while not (variable_control):
        atributo = input(mensaje_entrada).lower()
        if atributo in opciones:
            variable_control = True
        else:
            print(f'{mensaje_salida}')
        return atributo

def validacion_try(mensaje_entrada:str,mensaje_salida_valor:str,mensaje_salida_tipo:str,inicio_dominio:int = 1, fin_dominio:int = 999999999999999999999999):
   variable_control = False
   atributo = None
   while not (variable_control):
        try:
            atributo = int(input(mensaje_entrada))
            if inicio_dominio <= atributo <= fin_dominio:
                variable_control = True
            else:
                print(f'{mensaje_salida_valor}')
        except ValueError:
            print(f'{mensaje_salida_tipo}')
   return atributo
