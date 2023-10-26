from colorsys import rgb_to_hls, hls_to_rgb

def get_color_types(color:str) -> dict:    
    rvb = [int(color[i:i+2], 16) for i in range(1, len(color), 2)]
    tsl = list(rgb_to_hls(*list(map(lambda x: x/255, rvb))))
    tsl.insert(-1, tsl.pop())
    tsl_norm = (f"{round(tsl[0]*360)}°", *[f"{el:.0%}" for el in tsl[1:3]])
    return {"hex": color, "rvb": rvb, "tsl_norm": tsl_norm, "tsl": tuple(tsl)}

def get_complementary(color:str)->str:
    t, s, l = get_color_types(color)["tsl"]
    return f'#{"".join([f"{round(el*255):02x}" for el in hls_to_rgb(t+.5 % 1, l, s)])}'