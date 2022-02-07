import logging
import logging.config

# import sys

loggers = logging.getLogger(__name__)
loggers.setLevel(logging.DEBUG)

logger_handler = logging.FileHandler(filename="/tmp/model-html.txt")
logger_handler.setLevel(logging.DEBUG)
# logger_handler = logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

logger_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

logger_handler.setFormatter(logger_formatter)

loggers.addHandler(logger_handler)
loggers.info("Completed configuring logger()!")
