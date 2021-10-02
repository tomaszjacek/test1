import pygame
import numpy as np
from math import *
import igl

class vec3d:  
    def __init__(self,x=None,y=None,z=None):
        self.x=x
        self.y=y
        self.z=z


class triangle:
    def __init__(self,a=None,b=None,c=None):
        self.p=[]
        self.p.append(a)
        self.p.append(b)
        self.p.append(c)
       
class square:
    def __init__(self,a=None,b=None,c=None,d=None):
        self.p = []
        self.p.append(a)
        self.p.append(b)
        self.p.append(c)
        self.p.append(d)

class mesh:

    def fromObjFile(self,fileName):
        self.vertices = []
        self.faces = []
        (v1, _, _, f1, _, _) = igl.read_obj(fileName)
        for v in v1:
            self.vertices.append(vec3d(v[0],v[1],v[2]))
        for f in f1:
            self.faces.append(square(f[0],f[1],f[2],f[3]))

class mat4x4:
    m = np.zeros((3, 3))


class tmpClass:
    def addOneToVec(self,a):
        a.x+=1
        a.y+=1
        a.z+=1


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 600
keys = [False,False,False,False,False,False,False]

class MainWindow:
    def __init__(self):
        pygame.init()
        self.scale=30
        self.circle_pos = [WIDTH/2, HEIGHT/2] 
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.purple = (150, 0, 220)
        self.SCREEN.fill(BLACK)
        pygame.display.set_caption("3D projection in pygame!")

        self.clock = pygame.time.Clock()
        self.time_counter = 0
        self.angle = 0.2
        self.meshCube = mesh()
        self.meshCube.fromObjFile("G:/shared/blenderScripts/mesh/mh_testMeshObjFormat.obj")
        #for f in self.meshCube.faces:
            #print(f.p)
            #print("----------------------")
        self.matProj = mat4x4()
        self.matRotZ = mat4x4()
        self.matRotX = mat4x4()
        #self.fTheta = float(0.0)
        #self.fNear = float(0.1)
        #self.fFar = float(10.0)
        #self.fFov = float(90.0)
        #self.fAspectRatio = float(HEIGHT / WIDTH)
        #self.fFovRad = float(1.0) / tan(self.fFov * float(0.5) / float(180.0) * float(3.14159))

        #self.matProj.m[0][0] = self.fAspectRatio * self.fFovRad
        #self.matProj.m[1][1] = self.fFovRad
        #self.matProj.m[2][2] = self.fFar / (self.fFar - self.fNear)
        #self.matProj.m[3][2] = (-self.fFar * self.fNear) / (self.fFar - self.fNear)
        #self.matProj.m[2][3] = float(1.0)
        #self.matProj.m[3][3] = float(0.0)
        self.matProj.m[0][0] = 1
        self.matProj.m[1][1] = 1


        #self.rotation_z = np.matrix([
        #    [cos(self.angle), -sin(self.angle), 0],
        #    [sin(self.angle), cos(self.angle), 0],
        #    [0, 0, 1],
        #])
        self.matRotZ.m[0][0] = cos(self.angle)
        self.matRotZ.m[0][1] = sin(self.angle)
        self.matRotZ.m[1][0] = -sin(self.angle)
        self.matRotZ.m[1][1] = cos(self.angle)
        self.matRotZ.m[2][2] = 1
		#self.matRotZ.m[3][3] = 1

        #self.rotation_y = np.matrix([
        #    [cos(self.angle), 0, sin(self.angle)],
        #    [0, 1, 0],
        #    [-sin(self.angle), 0, cos(self.angle)],
        #])

        #self.rotation_x = np.matrix([
        #    [1, 0, 0],
        #    [0, cos(self.angle), -sin(self.angle)],
        #    [0, sin(self.angle), cos(self.angle)],
        #])
        self.matRotX.m[0][0] = 1
        self.matRotX.m[1][1] = cos(self.angle * float(0.5))
        self.matRotX.m[1][2] = sin(self.angle * float(0.5))
        self.matRotX.m[2][1] = -sin(self.angle * float(0.5))
        self.matRotX.m[2][2] = cos(self.angle * float(0.5))
		#self.matRotX.m[3][3] = 1

    def MultiplyMatrixVector(self, i, o, m):
        o.x = i.x * m.m[0][0] + i.y * m.m[1][0] + i.z * m.m[2][0] #+ m.m[3][0]
        o.y = i.x * m.m[0][1] + i.y * m.m[1][1] + i.z * m.m[2][1] #+ m.m[3][1]
        o.z = i.x * m.m[0][2] + i.y * m.m[1][2] + i.z * m.m[2][2] #+ m.m[3][2]
        #w = i.x * m.m[0][3] + i.y * m.m[1][3] + i.z * m.m[2][3] + m.m[3][3]

        #if (w != 0.000):
        #    o.x /= w; o.y /= w; o.z /= w
	

    def main_game_loop(self):
        while True:
            self.time_counter+=1
            #self.time_counter += self.clock.tick()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        keys[0] = True
                    if event.key == pygame.K_a:
                        keys[1] = True
                    if event.key == pygame.K_s:
                        keys[2] = True
                    if event.key == pygame.K_d:
                        keys[3] = True   
                    if event.key == pygame.K_z:
                        keys[4] = True
                    if event.key == pygame.K_x:
                        keys[5] = True
                    if event.key == pygame.K_c:
                        keys[6] = True  
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        keys[0] = False
                    if event.key == pygame.K_a:
                        keys[1] = False
                    if event.key == pygame.K_s:
                        keys[2] = False
                    if event.key == pygame.K_d:
                        keys[3] = False
                    if event.key == pygame.K_z:
                        keys[4] = False
                    if event.key == pygame.K_x:
                        keys[5] = False
                    if event.key == pygame.K_c:
                        keys[6] = False

            #if self.time_counter > 15:
                
            self.SCREEN.fill(BLACK)
            for point in self.meshCube.vertices:
                    #print(point.x,point.y)
                    if(keys[1]):
                        point.x-=5
                    if(keys[3]):
                        point.x+=5
                    if(keys[0]):
                        point.y-=5
                    if(keys[2]):
                        point.y+=5
                    if(keys[4]):
                        rotated2d = vec3d()
                        self.MultiplyMatrixVector(point,rotated2d,self.matRotZ)                    
                        point = rotated2d
                    if(keys[5]):
                        rotated2d = vec3d()
                        self.MultiplyMatrixVector(point,rotated2d,self.matRotX)
                        point = rotated2d
                    if(keys[6]):
                        rotated2d = vec3d()
                        #self.MultiplyMatrixVector(point,rotated2d,self.rotation_y)
                        #point = rotated2d
            #n=0
            for f in self.meshCube.faces:
                v1 = vec3d()
                self.MultiplyMatrixVector(self.meshCube.vertices[f.p[0]],v1,self.matProj)
                #v1.x+=1
                #v1.y+=1
                #v1.x*=float(0.5)*float(WIDTH)
                #v1.y*=float(0.5)*float(HEIGHT)
                v1.x = int(v1.x*self.scale)+self.circle_pos[0]
                v1.y = int(v1.y*self.scale)+self.circle_pos[1]
                v2 = vec3d()
                self.MultiplyMatrixVector(self.meshCube.vertices[f.p[1]],v2,self.matProj)
                #v2.x+=1
                #v2.y+=1
                #v2.x*=float(0.5)*float(WIDTH)
                #v2.y*=float(0.5)*float(HEIGHT)
                v2.x = int(v2.x*self.scale)+self.circle_pos[0]
                v2.y = int(v2.y*self.scale)+self.circle_pos[1]
                v3 = vec3d()
                self.MultiplyMatrixVector(self.meshCube.vertices[f.p[2]],v3,self.matProj)
                #v3.x+=1
                #v3.y+=1
                #v3.x*=float(0.5)*float(WIDTH)
                #v3.y*=float(0.5)*float(HEIGHT)
                v3.x = int(v3.x*self.scale)+self.circle_pos[0]
                v3.y = int(v3.y*self.scale)+self.circle_pos[1]
                v4 = vec3d()
                self.MultiplyMatrixVector(self.meshCube.vertices[f.p[3]],v4,self.matProj)
                #v4.x+=1
                #v4.y+=1
                #v4.x*=float(0.5)*float(WIDTH)
                #v4.y*=float(0.5)*float(HEIGHT)
                v4.x = int(v4.x*self.scale)+self.circle_pos[0]
                v4.y = int(v4.y*self.scale)+self.circle_pos[1]
                #print(v4.x,v4.y,self.time_counter)
                #print(f.p[0],f.p[1],f.p[2],f.p[3])
                #print(len(self.meshCube.faces))
                pygame.draw.polygon(self.SCREEN, WHITE, [(v1.x,v1.y),(v2.x,v2.y),(v3.x,v3.y),(v4.x,v4.y)])
                #n+=1
                #self.time_counter = 0
            pygame.display.update()



game = MainWindow()
game.main_game_loop()












#t = mesh()
#t.fromObjFile("G:/shared/blenderScripts/mesh/mh_testMeshObjFormat.obj")
#print(t.vertices[0].x,t.vertices[0].y,t.vertices[0].z)

#adder = tmpClass()
#adder.addOneToVec(t.vertices[0])
#print(t.vertices[0].x,t.vertices[0].y,t.vertices[0].z)

#m =mat4x4()
#print(m.m)

