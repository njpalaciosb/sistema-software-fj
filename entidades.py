
from abc import ABC, abstractmethod
import re

from excepciones import ErrorCliente
from gestor_logs import logger


class Entidad(ABC):
    """Clase abstracta que representa una entidad general del sistema."""

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto que deben implementar las clases derivadas."""
        pass


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, nombre, documento, correo, telefono):
        super().__init__(documento)

        self.__nombre = self._validar_nombre(nombre)
        self.__documento = self._validar_documento(documento)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

        logger.info("Cliente creado correctamente: %s", self.__documento)

    def _validar_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacío.")

        if len(nombre.strip()) < 3:
            raise ErrorCliente("El nombre debe tener al menos 3 caracteres.")

        return nombre.strip()

    def _validar_documento(self, documento):
        documento = str(documento).strip()

        if not re.fullmatch(r"[A-Za-z0-9-]{5,20}", documento):
            raise ErrorCliente(
                "El documento debe tener entre 5 y 20 caracteres "
                "y contener solo letras, números o guiones."
            )

        return documento

    def _validar_correo(self, correo):
        if not isinstance(correo, str):
            raise ErrorCliente("El correo debe ser un texto válido.")

        correo = correo.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.fullmatch(patron, correo):
            raise ErrorCliente("El formato del correo electrónico no es válido.")

        return correo

    def _validar_telefono(self, telefono):
        telefono = str(telefono).strip()

        if not re.fullmatch(r"\+?[0-9\s-]{7,18}", telefono):
            raise ErrorCliente("El número de teléfono no es válido.")

        return telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
