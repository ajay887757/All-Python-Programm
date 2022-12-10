import logging
logging.basicConfig(filename="abc.log",level=logging.ERROR,filemode="w")
# logging.basicConfig(level=logging.error)
print("Logging Demo")
logging.critical("This is critical Message")
logging.error("This is error Message")
logging.warning("This is warning Message")
logging.info("This is info Message")
logging.debug("This is debug message")
