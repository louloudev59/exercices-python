# Voici un exemple de code répondant à la consigne

from colorsys import rgb_to_hls

def get_color_types(color:str) -> dict:
    
    rvb = [int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)]
    tsl = rgb_to_hls(rvb[0]/255, rvb[1]/255, rvb[2]/255)
    tsl1 =(tsl[0], tsl[2], tsl[1])
    tsl_norm = f"({tsl[0] * 3.6:.0%}, {tsl[2]:.0%}, {tsl[1]:.0%})"
    
    return {
            "hex:":color,
            "rvb:":rvb,
            "tsl_norm:":tsl_norm,
            "tsl:":tsl1
            }

color = input("Veuillez entrer une couleur en héxadécimal : ")
print(get_color_types(color))

def get_complementary(color:str) -> str:
    tsl = get_color_types(color)["tsl"]
    tsl0 = tsl[0] + 0.5
    rgb = hls_to_rgb(tsl0 if tsl0 < 1 else tsl0 - 1, tsl[2], tsl[1])
    hex = list(map(lambda x: x*255, rgb))
    return '#%02x%02x%02x' % (int(hex[0]), int(hex[1]), int(hex[2]))