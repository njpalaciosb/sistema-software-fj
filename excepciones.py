class ErrorSistema(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ErrorValidacion(ErrorSistema):
    """Se produce cuando un dato no cumple las condiciones requeridas."""
    pass


class ErrorCliente(ErrorSistema):
    """Se produce cuando existe un problema con los datos del cliente."""
    pass


class ErrorServicio(ErrorSistema):
    """Se produce cuando un servicio no cumple las condiciones."""
    pass


class ErrorReserva(ErrorSistema):
    """Se produce cuando una reserva no puede realizarse."""
    pass


class ErrorEstadoReserva(ErrorReserva):
    """Se produce cuando una operación no es válida para el estado de la reserva."""
    pass