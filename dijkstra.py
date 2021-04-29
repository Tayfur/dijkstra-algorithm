
import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk

size = (width, height) = 640, 480
pygame.init()
Windows = pygame.display.set_mode(size)
clock = pygame.time.Clock()
cols, rows = 16, 16
w = width//cols
h = height//rows
matrix = []
queue, visited = deque(), []
path = []
class D_algorthm:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if random.randint(0, 100) < 20:
             self.wall = True
        
    def show(self, win, col, shape= 1):
        if self.wall == True:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(win, col, (self.x*w+w//2, self.y*h+h//2), w//3)
    
    def add_neighbors(self, matrix):
        if self.x < cols - 1:
            self.neighbors.append(matrix[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(matrix[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(matrix[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(matrix[self.x][self.y-1])

for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(D_algorthm(i, j))
    matrix.append(arr)

for i in range(cols):
    for j in range(rows):
        matrix[i][j].add_neighbors(matrix)

S = matrix[cols//17][rows//17]
L = matrix[cols-1][rows - cols//16]
S.wall = False
L.wall = False
queue.append(S)
S.visited = True
def main():
    flag = False
    noflag = True
    Sflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Sflag = True

        if Sflag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == L:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        print("Finish")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo('no way' )
                    noflag = False
                else:
                    continue


        Windows.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                D_algorthm = matrix[i][j]
                D_algorthm.show(Windows, (255, 255, 255))
                if D_algorthm in path:
                    D_algorthm.show(Windows, (192, 57, 43))
                elif D_algorthm.visited:
                    D_algorthm.show(Windows, (255, 255, 255))
                if D_algorthm in queue:
                    D_algorthm.show(Windows, (255, 255, 255))
                    D_algorthm.show(Windows, (255, 255, 255), 0)
                if D_algorthm == S:
                    D_algorthm.show(Windows, (0, 255, 200))
                if D_algorthm == L:
                    D_algorthm.show(Windows, (0, 120, 255))
                
                
        pygame.display.flip()


main()
