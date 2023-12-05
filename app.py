from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys
logging.info("Welcome to custom log")

try:
    a = 4/"5"

except Exception as e:
    raise AppException(e,sys)

