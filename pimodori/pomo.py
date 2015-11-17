import copy, random
import colorsys
import time
nohat = 0
try:
    import unicornhat as uh
except ImportError:
    print "no Unicornhat found"
    nohat = 1
import time

if not nohat:
    uh.brightness(.2)

def show_matrix(mat):
    for row in mat:
        print " ".join(str(x[0]) for x in row)

def uh_show_matrix(mat, pause = .075):
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            uh.set_pixel(x, y, mat[x][y][0], mat[x][y][1], mat[x][y][2])
            
    uh.show()
    time.sleep(pause)
        

def pomodoro(color = (255,0,0), min=25):
    for y in range(8):
        for x in range(8):
            uh.set_pixel(x, y, color[0], color[1], color[2])
    uh.show()
    for i in range(7,-1,-1):
        for j in range(7,-1,-1):
            time.sleep(min*60/64)
            uh.set_pixel(j,i, 0,0,0)
            uh.show()



if __name__ == "__main__":
    while 1: 
        pomodoro(min=25)
        pomodoro(color=(0,255,0), min=5)
