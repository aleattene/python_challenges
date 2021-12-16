

def hex_color_mixer(colors):
    # Data structures for homologous colors
    reds, greens, blues = [], [], []
    # Filling of data structures
    for color in colors:
        reds.append(int(color[1:3], 16))
        greens.append(int(color[3:5], 16))
        blues.append(int(color[5:7], 16))
    # Average of each color RGB
    redAvg = hex(round((sum(reds) / len(reds)+0.01)))[2:].upper().zfill(2)
    greenAvg = hex(round((sum(greens) / len(greens)+0.01)))[2:].upper().zfill(2)
    blueAvg = hex(round((sum(blues) / len(blues)+0.01)))[2:].upper().zfill(2)
    # Returns the hexadecimal code of the new color
    return '#' + redAvg + greenAvg + blueAvg
