from function import function as fn  
import datetime

class Dispositivo:
    def __init__(self, tipo: str, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        
    def to_string(self):
        return f"Dispositivo|{self.tipo}|{self.marca}|{self.modelo}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        if parts[0] == "Dispositivo":
            return cls(parts[1], parts[2], parts[3])
        elif parts[0] == "Celular":
            return Celular.from_string(s)
        elif parts[0] == "Computadora":
            return Computadora.from_string(s)
    
    def __str__(self):
        return f"Dispositivo(tipo={self.tipo}, marca={self.marca}, modelo={self.modelo})"

class Celular(Dispositivo):
    def __init__(self, tipo: str, marca, modelo, sistema_operativo: str, camara_megapixeles: int):
        super().__init__(tipo, marca, modelo)
        self.sistema_operativo = sistema_operativo
        self.camara_megapixeles = camara_megapixeles
        
    def to_string(self):
        return f"Celular|{self.tipo}|{self.marca}|{self.modelo}|{self.sistema_operativo}|{self.camara_megapixeles}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        return cls(parts[1], parts[2], parts[3], parts[4], int(parts[5]))
        
    def __str__(self):
        return f"Celular({super().__str__()}, sistema_operativo={self.sistema_operativo}, camara_megapixeles={self.camara_megapixeles})"

class Computadora(Dispositivo):
    def __init__(self, tipo: str, marca, modelo, procesador, ram_gb):
        super().__init__(tipo, marca, modelo)
        self.procesador = procesador
        self.ram_gb = ram_gb

    def to_string(self):
        return f"Computadora|{self.tipo}|{self.marca}|{self.modelo}|{self.procesador}|{self.ram_gb}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        return cls(parts[1], parts[2], parts[3], parts[4], int(parts[5]))

    def __str__(self):
        return f"Computadora({super().__str__()}, procesador={self.procesador}, ram_gb={self.ram_gb})"

class Persona:
    def __init__(self, nombre: str, edad: int, fecha_nacimiento, sexo: str, numero_telefono: int, domicilio: str):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_telefono = numero_telefono
        self.domicilio = domicilio
    
    def to_string(self):
        return f"Persona|{self.nombre}|{self.edad}|{str(self.fecha_nacimiento)}|{self.sexo}|{self.numero_telefono}|{self.domicilio}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        if parts[0] == "Persona":
            return cls(parts[1], int(parts[2]), datetime.datetime.fromisoformat(parts[3]).date(), parts[4], int(parts[5]), parts[6])
        elif parts[0] == "Empleado":
            return Empleado.from_string(s)
        elif parts[0] == "Cliente":
            return Cliente.from_string(s)
    
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad}, fecha_nacimiento={self.fecha_nacimiento}, sexo={self.sexo}, numero_telefono={self.numero_telefono}, domicilio={self.domicilio})"

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, fecha_nacimiento, sexo: str, numero_telefono: int, domicilio: str, puesto: str, salario: float):
        super().__init__(nombre, edad, fecha_nacimiento, sexo, numero_telefono, domicilio)
        self.puesto = puesto
        self.salario = salario

    def to_string(self):
        return f"Empleado|{self.nombre}|{self.edad}|{str(self.fecha_nacimiento)}|{self.sexo}|{self.numero_telefono}|{self.domicilio}|{self.puesto}|{self.salario}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        return cls(parts[1], int(parts[2]), datetime.datetime.fromisoformat(parts[3]).date(), parts[4], int(parts[5]), parts[6], parts[7], float(parts[8]))

    def __str__(self):
        return f"Empleado({super().__str__()}, puesto={self.puesto}, salario={self.salario})"
    
class Cliente(Persona):
    def __init__(self, nombre: str, edad: int, fecha_nacimiento, sexo: str, numero_telefono: int, domicilio: str, numero_cliente):
        super().__init__(nombre, edad, fecha_nacimiento, sexo, numero_telefono, domicilio)
        self.numero_cliente = numero_cliente
        
    def to_string(self):
        return f"Cliente|{self.nombre}|{self.edad}|{str(self.fecha_nacimiento)}|{self.sexo}|{self.numero_telefono}|{self.domicilio}|{self.numero_cliente}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        return cls(parts[1], int(parts[2]), datetime.datetime.fromisoformat(parts[3]).date(), parts[4], int(parts[5]), parts[6], parts[7])
        
    def __str__(self):
        return f"Cliente({super().__str__()}, numero_cliente={self.numero_cliente})"

