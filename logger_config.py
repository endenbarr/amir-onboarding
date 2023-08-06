import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logger.log",
                    filemode='w',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
