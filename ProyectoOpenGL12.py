#Cristian Perez
#Cubo
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GLUT as GLUT
import sys
from PIL import Image as Image
import numpy
from math import *


tree_vertices = (

    (9,-1,-1),#0
    (9,3,-1),#1
    (7,3,-1),#2
    (7,-1,-1),#3
    (9,-1,1),#4
    (9,3,1),#5
    (7,-1,1),
    (7,3,1),
    (8,6,0)
    )

tree_edges =(
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (1,8),
    (2,8),
    (5,8),
    (7,8)
    
    )

tree_surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    (1,8,2,1),
    (1,8,5,1),
    (7,8,2,7),
    (5,8,7,5),
    

    )

def Tree():
    glBegin(GL_QUADS)
    for edge in tree_edges:
        for vertex in edge:
            glColor3fv((0.5,0.5,1))
            glVertex3fv(tree_vertices[vertex])
            
    glEnd()

def Tree_wireframe():
    glBegin(GL_LINES)
    for edge in tree_edges:
        for vertex in edge:
            glColor3fv((0.5,0.5,1))
            glVertex3fv(tree_vertices[vertex])
            
    glEnd()


vertices = (
    (1,-1,-1),#0
    (1,1,-1),#1
    (-1,1,-1),#2
    (-1,-1,-1),#3
    (1,-1,1),#4
    (1,1,1),#5
    (-1,-1,1),
    (-1,1,1),
    (-0.33,-1,1),
    (0.33,-1,1),
    (-0.33,0,1),
    (0.33,0,1),
    (0,2,0),
    (-0.33,-1,1),
    (0.33,-1,1),
    (-0.33,0,1),
    (0.33,0,1)
    )
edgies = (
    (13,14),
    (13,15),
    (14,16),
    (15,16)
    )

box_vertices = (
   (10,-3,-10),#0
    (10,-1.1,-10),#1
    (-10,-1.1,-10),#2
    (-10,-3,-10),#3
    (10,-3,10),#4
    (10,-1.1,10),#5
    (-10,-3,10),
    (-10,-1.1,10),
    
    )


floor_vertices = (

    (-10,-1.55,20),
    (10,-1.55,20),
    (-10,-1.55,-300),
    (10,-1.55,-300)

    )


sphere_vertices =(
    (0,20,0),
    (0,-20,0),
    (20,0,0),
    (-20,0,0),
    (0,0,75),
    (0,0,-75),
    

    )

sphere_edges =(
    (0,2),
    (0,3),
    (0,4),
    (0,5),
    (1,2),
    (1,3),
    (1,4),
    (1,5),
    

    )

def Cone():
    glPushMatrix()
    glTranslatef(6,0,0)
    quadric1 = gluNewQuadric()
    gluQuadricDrawStyle(quadric1, GLU_FILL )
    gluCylinder( quadric1,4,0,4,36,18)
    gluDeleteQuadric(quadric1)
    glPopMatrix()
     

def rawSphere( x,y,z):

    glPushMatrix()


    glRotatef( x, 1.0, 0.0, 0.0)
    glRotatef( y, 0.0, 1.0, 0.0)
    glRotatef( z, 0.0, 0.0, 1.0)


    glLineWidth( 3.0 )
    glColor3f( 1, 1, 1)

    quadric = gluNewQuadric()

    gluQuadricDrawStyle(quadric, GLU_FILL )
    gluSphere( quadric , 10 , 36 , 18 )

    gluDeleteQuadric(quadric)


    glPopMatrix()

def ground():
    glBegin(GL_QUADS)
    for vertex in floor_vertices:
        glColor3fv((0,0.5,0.5))
        glVertex3fv(vertex)
    glEnd()

def ground_wireframe():
    glBegin(GL_LINES)
    for vertex in floor_vertices:
        glColor3fv((0,0.5,0.5))
        glVertex3fv(vertex)
    glEnd()

