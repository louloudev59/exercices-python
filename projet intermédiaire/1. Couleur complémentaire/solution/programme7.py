# import des modules nécessaire
import colorsys

def get_color_types(color: str) -> dict:
    # Les nombres qui multiplierons le nombre de la couleur qui sont en RGB
    multiplicateurs = [360, 100, 100]
    # Variable contenant la couleur en hls (valeur comprise entre 0-255)
    color_ = color.lstrip("#")
    rvb = list(int(color_[i:i+2], 16) for i in (0, 2, 4))

    # Variable contenant la couleur en hls (valeur comprise entre 0-1)
    rvb_ = (i/255 for i in rvb)
    tsl = list(colorsys.rgb_to_hls(*rvb_))
    tsl[1], tsl[2] = tsl[2], tsl[1]
    # variable contenant la couleur tsl_norm
    tsl_norm = []
    for i in range(3):
        tsl_norm.append(str(int(tsl[i] * multiplicateurs[i])) + ("°", "%", "%")[i])
        
    return {"hex":color, "rvb": rvb, "tls_norm": tuple(tsl_norm), "tsl" : tsl}

def get_complementary(color: str) -> str:
    # Conversion de la couleur hexadécimale en RVB décimal
    rvb = [int(color[i:i+2], 16)/255 for i in (1, 3, 5)]
    # Conversion du RVB en HSV (Hue, Saturation, Value)
    hsv = list(colorsys.rgb_to_hsv(*rvb))
    # Inversion de la teinte (H) de manière diamétralement opposée sur le cercle des couleurs (ajout de 0,5)
    # J'inverse la teinte (de 180°) et je garde la saturation et la luminosité identique'
    hsv[0] = (hsv[0] + 0.5)
    # Conversion de la couleur complémentaire en RVB décimal
    comp_rvb = [int(val * 255) for val in colorsys.hsv_to_rgb(*hsv)]

    # Conversion des valeurs RVB complémentaires en format hexadécimal
    comp_color = "#{:02x}{:02x}{:02x}".format(*comp_rvb)
    return comp_color

color_hexa = "#19021e"
print(get_color_types(color_hexa))
print(get_complementary(color_hexa))