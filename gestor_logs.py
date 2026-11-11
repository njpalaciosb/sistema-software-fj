
import logging


def configurar_logger():
    """Configura el registro de eventos y errores del sistema."""

    logging.basicConfig(
        filename="software_fj.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("SoftwareFJ")


logger = configurar_logger()
