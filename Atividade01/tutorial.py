import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

image_width = 256
image_height = 256

# Render
print("P3")
print(f"{image_width} {image_height}")
print("255")

# Inicie o logger e imprima as mensagens de log

for j in range(image_height):
    logger.info("Scanlines remaining: %d\r", image_height - j)
    for i in range(image_width):
        r = float(i) / (image_width - 1)
        g = float(j) / (image_height - 1)
        b = 0

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)

        print(f"{ir} {ig} {ib}")

logger.info("Done.\r")




