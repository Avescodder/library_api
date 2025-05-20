import logging

def setup_logger(name='logger'):
    """
    Настраивает и возвращает логгер с заданной конфигурацией
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        httpx_logger = logging.getLogger("httpx")
        httpx_logger.setLevel(logging.WARNING)
    
    return logger


def get_logger():
    return setup_logger()