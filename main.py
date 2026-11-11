
from entidades import Cliente
from servicios import Servicio, ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva

from excepciones import (
    ErrorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)

from gestor_logs import logger


class GestorSistema:
    """Administra los clientes, servicios y reservas de Software FJ."""

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def registrar_cliente(self, cliente):
        """Valida y registra un cliente."""

        if not isinstance(cliente, Cliente):
            raise ErrorCliente(
                "El objeto proporcionado no corresponde a un cliente."
            )

        for registrado in self.__clientes:
            if registrado.documento == cliente.documento:
                raise ErrorCliente(
                    "Ya existe un cliente registrado con ese documento."
                )

        self.__clientes.append(cliente)

        logger.info(
            "Cliente registrado en el sistema: %s",
            cliente.documento
        )

        return cliente

    def registrar_cliente_seguro(
        self,
        nombre,
        documento,
        correo,
        telefono
    ):
        """Registra un cliente y demuestra el encadenamiento de excepciones."""

        try:
            cliente = Cliente(
                nombre,
                documento,
                correo,
                telefono
            )

            self.registrar_cliente(cliente)

            return cliente

        except ErrorCliente as error:
            logger.exception(
                "Error durante el registro del cliente."
            )

            raise ErrorSistema(
                "No fue posible completar el registro del cliente."
            ) from error

    def registrar_servicio(self, servicio):
        """Valida y registra un servicio."""

        if not isinstance(servicio, Servicio):
            raise ErrorServicio(
                "El objeto proporcionado no corresponde a un servicio válido."
            )

        for registrado in self.__servicios:
            if registrado.nombre.lower() == servicio.nombre.lower():
                raise ErrorServicio(
                    "Ya existe un servicio registrado con ese nombre."
                )

        self.__servicios.append(servicio)

        logger.info(
            "Servicio registrado: %s",
            servicio.nombre
        )

        return servicio

    def crear_reserva(self, cliente, servicio, duracion):
        """Crea y registra una reserva."""

        if cliente not in self.__clientes:
            raise ErrorReserva(
                "El cliente no está registrado en el sistema."
            )

        if servicio not in self.__servicios:
            raise ErrorReserva(
                "El servicio no está registrado en el sistema."
            )

        reserva = Reserva(
            cliente,
            servicio,
            duracion
        )

        self.__reservas.append(reserva)

        logger.info(
            "Reserva agregada al sistema para el cliente %s.",
            cliente.documento
        )

        return reserva

    def mostrar_resumen(self):
        """Muestra el total de registros del sistema."""

        print("\n========== RESUMEN DEL SISTEMA ==========")
        print(f"Clientes registrados: {len(self.__clientes)}")
        print(f"Servicios registrados: {len(self.__servicios)}")
        print(f"Reservas registradas: {len(self.__reservas)}")
        print("=========================================")


def ejecutar_operacion(numero, descripcion, accion):
    """Ejecuta una operación controlando las posibles excepciones."""

    print(f"\nOPERACIÓN {numero}: {descripcion}")

    try:
        accion()

    except Exception as error:
        print(f"Error controlado: {error}")

        logger.exception(
            "Falló la operación %s: %s",
            numero,
            descripcion
        )

    else:
        print("Operación realizada correctamente.")

    finally:
        print(f"Finalización de la operación {numero}.")


