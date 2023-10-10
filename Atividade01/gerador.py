
import numpy as np
from PIL import Image


"""
Função que salva uma imagem em formato PPM

Parâmetros:
    image: imagem a ser salva
    filename: nome do arquivo a ser salvo

Retorno:
    Nenhum
"""
def save_as_ppm(image, filename):
    with open(filename, "w") as ppmfile:
        ppmfile.write("P3\n")
        ppmfile.write(f"{image.width} {image.height}\n")
        ppmfile.write("255\n")
        for j in range(image.height):
            for i in range(image.width):
                r, g, b = image.getpixel((i, j))
                ppmfile.write(f"{r} {g} {b} ")
            ppmfile.write("\n")


"""
Função que gera uma imagem com a silhueta escudo do São Paulo Futebol Clube

Parâmetros:
    width: largura da imagem
    height: altura da imagem

Retorno:
    Uma imagem com a silhueta do escudo do São Paulo Futebol Clube
"""
def create_spfc_image(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            #parte de cima
            if j < 50:
                img[j, i] = [255, 0, 0]
            #laterais
            elif i < 50 or i > 206:
                img[j, i] = [255, 0, 0]
            #diagonais
            elif i + 60 <= j:
                img[j, i] = [255, 0, 0]
            elif (i + j) - 60 >= (width - 1):
                img[j, i] = [255, 0, 0]
            #fundo
            else:
                img[j, i] = [255, 255, 255]
    return Image.fromarray(img)


"""
Função que gera uma imagem com um pôr do sol

Parâmetros:
    width: largura da imagem
    height: altura da imagem

Retorno:
    Uma imagem com um pôr do sol
"""
def create_sunset_image(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            #chão
            if j > 128:
                img[j, i] = [63, 53, 87]
            #sol
            elif (i - 128) ** 2 + (j - 128) ** 2 <= 64 ** 2:
                img[j, i] = [243, 181, 120]
            #céu
            else:
                img[j, i] = [247, 131, 118]
    return Image.fromarray(img)

"""
Função que gera uma imagem em forma de alvo

Parâmetros:
    width: largura da imagem
    height: altura da imagem

Retorno:
    Uma imagem em forma de alvo
"""
def create_target_image(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            if 100 <= i <= 140 and 100 <= j <= 140:
                img[j, i] = [167, 26, 91]
            elif 75 <= i <= 170 and 75 <= j <= 170:
                img[j, i] = [230, 134, 122]
            elif 50 <= i <= 200 and 50 <= j <= 200:
                img[j, i] = [237, 74, 106]
            elif 25 <= i <= 230 and 25 <= j <= 230:
                img[j, i] = [230, 134, 122]
            else:
                img[j, i] = [237, 74, 106]
    return Image.fromarray(img)


# Gere as imagens e salve-as
spfc_image = create_spfc_image(256, 256)
sunset_image = create_sunset_image(256, 256)
target_image = create_target_image(256, 256)

save_as_ppm(spfc_image, "spfc.ppm")
save_as_ppm(sunset_image, "sunset.ppm")
save_as_ppm(target_image, "target.ppm")

spfc_image.save("spfc.png")
sunset_image.save("sunset.png")
target_image.save("target.png")
