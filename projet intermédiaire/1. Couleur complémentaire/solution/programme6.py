def get_color_types(color: str) -> dict:
    """Retourne un dictionnaire des codes couleurs hex, rvb, tsl et tsl_norm
    à partir du code héxadécimal."""

    colors = {'hex': color,
              'rvb': hex_to_rvb(color)}
    tsl_norm, tsl = rvb_to_tsl(colors['rvb'])
    colors.update({'tsl_norm': tsl_norm, 'tsl': tsl})
    return colors

def get_complementary(color: str) -> str:
    """Retourne le code héxadécimal de la couleur complémentaire
    à la couleur donnée (au format héxadécimal)."""

    _, tsl = rvb_to_tsl(hex_to_rvb(color))
    teinte_complementary = teinte_complementaire(tsl[0])
    rvb = tsl_to_rvb([teinte_complementary, tsl[1], tsl[2]])
    return rvb_to_hex(rvb)

def hex_to_rvb(hexa: str) -> list[int]:
    """Convertion d'un code couleur hexadécimal en code RVB.
    ex: '#c47b55' -> [196, 123, 85]"""

    return [int(hexa[i:i+2], base=16) for i in range(1, 7, 2)]

def rvb_to_hex(rvb: list[int]) -> str:
    """Convertion d'un code couleur hexadécimal en code RVB.
    ex: [26, 13, 40] -> '#1a0d28'"""

    return '#' + ''.join(f'{hex(i)[2:].zfill(2)}' for i in rvb)

def rvb_to_tsl(rvb: list[int]) -> tuple[tuple[str], tuple[float]]:
    """Convertion d'une couleur au format RVB aux formats TSL_norm et TSL.
    ex: [13, 41, 37] -> (['171°', '52%', '11%'], [0.476, 0.519, 0.106])"""

    r, v, b = [i / 255 for i in rvb]
    maxi = max(r, v, b)
    mini = min(r, v, b)
    delta = maxi - mini

    if not delta:
        teinte = 0.0
    elif maxi == r:
        teinte = 60 * (((v - b) / delta) % 6)
    elif maxi == v:
        teinte = 60 * (((b - r) / delta) + 2)
    else:
        teinte = 60 * (((r - v) / delta) + 4)

    legerete = (maxi + mini) / 2
    saturation = delta / (1 - abs(2 * legerete - 1)) if delta else 0.0

    return (f'{round(teinte)}°', f'{saturation:.0%}', f'{legerete:.0%}'), \
           (teinte / 360, saturation, legerete)
def teinte_complementaire(teinte: float) -> float:
    """Retourne la teinte opposée sur le cercle chromatique."""

    return teinte - 0.5 if teinte >= 0.5 else teinte + 0.5

def tsl_to_rvb(tsl: list[float]) -> list[int]:
    """Convertion d'une couleur au format TSL aux formats RVB.
    ex: [0.190, 0.853, 0.547] -> [210, 238, 41]"""

    c = (1 - abs(2 * tsl[2] - 1)) * tsl[1]
    x = c * (1 - abs((tsl[0] * 6) % 2 - 1))
    m = tsl[2] - c / 2

    d = {60: (c, x, 0),
         120: (x, c, 0),
         180: (0, c, x),
         240: (0, x, c),
         300: (x, 0, c),
         360: (c, 0, x)}

    r, v, b = next(v for k, v in sorted(d.items()) if k > tsl[0] * 360)

    return [round((i + m) * 255) for i in (r, v, b)]

if __name__ == '__main__':
    from pprint import pprint

    hex_color = '#19021e'
    pprint(get_color_types(hex_color))
    print(get_complementary(hex_color))