class Trabajo:
    def __init__(self, id_trabajo: int, dispositivo: Dispositivo, cliente: Cliente, empleado: Empleado, descripcion: str, costo_estimado: float):
        self.id_trabajo = id_trabajo
        self.dispositivo = dispositivo
        self.cliente = cliente
        self.empleado = empleado
        self.descripcion = descripcion
        self.costo_estimado = costo_estimado
        self.costo_real = 0.0
        self.fecha_inicio = None  # datetime
        self.fecha_fin = None     # datetime
        self.estado = "pendiente"   

    def to_string(self):
        fecha_inicio_str = str(self.fecha_inicio) if self.fecha_inicio else "None"
        fecha_fin_str = str(self.fecha_fin) if self.fecha_fin else "None"
        return f"Trabajo|{self.id_trabajo}|{self.dispositivo.to_string()}|{self.cliente.to_string()}|{self.empleado.to_string()}|{self.descripcion}|{self.costo_estimado}|{self.costo_real}|{fecha_inicio_str}|{fecha_fin_str}|{self.estado}"
    
    @classmethod
    def from_string(cls, s):
        parts = s.split("|")
        dispositivo = Dispositivo.from_string("|".join(parts[2:7]))  # Ajustar según formato
        cliente = Persona.from_string("|".join(parts[7:15]))  # Ajustar
        empleado = Persona.from_string("|".join(parts[15:24]))  # Ajustar
        trabajo = cls(int(parts[1]), dispositivo, cliente, empleado, parts[24], float(parts[25]))
        trabajo.costo_real = float(parts[26])
        trabajo.fecha_inicio = datetime.datetime.fromisoformat(parts[27]) if parts[27] != "None" else None
        trabajo.fecha_fin = datetime.datetime.fromisoformat(parts[28]) if parts[28] != "None" else None
        trabajo.estado = parts[29]
        return trabajo

    def iniciar_trabajo(self):
        if self.estado == "pendiente":
            self.fecha_inicio = datetime.datetime.now()
            self.estado = "en_progreso"
            print(f"Trabajo {self.id_trabajo} iniciado.")
        else:
            print("El trabajo ya está en progreso o completado.")

    def finalizar_trabajo(self, costo_real: float):
        if self.estado == "en_progreso":
            self.fecha_fin = datetime.datetime.now()
            self.costo_real = costo_real
            self.estado = "completado"
            print(f"Trabajo {self.id_trabajo} completado.")
        else:
            print("El trabajo no está en progreso.")

    def __str__(self):
        return f"Trabajo(id={self.id_trabajo}, dispositivo={self.dispositivo.modelo}, cliente={self.cliente.nombre}, empleado={self.empleado.nombre}, estado={self.estado}, costo_estimado={self.costo_estimado}, costo_real={self.costo_real})"

