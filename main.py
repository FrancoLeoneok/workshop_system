from clase import Negocio, Cliente, Empleado, Computadora, Celular
import datetime

def mostrar_menu():
    print("MENU DE OPCIONES")
    print("="*30)
    print("1. Agregar Cliente")
    print("2. Agregar Empleado")
    print("3. Agregar Computadora")
    print("4. Agregar Celular")
    print("5. Crear Trabajo")
    print("6. Ver Trabajos")
    print("7. Ver lista de Clientes")
    print("8. Ver lista de Empleados")
    print("9. Modificar Trabajo")
    print("0. Salir")
    print("="*30)

def main():
    negocio = Negocio(inventario=[], personal=[], clientela=[])
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre del cliente: ")
            try:
                edad = int(input("Ingrese edad: "))
            except ValueError:
                print("Error: Edad debe ser un número entero.")
                continue
            fecha_nacimiento_str = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
            try:
                fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
            except ValueError:
                print("Error: Formato de fecha inválido. Use YYYY-MM-DD.")
                continue
            sexo = input("Ingrese sexo (M/F): ").upper()
            if sexo not in ["M", "F"]:
                print("Error: Sexo debe ser M o F.")
                continue
            try:
                numero_telefono = int(input("Ingrese número de teléfono: "))
            except ValueError:
                print("Error: Número de teléfono debe ser un número entero.")
                continue
            domicilio = input("Ingrese domicilio: ")
            numero_cliente = len(negocio.clientela) + 1  # Asignar un número único
            cliente = Cliente(nombre, edad, fecha_nacimiento, sexo, numero_telefono, domicilio, numero_cliente)
            negocio.clientela.append(cliente)
            negocio.guardar_clientela()  # Guardar automáticamente
            print("Cliente agregado.")
            
        elif opcion == "2":
            nombre = input("Ingrese nombre del empleado: ")
            try:
                edad = int(input("Ingrese edad: "))
            except ValueError:
                print("Error: Edad debe ser un número entero.")
                continue
            fecha_nacimiento_str = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
            try:
                fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
            except ValueError:
                print("Error: Formato de fecha inválido. Use YYYY-MM-DD.")
                continue
            sexo = input("Ingrese sexo (M/F): ").upper()
            if sexo not in ["M", "F"]:
                print("Error: Sexo debe ser M o F.")
                continue
            try:
                numero_telefono = int(input("Ingrese número de teléfono: "))
            except ValueError:
                print("Error: Número de teléfono debe ser un número entero.")
                continue
            domicilio = input("Ingrese domicilio: ")
            puesto = input("Ingrese puesto: ")
            try:
                salario = float(input("Ingrese salario: "))
            except ValueError:
                print("Error: Salario debe ser un número.")
                continue
            empleado = Empleado(nombre, edad, fecha_nacimiento, sexo, numero_telefono, domicilio, puesto, salario)
            negocio.personal.append(empleado)
            negocio.guardar_personal()  # Guardar automáticamente
            print("Empleado agregado.")
            
        elif opcion == "3":
            negocio.agregar_compu()
            
        elif opcion == "4":
            negocio.agregar_celu()
            
        elif opcion == "5":
            negocio.crear_trabajo()
            
        elif opcion == "6":
            negocio.listar_trabajos()
            
        elif opcion == "7":
            if not negocio.clientela:
                print("No hay clientes registrados.")
            else:
                print("Lista de clientes:")
                for cliente in negocio.clientela:
                    print(cliente)
                    
        elif opcion == "8":
            if not negocio.personal:
                print("No hay empleados registrados.")
            else:
                print("Lista de empleados:")
                for empleado in negocio.personal:
                    print(empleado)
                    
        elif opcion == "9":
            negocio.actualizar_estado_trabajo()
            
        elif opcion == "0":
            print("Saliendo del programa.")
            break
            
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()


