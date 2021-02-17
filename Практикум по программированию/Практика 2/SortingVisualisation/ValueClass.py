import random

def get_rgb_from_hsb (hue, saturation = 100, brightness = 100):
    
    h_i = (hue // 60) % 6
    b_min = (100 - saturation) / 100 * brightness
    a = (brightness - b_min) * (hue % 60) / 60
    b_inc = b_min + a
    b_dec = brightness - a
    
    if h_i == 0:
        return int(brightness * 255 / 100), int(b_inc * 255 / 100), int(b_min * 255 / 100)
    elif h_i == 1:
        return int(b_dec * 255 / 100), int(brightness * 255 / 100), int(b_min * 255 / 100)
    elif h_i == 2:
        return int(b_min * 255 / 100), int(brightness * 255 / 100), int(b_inc * 255 / 100)
    elif h_i == 3:
        return int(b_min * 255 / 100), int(b_dec * 255 / 100), int(brightness * 255 / 100)
    elif h_i == 4:
        return int(b_inc * 255 / 100), int(b_min * 255 / 100), int(brightness * 255 / 100)
    elif h_i == 5:
        return int(brightness * 255 / 100), int(b_min * 255 / 100), int(b_dec * 255 / 100)

def _from_rgb(rgb):

    return "#%02x%02x%02x" % rgb

def renormalize(n, range1, range2):
    
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    
    return (delta2 * (n - range1[0]) / delta1) + range2[0]

class Value:
    
    def __init__(self, value_range):
        self.value_range = value_range
        self.value = random.randint(self.value_range[0], self.value_range[1])
        self.set_color()
    
    def set_color(self):
        self.color = _from_rgb(get_rgb_from_hsb(renormalize(self.value, (self.value_range[0], self.value_range[1]), (0, 360))))
    