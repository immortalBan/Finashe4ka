from tkinter import *
import BlackHoleClass
import PhotonClass

width = height = 720

root = Tk()
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()

start = height // 2

black_hole = BlackHoleClass.BlackHole(width / 2, height / 2, 30000, canvas)
photones = []

for i in range(0, start, 10):
    photones.append(PhotonClass.Photon(width - 20, i, canvas))

def show():
    canvas.delete("all")
    black_hole.show()
    for photone in photones:
        black_hole.pull(photone)
        photone.update()
        photone.show()
    root.after(10, show)
    black_hole.show_main_hole()

show()
root.mainloop()