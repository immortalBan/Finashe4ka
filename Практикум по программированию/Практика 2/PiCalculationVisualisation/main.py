from tkinter import *
import math

pi = 4
iterations = 0
maxIteration = 1000
i_start = 0
j_start = 1
pi_start = 1

minY = 2;
maxY = 4;

history = []

width = 1080
height = 720

ans = input('Выберите:\n 1.Ряд Лейбница\n 2.Ряд Валлиса\n -> ')

root = Tk()
canvas = Canvas(root, width=width, height=height, bg="black")
canvas.pack()

def mapping(number, range1_1, range1_2, range2_1, range2_2):
    
    delta1 = range1_2 - range1_1
    delta2 = range2_2 - range2_1
    
    return (delta2 * (number - range1_1) / delta1) + range2_1

piY = mapping(math.pi, minY, maxY, height, 0)

def leibniz_formula ():
    
    global pi, iterations, history 
    
    if iterations == maxIteration:
        canvas.create_text(540, 60, text = "Iteration 1000", font = ('Arial' ,80), fill = 'white')
        return
    
    den = iterations * 2 + 3
    
    if iterations % 2 == 0:
        pi -= (4 / den)
    else:
        pi += (4 / den)
        
    history.append(pi)
    
    spacing = width / len(history)
    
    canvas.delete("all")
    
    canvas.create_line(0, piY, width, piY, fill = 'white')
    
    canvas.create_text(540, 660, text = pi, font = ('Arial' ,80), fill = 'white')
    
    for i in range(len(history)-1):
        x1 = i * spacing
        x2 = (i+1) * spacing
        y1 = mapping(history[i], minY, maxY, height, 0)
        y2 = mapping(history[i+1], minY, maxY, height, 0)
        canvas.create_line(x1, y1, x2, y2, fill = 'white')
    
    iterations += 1
    
    root.after(1, leibniz_formula)


def wallis_formula ():
    
    global pi_start, iterations, history, i_start, j_start
    
    if iterations == maxIteration:
        canvas.create_text(540, 60, text = "Iteration 1000", font = ('Arial' ,80), fill = 'white')
        return
    
    if iterations % 2 == 0:
        i_start += 2
    else:
        j_start += 2
    
    pi_start *= i_start / j_start
    
    history.append(pi_start * 2)
    
    spacing = width / len(history)
    
    canvas.delete("all")
    
    canvas.create_line(0, piY, width, piY, fill = 'white')
    
    canvas.create_text(540, 660, text = pi_start * 2, font = ('Arial' ,80), fill = 'white')
    
    for i in range(len(history)-1):
        x1 = i * spacing
        x2 = (i+1) * spacing
        y1 = mapping(history[i], minY, maxY, height, 0)
        y2 = mapping(history[i+1], minY, maxY, height, 0)
        canvas.create_line(x1, y1, x2, y2, fill = 'white')
    
    iterations += 1
    
    root.after(1, wallis_formula)
    
if ans == '1':
    leibniz_formula()
elif ans == '2':
    wallis_formula()   

root.mainloop()
