import logging


def logging_config():
    logging.basicConfig(
    #filename="quotes_mailer.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()])

    return logging.getLogger(__name__)