def sphere():
    glBegin(GL_LINES)
    for edge in sphere_edges:
        for vertex in edge:
            glVertex3fv(sphere_vertices[vertex])

    glEnd()

box_edges =(
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)

    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    #(6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (6,8), #punto izquierdo de la puerta
    (9,4), #punto derecho de la puerta(este y el anterior son inferiores)
    (8,10),
    (9,11),
    (10,11),
    (1,12),
    (2,12),
    (5,12),
    (7,12)
    
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    (1,12,2,1),
    (1,12,5,1),
    (7,12,2,7),
    (5,12,7,5),
    (13,14,16,15)
    )

box_surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)

    )

colors = (

    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1)

    )

def Cube():
    glBegin(GL_QUADS)
   
    for surface in surfaces:
        x=0
       
        #glColor3fv((1,0,0))
        for vertex in surface:
            x+=1
            if vertex<=12:
                glColor3fv(colors[x])
                #glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
                glVertex3fv(vertices[vertex])
    glEnd()

    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()


def Cube_wireframe():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def Door():
    glBegin(GL_QUADS)

    for surface in surfaces:
        #glColor3fv((1,0,0))
    

        for vertex in surface:
            if vertex>12:
                glColor3fv((1,0,0))
                glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edgies:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    
def Floor():
    glBegin(GL_QUADS)
   
    for surface in box_surfaces:
        x=0
       
        #glColor3fv((1,0,0))
        for vertex in surface:
            x+=1
            
            glColor3fv((0,1,0))
            glVertex3fv(box_vertices[vertex])
    glEnd()

    
    glBegin(GL_LINES)
    for edge in box_edges:
        for vertex in edge:
            glVertex3fv(box_vertices[vertex])

    glEnd()





def Circle():
    posx, posy = 0,0    
    sides = 32    
    radius = 1    
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def main():
    Load=0
    Key_enable=0
    house1=0
    pygame.init()
    display = (800,600)
    
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    surface =pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
    
    glTranslatef(0,0,-50)

    #glRotatef(25,2,1,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)
                if event.key == pygame.K_m:
                    glScale(1.1,1.1,1.1)
                if event.key == pygame.K_n:
                    glScale(0.9,0.9,0.9)

                if event.key ==pygame.K_i:
                    if Load ==0:
                        Load= 1
                    elif Load ==1:
                        Load = 2
                    elif Load ==2:
                        Load = 0
                if event.key ==pygame.K_c:
                    Load=0
                    house1=0

                if event.key == pygame.K_e:
                   Key_enable=1
                if event.key == pygame.K_c:
                   Key_enable=0
                    
                        
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==4:
                    glTranslatef(0,0,1)

                if event.button ==5:
                    glTranslatef(0,0,-1)
                

                    
                    

                
        #glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if Load ==0 and Key_enable==0:
            glPushMatrix()
            glTranslatef(0,0,50)
            rawSphere(10,20,0)
            glPopMatrix()
            Cube()
            Door()
            ground()
            Tree()
          
           
          
            #Cone()
        if Load ==0 and Key_enable==1:
            #Cube()
            Cube_wireframe()
            #Door()
            #ground()
            ground_wireframe()
            Tree_wireframe()
            

          
            
        if Load==1:
            if house1==0:
                glLoadIdentity()
                display = (800,600)
                pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
                gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
                glTranslatef(0,0,-15)
               # glRotatef(25,2,1,0)
                house1=1
            glPushMatrix()
            glTranslatef(-1.33,0,3.5)
            glRotatef(90,0,1,0)
            
            Door()
            glPopMatrix()
            Cube()
            #Sphere_show()
          
                        
            
        if Load==2:
            if house1==0:
                glLoadIdentity()
                display = (800,600)
                pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
                gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
                glTranslatef(0,0,-15)
               # glRotatef(25,2,1,0)
                glScale()
                house=1
            Cube()
            Door()
           
        pygame.display.flip()
        pygame.time.wait(10)

main()
    