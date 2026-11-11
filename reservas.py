
from datetime import datetime

from entidades import Cliente
from servicios import Servicio
from excepciones import ErrorReserva, ErrorEstadoReserva
from gestor_logs import logger


class Reserva:
    """Representa una reserva realizada por un cliente."""

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva(
                "La reserva debe estar asociada a un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ErrorReserva(
                "La reserva debe estar asociada a un servicio válido."
            )

        servicio.validar_duracion(duracion)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__fecha_creacion = datetime.now()
        self.__costo = 0.0

        logger.info(
            "Reserva creada para el cliente %s. Estado: Pendiente.",
            cliente.documento
        )

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    @property
    def costo(self):
        return self.__costo

    def calcular_costo(self, descuento=0, impuesto=0):
        """Calcula el costo utilizando el servicio asociado."""

        return self.__servicio.calcular_costo(
            self.__duracion,
            descuento,
            impuesto
        )

    def confirmar(self):
        """Confirma una reserva que se encuentre pendiente."""

        if self.__estado != "Pendiente":
            raise ErrorEstadoReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        costo_calculado = self.calcular_costo()

        self.__costo = costo_calculado
        self.__estado = "Confirmada"

        logger.info(
            "Reserva confirmada. Cliente: %s. Costo: %.2f",
            self.__cliente.documento,
            self.__costo
        )

        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise ErrorEstadoReserva(
                "No se puede cancelar una reserva que ya fue procesada "
                "o cancelada."
            )

        self.__estado = "Cancelada"

        logger.warning(
            "Reserva cancelada para el cliente %s.",
            self.__cliente.documento
        )

        return "La reserva fue cancelada correctamente."

    def procesar(self):
        """Procesa una reserva previamente confirmada."""

        if self.__estado != "Confirmada":
            raise ErrorEstadoReserva(
                "Solo se pueden procesar reservas confirmadas."
            )

        self.__estado = "Procesada"

        logger.info(
            "Reserva procesada para el cliente %s.",
            self.__cliente.documento
        )

        return "La reserva fue procesada correctamente."

    def mostrar_informacion(self):
        """Devuelve un resumen de la reserva."""

        return (
            "\n--- INFORMACIÓN DE LA RESERVA ---\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Documento: {self.__cliente.documento}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} "
            f"{self.__servicio.unidad_duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}\n"
            f"Fecha: {self.__fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}"
        )
