from colour import Color
from colorsys import rgb_to_hsv, hsv_to_rgb

hex_color = "#19021e"

#1
def get_color_types(color_hex):
    color = Color(hex_color)
    return {'hex': color_hex, 'rvb': [round(x*255) for x in color.get_rgb()], 'tsl_norm': tuple(f"{x}{'°' if i == 0 else '%'}" for i, x in enumerate([round(x * (360 if i == 0 else 100)) for i, x in enumerate(color.get_hsl())])), 'tsl': color.get_hsl()}

#2
print(get_color_types(hex_color))

def complementary(r, g, b):
   h, s, v = rgb_to_hsv(r, g, b)
   return hsv_to_rgb((h + 0.5) % 1, s, v)

#3
def get_complementary(color_hex):
    return Color(rgb=complementary(*Color(color_hex).get_rgb())).hex_l

print(get_complementary(hex_color))