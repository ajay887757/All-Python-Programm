import logging
import student_logging

logging.basicConfig(filename="student_log_info.log",level=logging.DEBUG)

logging.critical("This is critical massege by logging_module")
logging.error("This is error massege by logging_module")
logging.warning("This is warning massege by logging_module")
logging.info("This is info massege by logging_module")
logging.debug("This is debug massege by logging_module")