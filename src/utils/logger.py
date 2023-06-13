import logging
import os
from dotenv import load_dotenv

load_dotenv()
log_level = os.getenv('LOG_LEVEL', 'INFO')

logger = logging.getLogger(__name__)
logger.setLevel(log_level)

handler = logging.FileHandler('../logs.log')
handler.setLevel(log_level)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def getLogger():
    return logger