def ejecutar_pruebas():
    """Ejecuta las operaciones de prueba del sistema Software FJ."""

    sistema = GestorSistema()

    cliente1 = None
    cliente2 = None

    sala = None
    equipo = None
    asesoria = None

    reserva1 = None
    reserva2 = None
    reserva3 = None

    # OPERACIÓN 1: Registrar un cliente válido.
    def prueba1():
        nonlocal cliente1

        cliente1 = sistema.registrar_cliente_seguro(
            "María Fernanda López",
            "1020304050",
            "maria@gmail.com",
            "3001234567"
        )

        print(cliente1.mostrar_informacion())

    ejecutar_operacion(
        1,
        "Registro de un cliente válido",
        prueba1
    )

    # OPERACIÓN 2: Intentar registrar un cliente con nombre vacío.
    def prueba2():
        sistema.registrar_cliente_seguro(
            "",
            "1020304051",
            "cliente@gmail.com",
            "3001234568"
        )

    ejecutar_operacion(
        2,
        "Registro de un cliente con nombre vacío",
        prueba2
    )

    # OPERACIÓN 3: Registrar un segundo cliente válido.
    def prueba3():
        nonlocal cliente2

        cliente2 = sistema.registrar_cliente_seguro(
            "Carlos Rodríguez",
            "1020304052",
            "carlos@gmail.com",
            "3001234569"
        )

        print(cliente2.mostrar_informacion())

    ejecutar_operacion(
        3,
        "Registro de un segundo cliente válido",
        prueba3
    )

    # OPERACIÓN 4: Crear un servicio de reserva de salas.
    def prueba4():
        nonlocal sala

        sala = ReservaSala(
            "Sala de reuniones",
            50000
        )

        sistema.registrar_servicio(sala)

        print(sala.mostrar_descripcion())

    ejecutar_operacion(
        4,
        "Creación y registro de un servicio de reserva de sala",
        prueba4
    )

    # OPERACIÓN 5: Crear un servicio de alquiler de equipos.
    def prueba5():
        nonlocal equipo

        equipo = AlquilerEquipo(
            "Alquiler de computador",
            80000
        )

        sistema.registrar_servicio(equipo)

        print(equipo.mostrar_descripcion())

    ejecutar_operacion(
        5,
        "Creación y registro de un servicio de alquiler de equipos",
        prueba5
    )

    # OPERACIÓN 6: Crear un servicio de asesoría.
    def prueba6():
        nonlocal asesoria

        asesoria = Asesoria(
            "Asesoría tecnológica",
            100000
        )

        sistema.registrar_servicio(asesoria)

        print(asesoria.mostrar_descripcion())

    ejecutar_operacion(
        6,
        "Creación y registro de un servicio de asesoría",
        prueba6
    )

    # OPERACIÓN 7: Intentar crear un servicio con tarifa negativa.
    def prueba7():
        servicio_invalido = ReservaSala(
            "Sala incorrecta",
            -5000
        )

        sistema.registrar_servicio(servicio_invalido)

    ejecutar_operacion(
        7,
        "Creación de un servicio con tarifa negativa",
        prueba7
    )

    # OPERACIÓN 8: Crear y confirmar una reserva de sala.
    def prueba8():
        nonlocal reserva1

        reserva1 = sistema.crear_reserva(
            cliente1,
            sala,
            2
        )

        print(reserva1.confirmar())
        print(reserva1.mostrar_informacion())

    ejecutar_operacion(
        8,
        "Creación y confirmación de una reserva de sala",
        prueba8
    )

    # OPERACIÓN 9: Crear y cancelar una reserva de equipo.
    def prueba9():
        nonlocal reserva2

        reserva2 = sistema.crear_reserva(
            cliente2,
            equipo,
            3
        )

        print(reserva2.cancelar())
        print(reserva2.mostrar_informacion())

    ejecutar_operacion(
        9,
        "Creación y cancelación de una reserva de equipo",
        prueba9
    )

    # OPERACIÓN 10: Crear, confirmar y procesar una asesoría.
    def prueba10():
        nonlocal reserva3

        reserva3 = sistema.crear_reserva(
            cliente1,
            asesoria,
            1
        )

        print(reserva3.confirmar())
        print(reserva3.procesar())
        print(reserva3.mostrar_informacion())

    ejecutar_operacion(
        10,
        "Creación y procesamiento de una reserva de asesoría",
        prueba10
    )

    # OPERACIÓN 11: Intentar crear una reserva con duración negativa.
    def prueba11():
        sistema.crear_reserva(
            cliente1,
            sala,
            -2
        )

    ejecutar_operacion(
        11,
        "Creación de una reserva con duración incorrecta",
        prueba11
    )

    # OPERACIÓN 12: Intentar procesar una reserva pendiente.
    def prueba12():
        reserva_pendiente = sistema.crear_reserva(
            cliente2,
            sala,
            1
        )

        reserva_pendiente.procesar()

    ejecutar_operacion(
        12,
        "Procesamiento de una reserva sin confirmar",
        prueba12
    )

    # OPERACIÓN 13: Demostrar las modalidades del cálculo del costo.
    def prueba13():

        costo_base = sala.calcular_costo(2)

        costo_descuento = sala.calcular_costo(
            2,
            descuento=10
        )

        costo_completo = sala.calcular_costo(
            2,
            descuento=10,
            impuesto=19
        )

        print(f"Costo base: ${costo_base:,.2f}")
        print(f"Costo con descuento: ${costo_descuento:,.2f}")
        print(
            f"Costo con descuento e impuesto: "
            f"${costo_completo:,.2f}"
        )

    ejecutar_operacion(
        13,
        "Cálculo del costo con diferentes parámetros",
        prueba13
    )

    # OPERACIÓN 14: Intentar registrar un documento duplicado.
    def prueba14():
        sistema.registrar_cliente_seguro(
            "Otro Cliente",
            "1020304050",
            "otro@gmail.com",
            "3009876543"
        )

    ejecutar_operacion(
        14,
        "Registro de un cliente con documento duplicado",
        prueba14
    )

    # OPERACIÓN 15: Intentar alquilar equipos por una fracción de día.
    def prueba15():
        equipo.calcular_costo(2.5)

    ejecutar_operacion(
        15,
        "Cálculo de alquiler de equipos con días fraccionados",
        prueba15
    )

    # OPERACIÓN 16: Intentar aplicar un descuento fuera del rango permitido.
    def prueba16():
        sala.calcular_costo(
            2,
            descuento=120
        )

    ejecutar_operacion(
        16,
        "Cálculo con descuento no permitido",
        prueba16
    )

    sistema.mostrar_resumen()


if __name__ == "__main__":

    print("==========================================")
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("==========================================")

    try:
        ejecutar_pruebas()

    except Exception as error:
        logger.exception(
            "Error general en la aplicación: %s",
            error
        )

        print(f"Error general controlado: {error}")

    finally:
        print("\nEjecución del sistema finalizada.")
        print("Consulte software_fj.log para revisar los registros.")
