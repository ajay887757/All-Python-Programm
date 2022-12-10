import logging

# logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p")


logging.critical("This is critical message")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")