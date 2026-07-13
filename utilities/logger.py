import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        log_dir = "logs"

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("AutomationFramework")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(
                "logs/test_execution.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger