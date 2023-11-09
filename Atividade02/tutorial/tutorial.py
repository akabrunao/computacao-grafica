import math
import sys
from color import write_color
from vec3 import Vec3

# Configuração do logger
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

image_width = 256
image_height = 256

# Abrir o arquivo tutorial.pmm em modo de escrita
with open("Atividade02/tutorial/tutorial.ppm", "w") as ppm:
    # Render
    ppm.write("P3\n")
    ppm.write(f"{image_width} {image_height}\n")
    ppm.write("255\n")

    # Inicie o logger e imprima as mensagens de log
    for j in range(image_height):
        logger.info("Scanlines remaining: %d\r", image_height - j)
        for i in range(image_width):
            pixel_color = Vec3(i / (image_width - 1), j / (image_height - 1), 0)
            write_color(ppm, pixel_color)

    logger.info("Done.\r")
