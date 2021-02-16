from tkinter import *


def setup():
    
    global root, canvas, hue, hue_step, width, height, x, y, z, a, b, c, dt, amplitude
    
    width = height = 720
    
    root = Tk()
    canvas = Canvas(root, width=width, height=height, bg="#fff2fa")
    canvas.pack()
    
    hue = 0
    hue_step = 0.1
    
    x = 0.01
    y = 0
    z = 0
    
    a = 10
    b = 28
    c = 8 / 3
    
    dt = 0.008
    
    amplitude = 10

def draw():
    
    global x, y, z, hue
    
    x_old = x
    y_old = y
    z_old = z
    
    dx = (a * (y - x))*dt
    dy = (x * (b - z) - y)*dt
    dz = (x * y - c * z)*dt
    
    x = x + dx
    y = y + dy
    z = z + dz
    
    canvas.create_line(x_old * amplitude + width // 2, y_old * amplitude + height // 2, x * amplitude + width // 2, y * amplitude + height // 2, fill = _from_rgb(get_rgb_from_hsb(hue)))
    
    hue += hue_step
    
    root.after(1, draw)
    
def main():
    
    setup()
    draw()
    
    root.mainloop()
   
    
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
    
    

if __name__ == "__main__":
    main()