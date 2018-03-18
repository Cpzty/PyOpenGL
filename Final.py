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
import winsound
from texture import *


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

def Cube_texture():
    smurf  = pygame.image.load("brick.png")
    bronze = pygame.image.tostring(smurf, "RGBA", 1)

    width = smurf.get_width()
    height = smurf.get_height()

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
    GL_UNSIGNED_BYTE, bronze)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-8.0, -4.0,  4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f( -4.0, -4.0,  4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f( -4.0,  4.0,  4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(-8.0,  4.0,  4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(-8.0, -4.0, -4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f(-8.0,  4.0, -4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f( -4.0,  4.0, -4.0);
    glTexCoord2f(0.0, 0.0); glVertex3f( -4.0, -4.0, -4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(-8.0,  4.0, -4.0);
    glTexCoord2f(0.0, 0.0); glVertex3f(-8.0,  4.0,  4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f( -4.0,  4.0,  4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f( -4.0,  4.0, -4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f(-8.0, -4.0, -4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f( -4.0, -4.0, -4.0);
    glTexCoord2f(0.0, 0.0); glVertex3f( -4.0, -4.0,  4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(-8.0, -4.0,  4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f( -4.0, -4.0, -4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f( -4.0,  4.0, -4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f( -4.0,  4.0,  4.0);
    glTexCoord2f(0.0, 0.0); glVertex3f( -4.0, -4.0,  4.0);
    glTexCoord2f(0.0, 0.0); glVertex3f(-8.0, -4.0, -4.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(-8.0, -4.0,  4.0);
    glTexCoord2f(1.0, 1.0); glVertex3f(-8.0,  4.0,  4.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(-8.0,  4.0, -4.0);
    glEnd()


def main():
    shear_factor = -10.1
    play_sound =0
    shear_m = (
    (1,0,0,0),
    (0,1,0,0),
    (0,0,shear_factor,0),
    (0,0,0,1)
    )

    Load=0
    Key_enable=0
    house1=0
    izquierda =0
    #dado las restricciones necesito incrementar la variable
    mov_izquierda_derecha =0
    mov_izquierda_derecha_wireframe =0
    #arriba abajo
    mov_arriba_abajo =0
    mov_arriba_abajo_wireframe =0

    #rotacion casa
    casa_rota_z =0
    casa_rota_z_wireframe =0

    #rotacion arbol
    arbol_rota_z =0
    arbol_rota_z_wireframe =0
    
    #dado las restricciones necesito incrementar la variable
    casa_mov_izquierda_derecha =0
    casa_mov_izquierda_derecha_wireframe =0
    #arriba abajo
    casa_mov_arriba_abajo =0
    casa_mov_arriba_abajo_wireframe =0
    #Scaling prefiero que se escale todo pero por si las moscas
    scale_casa =0
    scale_arbol =1
    
    
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

            #Casa con WASD y arbol con Flechas    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   izquierda =1
                   mov_izquierda_derecha=mov_izquierda_derecha-0.5
                   mov_izquierda_derecha_wireframe=mov_izquierda_derecha_wireframe-0.5
                if event.key == pygame.K_RIGHT:
                    mov_izquierda_derecha=mov_izquierda_derecha+0.5
                    mov_izquierda_derecha_wireframe=mov_izquierda_derecha_wireframe+0.5
                if event.key == pygame.K_UP:
                    mov_arriba_abajo = mov_arriba_abajo +0.5
                    mov_arriba_abajo_wireframe = mov_arriba_abajo_wireframe +0.5
                if event.key == pygame.K_DOWN:
                    mov_arriba_abajo = mov_arriba_abajo -0.5
                    mov_arriba_abajo_wireframe = mov_arriba_abajo_wireframe -0.5

                if event.key == pygame.K_w:
                    casa_mov_arriba_abajo = casa_mov_arriba_abajo +0.5
                    casa_mov_arriba_abajo_wireframe = casa_mov_arriba_abajo_wireframe +0.5
                if event.key == pygame.K_s:
                    casa_mov_arriba_abajo = casa_mov_arriba_abajo -0.5
                    casa_mov_arriba_abajo_wireframe = casa_mov_arriba_abajo_wireframe -0.5
                if event.key == pygame.K_a:
                    casa_mov_izquierda_derecha=casa_mov_izquierda_derecha-0.5
                    casa_mov_izquierda_derecha_wireframe=casa_mov_izquierda_derecha_wireframe-0.5
                if event.key == pygame.K_d:
                    casa_mov_izquierda_derecha=casa_mov_izquierda_derecha+0.5
                    casa_mov_izquierda_derecha_wireframe=casa_mov_izquierda_derecha_wireframe+0.5
                #sheer
                if event.key == pygame.K_v:
                    Load = 4
                    
                #rotacion casa
                if event.key == pygame.K_r:
                    casa_rota_z =casa_rota_z+10

                if event.key == pygame.K_f:
                    casa_rota_z =casa_rota_z-10

                if event.key == pygame.K_o:
                    arbol_rota_z =arbol_rota_z+10

                if event.key == pygame.K_p:
                    arbol_rota_z =arbol_rota_z-10
                
                if event.key == pygame.K_m:
                    glScale(1.1,1.1,1.1)
                    scale_arbol=scale_arbol+1.1
                if event.key == pygame.K_n:
                    glScale(0.9,0.9,0.9)
                    #scale_arbol=scale_arbol-0.2
                if event.key ==pygame.K_i:
                    if Load ==0:
                        Load= 1
                    elif Load ==1:
                        Load = 2
                    elif Load ==2:
                        Load = 3
                    elif Load ==3:
                        Load = 4
                    elif Load ==4:
                        Load =5
                    elif Load ==5:
                        Load=6
                    elif Load ==6:
                        Load=0
                    
                if event.key ==pygame.K_c:
                    Load=0
                    house1=0

                if event.key == pygame.K_e:
                   Key_enable=1
                if event.key == pygame.K_c:
                   Key_enable=0
                if event.key == pygame.K_h:
                    Load =5
                if event.key == pygame.K_k:
                    Load =6
                   
                    
                        
                    
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
            glPushMatrix()
            glTranslatef(mov_izquierda_derecha,mov_arriba_abajo,0)
            glRotatef(arbol_rota_z,0,0,1)
            #glScale(1,scale_arbol,1)
            Tree()
            glPopMatrix()
            #Hay que separar movimiento de rotacion porque los controles se vuelven raros
            #Movimiento casa
            glPushMatrix()
            glRotatef(casa_rota_z,0,0,1)
            glTranslatef(casa_mov_izquierda_derecha,casa_mov_arriba_abajo,0)
            #sheer
            #glMultMatrixf(shear_m)
            Cube()
            Door()
            glPopMatrix()
            ground()
            Cube_texture()
            play_sound =0
            
          
           
          
            #Cone()
        if Load ==0 and Key_enable==1:
            #Cube()
            Cube_wireframe()
            #Door()
            #ground()
            ground_wireframe()
            Tree_wireframe()
            

          
            
        if Load==1:
            glPushMatrix()
            glTranslatef(mov_izquierda_derecha_wireframe,mov_arriba_abajo_wireframe,0)
            glRotatef(arbol_rota_z,0,0,1)
            #glScale(1,scale_arbol,1)
            Tree_wireframe()
            glPopMatrix()

            #Hay que separar movimiento de rotacion porque los controles se vuelven raros
            #Movimiento casa
            glPushMatrix()
            glRotatef(casa_rota_z,0,0,1)
            glTranslatef(casa_mov_izquierda_derecha_wireframe,casa_mov_arriba_abajo_wireframe,0)
            #sheer
            #glMultMatrixf(shear_m)
            Cube_wireframe()
            #Door()
            glPopMatrix()
            ground()
            Cube_texture()
          

        if Load ==2:
            Cube_texture()
          
        

        if Load ==4:
            glPushMatrix()
            glMultMatrixf(shear_m)
            Cube()
            glPopMatrix()

        if Load ==5:
            smurf1  = pygame.image.load("HCI1.png")
            bronze1 = pygame.image.tostring(smurf1, "RGBA", 1)

            width = smurf1.get_width()
            height = smurf1.get_height()

            glEnable(GL_TEXTURE_2D)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


            texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
            GL_UNSIGNED_BYTE, bronze1)
            glPushMatrix()
            glTranslatef(0,0,-90)
            glBegin(GL_QUADS)
            glTexCoord2f(0,1)
            glVertex3f(-100,100,100)
            glTexCoord2f(1,1)
            glVertex3f(100,100,100)
            glTexCoord2f(1,0)
            glVertex3f(100,-100,100)
            glTexCoord2f(0,0)
            glVertex3f(-100,-100,100)
            glEnd()
            glPopMatrix()

        if Load ==6:
            # glRotatef(25,2,1,0)
            glPushMatrix()
            glTranslatef(-1.33,0,3.5)
            glRotatef(90,0,1,0)
            Door()
            glPopMatrix()

            glPushMatrix()
            glTranslatef(0,0,50)
            rawSphere(10,20,0)
            glPopMatrix()

            glPushMatrix()
            glTranslatef(mov_izquierda_derecha,mov_arriba_abajo,0)
            glRotatef(arbol_rota_z,0,0,1)
            #glScale(1,scale_arbol,1)
            Tree()
            glPopMatrix()
            #Hay que separar movimiento de rotacion porque los controles se vuelven raros
            #Movimiento casa
            glPushMatrix()
            glRotatef(casa_rota_z,0,0,1)
            glTranslatef(casa_mov_izquierda_derecha,casa_mov_arriba_abajo,0)
            #sheer
            #glMultMatrixf(shear_m)
            Cube()
            glPopMatrix()
            
            if play_sound ==0:
                winsound.PlaySound('door_2.wav',winsound.SND_FILENAME)
                play_sound =1
                
                
        pygame.display.flip()
        pygame.time.wait(10)

main()
    
