import pygame
import numpy as np
from math import *
import igl


(points, _, _, f2, _, _) = igl.read_obj("G:/shared/blenderScripts/mesh/mh_testMeshObjFormat.obj")

print(f2[0][0])
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 1200, 1200
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 30

circle_pos = [WIDTH/2, HEIGHT/2]  # x, y

angle = 0.2
keys = [False,False,False,False,False,False,False]
# points = []

# # all the cube vertices
# points.append(np.matrix([-1, -1, 1]))
# points.append(np.matrix([1, -1, 1]))
# points.append(np.matrix([1,  1, 1]))
# points.append(np.matrix([-1, 1, 1]))
# points.append(np.matrix([-1, -1, -1]))
# points.append(np.matrix([1, -1, -1]))
# points.append(np.matrix([1, 1, -1]))
# points.append(np.matrix([-1, 1, -1]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j, points):
    pygame.draw.line(
        screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

def connect_points_new(startX,startY,endX,endY):
    pygame.draw.line(
        screen, BLACK, (startX,startY), (endX,endY))

clock = pygame.time.Clock()
while True:

    clock.tick(60)

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
    # update stuff

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])


    screen.fill(BLACK)
    # drawining stuff

    i = 0
    for point in points:
        if(keys[1]):
            point[0]-=5
        if(keys[3]):
            point[0]+=5
        if(keys[0]):
            point[1]-=5
        if(keys[2]):
            point[1]+=5
        if(keys[4]):
            rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
            point[0] = rotated2d[0]
            point[1] = rotated2d[1]
            point[2] = rotated2d[2]
        if(keys[5]):
            rotated2d = np.dot(rotation_x, point.reshape((3, 1)))
            point[0] = rotated2d[0]
            point[1] = rotated2d[1]
            point[2] = rotated2d[2]         
        if(keys[6]):
            rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
            point[0] = rotated2d[0]
            point[1] = rotated2d[1]
            point[2] = rotated2d[2]     
        #rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        #rotated2d = np.dot(rotation_y, rotated2d)

        #projected2d = np.dot(projection_matrix, rotated2d)
        projected2d = np.dot(projection_matrix, point.reshape((3, 1)))
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]


        projected_points[i] = [x, y]
        #pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1
    for p in f2:
        #connect_points_new(projected_points[p[0]][0], projected_points[p[0]][1], projected_points[p[1]][0], projected_points[p[1]][1])
        #connect_points_new(projected_points[p[1]][0], projected_points[p[1]][1], projected_points[p[2]][0], projected_points[p[2]][1])
        #connect_points_new(projected_points[p[2]][0], projected_points[p[2]][1], projected_points[p[3]][0], projected_points[p[3]][1])
        #connect_points_new(projected_points[p[3]][0], projected_points[p[3]][1], projected_points[p[0]][0], projected_points[p[0]][1])

        pygame.draw.polygon(screen, WHITE, [(projected_points[p[0]][0],projected_points[p[0]][1]),(projected_points[p[1]][0],projected_points[p[1]][1]),(projected_points[p[2]][0], projected_points[p[2]][1]),(projected_points[p[3]][0],projected_points[p[3]][1])])
    # for p in range(4):
    #     connect_points(p, (p+1) % 4, projected_points)
    #     connect_points(p+4, ((p+1) % 4) + 4, projected_points)
    #     connect_points(p, (p+4), projected_points)

    pygame.display.update()
    