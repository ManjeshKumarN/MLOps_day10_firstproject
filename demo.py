from src.logger import logging

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

# So what happens?

# src.logger automatically refers to src/logger/__init__.py

# from src.logger import logging == from src.logger.__init__ import logging

# file A imports from src.logger import logging.

# on doing the above import , python loads and runs src/logger/__init__.py,because the code is defined in __int__.py file

# which internally runs configure_logger()  → root logger gets handlers. This configures the root logger. will use the same root logger, with the handlers already attached 

# Logging configuration is process-wide, not per file

# Any other file that imports logging or from src.logger import logging just inherits the already-configured root logger.

# Logging works everywhere automatically

# ----------------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException, MycustomException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MycustomException(e)

# -----------------------------------------------------
# for data ingestion
from src.pipline.training_pipeline import TrainPipeline
tp = TrainPipeline()
data_ingestion_artifacts = tp.start_data_ingestion()
print(data_ingestion_artifacts)