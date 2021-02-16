from tkinter import *
import DropClass
from constants import *


def input_data():
    
    global drops_number
    
    drops_number = int(input("Введите количество капель на экране\n -> "))

def setup():
    
    global drops, root, canvas
    
    root = Tk()
    canvas = Canvas(root, width=width, height=height, bg="#fff2fa")
    canvas.pack()
    
    drops = []
    
    for _ in range(drops_number):
        drops.append(DropClass.Drop())

def motion():
    
    canvas.delete("all")
    
    for drop in drops:
        drop.fall()
        drop.show(canvas)
    
    root.after(10, motion)

def main():
    
    input_data()
    setup()
    motion()

    root.mainloop()
    

if __name__ == "__main__":
    main()
