
from abc import ABC, abstractmethod
import math

from excepciones import ErrorServicio
from gestor_logs import logger


class Servicio(ABC):
    """Clase abstracta que representa un servicio de Software FJ."""

    def __init__(self, nombre, tarifa_base, unidad_duracion):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if (
            not isinstance(tarifa_base, (int, float))
            or isinstance(tarifa_base, bool)
            or not math.isfinite(tarifa_base)
            or tarifa_base <= 0
        ):
            raise ErrorServicio(
                "La tarifa base debe ser un valor positivo."
            )

        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)
        self._unidad_duracion = unidad_duracion

        logger.info("Servicio creado: %s", self._nombre)

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def unidad_duracion(self):
        return self._unidad_duracion

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def mostrar_descripcion(self):
        pass

    def validar_duracion(self, duracion):

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ErrorServicio(
                "La duración debe ser un número positivo y válido."
            )

    def calcular_total(self, costo, descuento=0, impuesto=0):

        for valor, nombre in (
            (descuento, "El descuento"),
            (impuesto, "El impuesto")
        ):
            if (
                not isinstance(valor, (int, float))
                or isinstance(valor, bool)
                or not math.isfinite(valor)
                or not 0 <= valor <= 100
            ):
                raise ErrorServicio(
                    f"{nombre} debe estar entre 0 y 100."
                )

        subtotal = costo - (costo * descuento / 100)
        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)


class ReservaSala(Servicio):
    """Servicio de reserva de salas por horas."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "horas")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)

        costo_base = self.tarifa_base * duracion

        return self.calcular_total(
            costo_base,
            descuento,
            impuesto
        )

    def mostrar_descripcion(self):
        return (
            f"{self.nombre}: reserva de salas para reuniones "
            "y actividades empresariales. Tarifa por hora."
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos por días completos."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "días")

    def validar_duracion(self, duracion):

        if (
            not isinstance(duracion, int)
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ErrorServicio(
                "El alquiler de equipos debe tener una duración "
                "en días completos y positivos."
            )

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)

        costo_base = self.tarifa_base * duracion

        return self.calcular_total(
            costo_base,
            descuento,
            impuesto
        )

    def mostrar_descripcion(self):
        return (
            f"{self.nombre}: alquiler de equipos tecnológicos "
            "por días completos. Tarifa diaria."
        )


class Asesoria(Servicio):
    """Servicio de asesoría especializada por horas."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "horas")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)

        costo_base = self.tarifa_base * duracion

        return self.calcular_total(
            costo_base,
            descuento,
            impuesto
        )

    def mostrar_descripcion(self):
        return (
            f"{self.nombre}: asesoría especializada en soluciones "
            "tecnológicas. Tarifa por hora."
        )
