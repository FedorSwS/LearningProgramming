import logging
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cosinus(degree):
    radian = degree*math.pi/180
    result = math.cos(radian)
    logger.info(f"Вычислен Косинус {degree} градусов) = {result:.3f}")
    return result

def run():
    logger.info("Приложение запущено")
    value = cosinus(180)
    print(f"Результат: {value:.3f}")
    logger.info("Приложение завершено")

if __name__ == "__main__": 
    print(__name__)
    run()
