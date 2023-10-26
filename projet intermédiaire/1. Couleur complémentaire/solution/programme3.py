from PIL import ImageColor
import colorsys

def get_color_types(color:str):
    # Convertir format RVB hexa d'une couleur aux formats RVB décimal et TSL
    dictionnary = {}

    dictionnary["hex"] = color

    rgb = list(ImageColor.getcolor(color, "RGB"))
    dictionnary["rvb"] = rgb
    a, b, c = [*rgb]
    normalize = [a/255, b/255, c/255]

    hls = colorsys.rgb_to_hls(*normalize)
    hls = (hls[0], hls[2], hls[1])
    dictionnary["tsl"] = hls

    tsl_norm = (f"{str(round(hls[0]*360))}°", f"{round(hls[1]*100)}%", f"{round(hls[2]*100)}%")
    dictionnary["tsl_norm"] = tsl_norm


    return dictionnary


def get_complementary(color):

    dictionnary = get_color_types(color)

    compl = (dictionnary["tsl"][0]-0.5, dictionnary["tsl"][2], dictionnary["tsl"][1])
    rgb = colorsys.hls_to_rgb(*compl)
    r, g, b = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

    return f"#{r:02x}{g:02x}{b:02x}"