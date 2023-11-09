import vec3

def write_color(out, pixel_color):
    # Escreve o valor traduzido [0,255] de cada componente de cor.
    out.write(f"{int(255.999 * pixel_color.x())} "
              f"{int(255.999 * pixel_color.y())} "
              f"{int(255.999 * pixel_color.z())}\n")
