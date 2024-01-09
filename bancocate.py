class CuentaBancaria:
    def __init__(self, tipo, saldo=0, nombre=None, contrasena=None):
        # Inicialización de la cuenta con valores proporcionados
        self.tipo = tipo
        self.saldo = saldo
        self.extracciones_mes = 0
        self.nombre = nombre
        self.contrasena = contrasena

    def depositar(self, monto):
        # Método para realizar un depósito en la cuenta
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Saldo actual: ${self.saldo}")
        else:
            print("Monto inválido.")

    def extraer(self, monto):
        # Método para realizar una extracción de la cuenta
        if self.tipo == "caja_de_ahorro":
            if self.extracciones_mes < 10:
                if 0 < monto <= self.saldo:
                    self.saldo -= monto
                    self.extracciones_mes += 1
                    print(f"Extracción de ${monto} realizada. Saldo actual: ${self.saldo}")
                else:
                    print("Monto inválido o saldo insuficiente5.")
            else:
                print("Se alcanzó el límite de extracciones para este mes.")
        elif self.tipo == "cuenta_corriente":
            if monto > 0 and monto <= (self.saldo + 5000):
                self.saldo -= monto
                print(f"Extracción de ${monto} realizada. Saldo actual: ${self.saldo}")
            else:
                print("Monto inválido o excede el límite de sobregiro.")

def crear_cuenta():
    # Función para crear una nueva cuenta solicitando datos al usuario
    tipo_cuenta = input("Ingrese el tipo de cuenta (caja_de_ahorro/cuenta_corriente): ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    nombre = input("Ingrese el nombre de la cuenta: ")
    contrasena = input("Ingrese la contraseña de la cuenta: ")
    return CuentaBancaria(tipo_cuenta, saldo_inicial, nombre, contrasena)

def autenticar(cuentas):
    # Función para autenticar a un usuario comparando nombre y contraseña
    nombre = input("Ingrese el nombre de la cuenta: ")
    contrasena = input("Ingrese la contraseña: ")
    for index, c in enumerate(cuentas):
        if c.nombre == nombre and c.contrasena == contrasena:
            return index
    print("Autenticación fallida.")
    return None

def mostrar_info_cuentas(cuentas):
    # Función para mostrar información detallada de todas las cuentas
    if not cuentas:
        print("No hay cuentas disponibles.")
    else:
        print("Información de cuentas:")
        for index, cuenta in enumerate(cuentas):
            print(f"--- Cuenta {index} ---")
            print(f"Nombre: {cuenta.nombre}")
            print(f"Contraseña: {cuenta.contrasena}")
            print(f"Tipo de cuenta: {cuenta.tipo}")
            print(f"Saldo: ${cuenta.saldo}")
            print("--------------------")

def main():
    # Función principal que maneja el flujo del programa
    print("Bienvenido al sistema bancario.")
    cuentas = []
    
    while True:
        print("\nMenú:")
        print("1. Crear cuenta")
        print("2. Depositar")
        print("3. Extraer")
        print("4. Mostrar información de cuentas")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            cuenta_nueva = crear_cuenta()
            cuentas.append(cuenta_nueva)
            print("Cuenta creada exitosamente.")
        elif opcion == 2:
            if not cuentas:
                print("No hay cuentas disponibles.")
                continue
            num_cuenta = autenticar(cuentas)
            if num_cuenta is not None:
                monto = float(input("Ingrese el monto a depositar: "))
                cuentas[num_cuenta].depositar(monto)
        elif opcion == 3:
            if not cuentas:
                print("No hay cuentas disponibles.")
                continue
            num_cuenta = autenticar(cuentas)
            if num_cuenta is not None:
                monto = float(input("Ingrese el monto a extraer: "))
                cuentas[num_cuenta].extraer(monto)
        elif opcion == 4:
            mostrar_info_cuentas(cuentas)
        elif opcion == 5:
            print("Gracias por usar nuestro sistema.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
