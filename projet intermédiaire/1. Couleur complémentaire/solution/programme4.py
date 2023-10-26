import colorsys

def get_color_types(hex):
    #suppression du # du hexadecimal
    hex_to_convert = hex.lstrip('#')

    #RGB
    #conversion par groupe de 2 en base 16 => rgb
    rgb = list(int(hex_to_convert[i:i+2], 16) for i in (0, 2, 4))

    #TSL - tls norm
    #Récupération des valeurs RGB et changement de plage avant envoie dans la fonction colorsys
    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0
    
    tsl_convert = colorsys.rgb_to_hls(r, g, b)
    tsl = (tsl_convert[0], tsl_convert[2], tsl_convert[1])

    #HLS - tsl
    #Mise en degré pour le h et en pourcentage pour s et l
    h = round(tsl_convert[0] * 360) 
    l = round(tsl_convert[1] * 100)
    s = round(tsl_convert[2] * 100)

    hls = (f"{h}°", f"{s}%", f"{l}%")

    #Création du dictionnaire
    dict = {
        'hex': hex,
        'rvb': rgb,
        'tls_norm': hls,
        'tsl':tsl
    }
    return dict

def get_complenentary(color):
    #Récupération des valeurs tsl avant arrondi
    dict = get_color_types(color)
    tsl_convert = dict[0]["tsl"]

    #Mise en degré pour le h et en pourcentage pour s et l
    h = tsl_convert[0] * 360
    l = tsl_convert[2] * 100
    s = tsl_convert[1] * 100

    #Rotation de 180° du h pour la complémentaire
    h = h + 180
    
    if h > 360:
        h = h - 360
  
    #Mise en RGB
    rgb = colorsys.hls_to_rgb(h/360, l/100, s/100)

    r = int(rgb[0] * 255)
    g = int(rgb[1] * 255)
    b = int(rgb[2] * 255)

    #Conversion en hexadécimal
    hex1 = hex(r)[2:] if len(hex(r)[2:]) > 1 else f"O{hex(r)[2:]}"
    hex2 = hex(g)[2:] if len(hex(g)[2:]) > 1 else f"O{hex(g)[2:]}"
    hex3 = hex(b)[2:] if len(hex(b)[2:]) > 1 else f"O{hex(b)[2:]}"

    hexadecimal = f"#{hex1}{hex2}{hex3}"
    return f"{color} => {hexadecimal}"

print(get_color_types("#19021e"))
print("\n############################\n")
print(get_complenentary("#19021e"))