class Negocio:
    def __init__(self, inventario: list[Dispositivo], personal: list[Empleado], clientela: list[Cliente]):
        self.inventario = inventario
        self.personal = personal
        self.clientela = clientela
        self.trabajos: list[Trabajo] = []  
        self.contador_trabajos = 0  
        self.cargar_datos()
    
    def cargar_datos(self):
        # Cargar inventario
        try:
            with open("programa/inventario.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        dispositivo = Dispositivo.from_string(line.strip())
                        self.inventario.append(dispositivo)
        except FileNotFoundError:
            pass

        try:
            with open("programa/personal.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        empleado = Persona.from_string(line.strip())
                        self.personal.append(empleado)
        except FileNotFoundError:
            pass
  
        try:
            with open("programa/clientela.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        cliente = Persona.from_string(line.strip())
                        self.clientela.append(cliente)
        except FileNotFoundError:
            pass
        
        # Cargar trabajos
        try:
            with open("programa/trabajos.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        trabajo = Trabajo.from_string(line.strip())
                        self.trabajos.append(trabajo)
                        if trabajo.id_trabajo > self.contador_trabajos:
                            self.contador_trabajos = trabajo.id_trabajo
        except FileNotFoundError:
            pass
    
    def guardar_inventario(self):
        with open("programa/inventario.txt", "w", encoding="utf-8") as file:
            for disp in self.inventario:
                file.write(disp.to_string() + "\n")
    
    def guardar_personal(self):
        with open("programa/personal.txt", "w", encoding="utf-8") as file:
            for emp in self.personal:
                file.write(emp.to_string() + "\n")
    
    def guardar_clientela(self):
        with open("programa/clientela.txt", "w", encoding="utf-8") as file:
            for cli in self.clientela:
                file.write(cli.to_string() + "\n")
    
    def guardar_trabajos(self):
        with open("programa/trabajos.txt", "w", encoding="utf-8") as file:
            for trab in self.trabajos:
                file.write(trab.to_string() + "\n")

    def agregar_compu(self):
        opciones_procesador = ["intel", "amd"]
        
        tipo = input("Ingrese el tipo de computadora (laptop/escritorio): ")
        marca = input("Ingrese la marca de la computadora: ")
        modelo = input("Ingrese el modelo de la computadora: ")
        procesador = fn.validar_opcion("Ingrese el procesador (intel/amd): ", opciones_procesador)
        try:
            ram_gb = int(input("Ingrese la cantidad de RAM en GB: "))
        except ValueError:
            print("Error: RAM debe ser un número entero.")
            return
        
        computadora = Computadora(tipo=tipo, marca=marca, modelo=modelo, procesador=procesador, ram_gb=ram_gb)
        self.inventario.append(computadora)
        self.guardar_inventario()
        print("Computadora agregada al inventario.")

    def agregar_celu(self):
        opciones_sistema_operativo = ["android", "ios"]
        
        tipo = input("Ingrese el tipo de celular (smartphone/telefono basico): ")
        marca = input("Ingrese la marca del celular: ")
        modelo = input("Ingrese el modelo del celular: ")
        sistema_operativo = fn.validar_opcion("Ingrese el sistema operativo (android/ios): ", opciones_sistema_operativo)
        try:
            camara_megapixeles = int(input("Ingrese la cantidad de megapixeles de la camara: "))
        except ValueError:
            print("Error: Megapixeles debe ser un número entero.")
            return
        
        celular = Celular(tipo=tipo, marca=marca, modelo=modelo, sistema_operativo=sistema_operativo, camara_megapixeles=camara_megapixeles)
        self.inventario.append(celular)
        self.guardar_inventario()
        print("Celular agregado al inventario.")

    def crear_trabajo(self):
        if not self.inventario:
            print("No hay dispositivos en el inventario.")
            return
        print("Dispositivos disponibles:")
        for i, disp in enumerate(self.inventario):
            print(f"{i+1}. {disp}")
        try:
            id_disp = int(input("Seleccione el número del dispositivo: ")) - 1
            dispositivo = self.inventario[id_disp]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        if not self.clientela:
            print("No hay clientes registrados.")
            return
        print("Clientes disponibles:")
        for i, cli in enumerate(self.clientela):
            print(f"{i+1}. {cli.nombre}")
        try:
            id_cli = int(input("Seleccione el número del cliente: ")) - 1
            cliente = self.clientela[id_cli]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        if not self.personal:
            print("No hay empleados registrados.")
            return
        print("Empleados disponibles:")
        for i, emp in enumerate(self.personal):
            print(f"{i+1}. {emp.nombre}")
        try:
            id_emp = int(input("Seleccione el número del empleado: ")) - 1
            empleado = self.personal[id_emp]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return
        
        descripcion = input("Ingrese descripción del trabajo: ")
        try:
            costo_estimado = float(input("Ingrese costo estimado: "))
        except ValueError:
            print("Error: Costo debe ser un número.")
            return
        
        self.contador_trabajos += 1
        trabajo = Trabajo(self.contador_trabajos, dispositivo, cliente, empleado, descripcion, costo_estimado)
        self.trabajos.append(trabajo)
        self.guardar_trabajos()
        print(f"Trabajo {trabajo.id_trabajo} creado.")

    def actualizar_estado_trabajo(self):
        if not self.trabajos:
            print("No hay trabajos registrados.")
            return
        print("Trabajos disponibles:")
        for i, trab in enumerate(self.trabajos):
            print(f"{i+1}. {trab}")
        try:
            id = int(input("Seleccione el número del trabajo: ")) - 1
            trabajo = self.trabajos[id]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return
        
        accion = input("¿Iniciar (i) o finalizar (f) el trabajo? ").lower()
        if accion == "i":
            trabajo.iniciar_trabajo()
        elif accion == "f":
            try:
                costo_real = float(input("Ingrese costo real: "))
                trabajo.finalizar_trabajo(costo_real)
            except ValueError:
                print("Error: Costo debe ser un número.")
                return
        else:
            print("Acción inválida.")
        
        self.guardar_trabajos()

    def listar_trabajos(self):
        if not self.trabajos:
            print("No hay trabajos registrados.")
            return
        print("Lista de trabajos:")
        for trab in self.trabajos:
            print(trab)

if __name__ == "__main__":   
    negocio = Negocio(inventario=[], personal=[], clientela=[])


  


