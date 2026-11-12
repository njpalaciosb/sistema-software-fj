"""Clases de dominio: servicio abstracto y servicios especializados."""
from abc import ABC, abstractmethod
import math
from excepciones import ErrorServicio
from gestor_logs import logger


class Servicio(ABC):
    """Clase abstracta que define el comportamiento común de un servicio."""

    def __init__(self, nombre, tarifa_base, unidad_duracion):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")
        if (
            isinstance(tarifa_base, bool)
            or not isinstance(tarifa_base, (int, float))
            or not math.isfinite(tarifa_base)
            or tarifa_base <= 0
        ):
            raise ErrorServicio("La tarifa base debe ser un número positivo.")

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

    def validar_duracion(self, duracion):
        """Validación general: número finito y mayor que cero."""
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ErrorServicio("La duración debe ser un número positivo y válido.")

    @staticmethod
    def _validar_porcentaje(valor, etiqueta):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or not 0 <= valor <= 100
        ):
            raise ErrorServicio(f"{etiqueta} debe estar entre 0 y 100.")

    def calcular_total(self, costo, descuento=0, impuesto=0):
        """Aplica descuento e impuesto porcentuales al costo base."""
        self._validar_porcentaje(descuento, "El descuento")
        self._validar_porcentaje(impuesto, "El impuesto")
        subtotal = costo * (1 - descuento / 100)
        return round(subtotal * (1 + impuesto / 100), 2)

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Cada servicio define cómo se calcula su costo."""

    @abstractmethod
    def mostrar_descripcion(self):
        """Cada servicio proporciona su propia descripción."""

    def __str__(self):
        return f"{self.nombre} | ${self.tarifa_base:,.2f} por {self.unidad_duracion}"


class ReservaSala(Servicio):
    """Reserva de salas por horas."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "hora")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)
        return self.calcular_total(self.tarifa_base * duracion, descuento, impuesto)

    def mostrar_descripcion(self):
        return f"{self.nombre}: reserva de salas para reuniones y actividades empresariales. Tarifa por hora."


class AlquilerEquipo(Servicio):
    """Alquiler de equipos tecnológicos por días completos."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "día")

    def validar_duracion(self, duracion):
        # En este servicio solo se aceptan días enteros positivos.
        if isinstance(duracion, bool) or not isinstance(duracion, int) or duracion <= 0:
            raise ErrorServicio("El alquiler de equipos requiere días completos y positivos.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)
        return self.calcular_total(self.tarifa_base * duracion, descuento, impuesto)

    def mostrar_descripcion(self):
        return f"{self.nombre}: alquiler de equipos tecnológicos por días completos. Tarifa diaria."


class Asesoria(Servicio):
    """Asesoría especializada por horas."""

    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base, "hora")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_duracion(duracion)
        return self.calcular_total(self.tarifa_base * duracion, descuento, impuesto)

    def mostrar_descripcion(self):
        return f"{self.nombre}: asesoría especializada en soluciones tecnológicas. Tarifa por hora."
