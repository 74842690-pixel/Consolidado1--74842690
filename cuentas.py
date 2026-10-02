
class CuentaBancaria:

    def _init_(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError(
                "El monto a depositar debe ser mayor que 0."
            )

        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError(
                "El monto a retirar debe ser mayor que 0."
            )

        if monto > self.__saldo:
            raise ValueError(
                "Saldo insuficiente para realizar el retiro."
            )

        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

    def _str_(self):
        return (
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Titular: {self.titular}\n"
            f"Saldo: S/ {self.__saldo:.2f}"
        )


# CUENTA DE AHORROS

class CuentaAhorros(CuentaBancaria):

    def _init_(self, numero_cuenta, titular, tasa_interes):
        super()._init_(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        saldo = self.consultar_saldo()
        return saldo * self.tasa_interes / 100

    def _str_(self):
        return (
            f"{super()._str_()}\n"
            f"Tasa de interés: {self.tasa_interes}%\n"
            f"Interés anual: S/ {self.calcular_interes():.2f}"
        )


# CUENTA CORRIENTE

class CuentaCorriente(CuentaBancaria):

    def _init_(self, numero_cuenta, titular, limite_sobregiro):
        super()._init_(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError(
                "El monto a retirar debe ser mayor que 0."
            )

        saldo_actual = self.consultar_saldo()

        if monto > saldo_actual + self.limite_sobregiro:
            raise ValueError(
                "El monto supera el límite de sobregiro permitido."
            )

        nuevo_saldo = saldo_actual - monto

        # Accedemos al saldo privado de la clase padre
        self.CuentaBancaria_saldo = nuevo_saldo

    def permite_sobregiro(self):
        return self.consultar_saldo() < 0

    def _str_(self):
        return (
            f"{super()._str_()}\n"
            f"Límite de sobregiro: S/ {self.limite_sobregiro:.2f}\n"
            f"Permite sobregiro: {self.permite_sobregiro()}"
        )


# PRUEBA DE CUENTA DE AHORROS


print(".....")
print("   CUENTA DE AHORROS")
print("....")

cuenta_ahorros = CuentaAhorros(
    "001-123456789",
    "Juan Perez",
    4.5
)

cuenta_ahorros.depositar(5000)

print("\nDespués del depósito:")
print(cuenta_ahorros)

cuenta_ahorros.retirar(1000)

print("\nDespués del retiro:")
print(cuenta_ahorros)

print(
    f"\nSaldo actual: S/ "
    f"{cuenta_ahorros.consultar_saldo():.2f}"
)

print(
    f"Interés anual calculado: S/ "
    f"{cuenta_ahorros.calcular_interes():.2f}"
)


# PRUEBA DE CUENTA CORRIENTE


print("\n.......")
print("  CUENTA CORRIENTE")
print(".....")

cuenta_corriente = CuentaCorriente(
    "002-987654321",
    "Maria Lopez",
    1000
)

cuenta_corriente.depositar(2000)

print("\nDespués del depósito:")
print(cuenta_corriente)

cuenta_corriente.retirar(2500)

print("\nDespués del retiro con sobregiro:")
print(cuenta_corriente)

print(
    f"\nSaldo actual: S/ "
    f"{cuenta_corriente.consultar_saldo():.2f}"
)

print(
    f"¿Permite sobregiro?: "
    f"{cuenta_corriente.permite_sobregiro()}"
)



# PRUEBA DE VALIDACIÓN

print("\n...........")
print("       PRUEBA DE VALIDACIONES")
print(".........")

try:
    cuenta_ahorros.depositar(-100)

except ValueError as error:
    print(f"Error al depositar: {error}")


try:
    cuenta_ahorros.retirar(10000)

except ValueError as error:
    print(f"Error al retirar: {error}")
