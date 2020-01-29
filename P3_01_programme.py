#!/usr/bin/env python3
# coding: utf-8

import pygame
from random import randint


class loading_map:
    def __init__(self, t_map):
        self.map_height = t_map
        try:
            read_map = open("ressource/MapMaze.txt", "r")
            self.mapstr = read_map.readlines()
            read_map.close()

        except IOError:
            print("error load map")


    def ep_map(self):
        self.map = [[0 for i in range(self.map_height)] for j in range(self.map_height)]
        ct2 = 0
        for line in self.mapstr:
            ct1 = 0
            line.rstrip('\n')
            for sp in line:
                self.map[ct2][ct1] = sp
                ct1 = ct1 + 1
                if ct1 == self.map_height:
                    break
            ct2 = ct2 + 1
            if ct2 == self.map_height:
                break
        return self.map

class main_maze:
    def __init__(self, t_map):
        self.map_height = t_map
        self.gamecontinue = True
        self.gamestop = False
        self.obj_recup = 0

    def smap(self,map,nbr_obj):
        self.nbr_obj = nbr_obj
        self.map = map
        self.num_floor = 0
        for i in range (self.map_height):
            self.num_floor = self.num_floor + self.map[i].count("s")

        self.pose_obj_x = list()
        self.pose_obj_y = list()
        self.list_random = list()
        nbr_random = 0
        while nbr_random != self.nbr_obj:
            new_number = randint(1,self.num_floor)
            if self.list_random.count(new_number) == 0:
                self.list_random.append(new_number)
                nbr_random = nbr_random + 1

        

    def stopgame(self):
        self.gamecontinue = False

    def print_map(self):
        ct_obj = 0
        num_obj = 1
        for x in range(1, map_height +1):
            for y in range(1, map_height +1):
                px = x * 20
                py = y * 20
                px =  px - 20
                py =  py - 20
                if self.map[y-1][x-1] == "m":
                    ecran.blit(wall_picture, (py, px))
                if self.map[y-1][x-1] == "s":
                    ct_obj = ct_obj + 1
                    if self.list_random.count(ct_obj) == 0:
                        ecran.blit(floor_picture, (py, px))
                    else:
                        if num_obj == 1:
                            ecran.blit(sword_picture, (py, px))
                            num_obj = num_obj + 1
                        elif num_obj == 2:
                            ecran.blit(shield_picture, (py, px))
                            num_obj = num_obj + 1
                        elif num_obj == 3:
                            ecran.blit(armor_picture, (py, px))
                            num_obj = num_obj + 1
                        else:
                            ecran.blit(objet_picture, (py, px))
                        self.pose_obj_x.append(x-1)
                        self.pose_obj_y.append(y-1)
                if self.map[y-1][x-1] == "p":
                    ecran.blit(player_picture, (py, px))
                    self.player_pose_y = y-1
                    self.player_pose_x = x-1
                if self.map[y-1][x-1] == "a":
                    ecran.blit(guard_picture, (py, px))
                    self.end_pose_y = y-1
                    self.end_pose_x = x-1
        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
        font = pygame.font.SysFont(None, 20)
        text = font.render(txt_nbr_obj,1,(255,255,255))
        ecran.blit(text, (0, 300))
    
    def player_move_right(self):
        if self.gamestop == False:
            if self.map[self.player_pose_y +1][self.player_pose_x] == "a":
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            if self.map[self.player_pose_y +1][self.player_pose_x] == "s":
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x and self.pose_obj_y[ct] == self.player_pose_y +1:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        ecran.blit(text, (0, 300))
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y +1][self.player_pose_x] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                ecran.blit(floor_picture, (py, px))
                ecran.blit(player_picture, (py+20, px))
                self.player_pose_y = self.player_pose_y + 1
        else:
            self.stopgame()

    def player_move_left(self):
        if self.gamestop == False:
            if self.map[self.player_pose_y -1][self.player_pose_x] == "a":
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            if self.map[self.player_pose_y -1][self.player_pose_x] == "s":
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x and self.pose_obj_y[ct] == self.player_pose_y -1:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        ecran.blit(text, (0, 300))
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y -1][self.player_pose_x] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                ecran.blit(floor_picture, (py, px))
                ecran.blit(player_picture, (py-20, px))
                self.player_pose_y = self.player_pose_y - 1
        else:
            self.stopgame()

    def player_move_up(self):
        if self.gamestop == False:
            if self.map[self.player_pose_y][self.player_pose_x -1] == "a":
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            if self.map[self.player_pose_y][self.player_pose_x -1] == "s":
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x -1 and self.pose_obj_y[ct] == self.player_pose_y:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        ecran.blit(text, (0, 300))
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y][self.player_pose_x -1] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                ecran.blit(floor_picture, (py, px))
                ecran.blit(player_picture, (py, px-20))
                self.player_pose_x = self.player_pose_x - 1
        else:
            self.stopgame()

    def player_move_down(self):
        if self.gamestop == False:
            if self.map[self.player_pose_y][self.player_pose_x +1] == "a":
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            if self.map[self.player_pose_y][self.player_pose_x +1] == "s":
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x +1 and self.pose_obj_y[ct] == self.player_pose_y:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        ecran.blit(text, (0, 300))
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y][self.player_pose_x +1] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                ecran.blit(floor_picture, (py, px))
                ecran.blit(player_picture, (py, px+20))
                self.player_pose_x = self.player_pose_x + 1
        else:
            self.stopgame()
    
    def player_win(self):
        ecran.blit(you_win_picture, (0, 0))
        self.gamestop = True
    
    def player_lose(self):
        ecran.blit(you_lose_picture, (0, 0))
        self.gamestop = True


map_height = 15
nbr_obj = 3

jeux = loading_map(map_height)

map = jeux.ep_map()

jeux = main_maze(map_height)

jeux.smap(map,nbr_obj)

pygame.init()

ecran = pygame.display.set_mode((map_height *20, map_height *20+20))
you_win_picture = pygame.image.load("ressource/you_win.png").convert_alpha()
you_lose_picture = pygame.image.load("ressource/you_lose.png").convert_alpha()
floor_picture = pygame.image.load("ressource/floor.png").convert_alpha()
wall_picture = pygame.image.load("ressource/wall.png").convert_alpha()
player_picture = pygame.image.load("ressource/player.png").convert_alpha()
guard_picture = pygame.image.load("ressource/guard.png").convert_alpha()
objet_picture = pygame.image.load("ressource/objet.png").convert_alpha()
sword_picture = pygame.image.load("ressource/sword.png").convert_alpha()
shield_picture = pygame.image.load("ressource/shield.png").convert_alpha()
armor_picture = pygame.image.load("ressource/armor.png").convert_alpha()
jeux.print_map()


while jeux.gamecontinue:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                jeux.stopgame()
            if event.key == pygame.K_LEFT:
                jeux.player_move_left()
            if event.key == pygame.K_RIGHT:
                jeux.player_move_right()
            if event.key == pygame.K_UP:
                jeux.player_move_up()
            if event.key == pygame.K_DOWN:
                jeux.player_move_down()
    pygame.display.flip()

pygame.quit()
