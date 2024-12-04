from contextlib import nullcontext

import pygame

from Background import BackgroundHandler
from Tree import TreeObstacle
import random
from Meteor import MeteorObstacle
from mainmenu import Menu
from Rocket import Rocket
from PickupHandler import PickUpHandler
from Coin import Coin
from upside_down import UpsideDown
from time import sleep

pygame.init()


def game():

    points = 0

    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    scoreboard = pygame.image.load("gameart/gameart/png&gif/ui/score_display.png")
    scoreboard = pygame.transform.scale(scoreboard, (120, 50))

    player_png = pygame.image.load("gameart/gameart/png&gif/gameplay/player.png")
    player_png = pygame.transform.scale(player_png, (80, 80))


    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
    menu = Menu(screen)

    radious = 40
    player_rect = pygame.Rect((player_pos.x - radious/2*1.5, player_pos.y - radious/2*1.5), (radious*1.5, radious*1.5))

    velocity = 0
    g = -1
    a = 2
    max_velocity = 10
    min_velocity = -15
    obstacles_in_game = []
    pickups_in_game = []

    obstacle_speed = 3
    item_speed = 3
    obstaclerate = 60 * 5
    minrate = 1
    maxrate = 3
    obcount = 299

    coincount = 0
    coinrate = 60*5


    skibidi = ["coin"]
    pickup_handler = PickUpHandler(skibidi)

    background = BackgroundHandler(1280, 720)

    bg_sur = pygame.Surface((1280, 720))

    def obstacle_handler():
        obstacle_list = ["tree", "meteor", "rocket", "upside_down"] # add other obstacles later
        current_obstacle = random.randint(0, len(obstacle_list) -1)

        if obstacle_list[current_obstacle] == "tree":
            xcord = screen.get_width() + 40
            tree = TreeObstacle(xcord, 360)
            return tree
        if obstacle_list[current_obstacle] == "meteor":
            xcord = screen.get_width() + 40
            meteor = MeteorObstacle(xcord, 0)
            return meteor
        if obstacle_list[current_obstacle] == "rocket":
            xcord = screen.get_width() + 40
            y = random.randint(20, 420)
            rocket = Rocket(xcord, y)
            return rocket
        if obstacle_list[current_obstacle] == "upside_down":
            xcord = screen.get_width() + 40
            upsidedown = UpsideDown(xcord, 0)
            return upsidedown


    def move_obstacles(obstacles):
        for obst in obstacles:
            obst.move(-obstacle_speed)
            if obst.x <= -100:
                obstacles.remove(obst)
    def move_pickups(pickups):
        if len(pickups) != 0:
            for item in pickups:
                item.move(-item_speed)
                if item.x <= -50:
                    pickups.remove(item)


    def draw(obstacles, playerpos, pickups, text):
        bg_sur.blit(background.img, (0, 0))

        for obstacle in obstacles:
            if obstacle.name == "tree":
                bg_sur.blit(obstacle.img, (obstacle.rect.x-45, obstacle.rect.y))

            if obstacle.name == "meteor":
                bg_sur.blit(obstacle.img, (obstacle.rect.x-10, obstacle.rect.y-10))
            if obstacle.name == "rocket":
                obstacle.animate()
                bg_sur.blit(obstacle.img, (obstacle.rect.x, obstacle.rect.y-15))
            if obstacle.name == "upside_down":
                bg_sur.blit(obstacle.img, (obstacle.rect.x-45, obstacle.rect.y))
        for pick in pickups:
            if pick.name == "coin":
                bg_sur.blit(pick.img, (pick.x-20, pick.y-20))
                pick.animate()


        screen.blit(bg_sur, (0, 0))
        #player:
        screen.blit(player_png, (player_rect.x-10, player_rect.y-10))
        #score:
        screen.blit(scoreboard, (0, 0))
        screen.blit(text, (75, 4))


    def collide(player_rect, ingame):
        for obstacle in ingame:
            if pygame.Rect.colliderect(obstacle.rect, player_rect):
                return False
        return True

    def pickuppickup(pickups):
        for pickup in pickups:
            if pygame.Rect.colliderect(pickup.rect, player_rect):
                if pickup.name == "coin":
                    pickups.remove(pickup)
                    return True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            velocity += a


        velocity += g

        if velocity > max_velocity:
            velocity = max_velocity
        if velocity < min_velocity:
            velocity = min_velocity
        if player_pos.y <= 32:
            player_pos.y = 32
            player_rect.y = 32 - radious/2*1.5
            velocity = -0.1
        if player_pos.y >= screen.get_height() -32:
            velocity = 0.1
            player_pos.y = screen.get_height() -32
            player_rect.y = screen.get_height() -32 - radious/2*1.5

        #obstacle handling:
        obcount += 1

        obstacle_speed += 1/1800
        item_speed += 1/1800

        if not minrate <= 0.4:
            minrate -= 1 / 3600
        if not maxrate <= 0.4:
            maxrate -= 1/3600

        if obcount >= obstaclerate:
            obstaclerate = 60 * random.uniform(minrate, maxrate)
            obcount = 0
            obstacle = obstacle_handler()
            obstacles_in_game.append(obstacle)
        move_obstacles(obstacles_in_game)

        #pickup handling
        if coinrate <= coincount:
            coincount = 0
            coinrate = 60 * random.uniform(2, 8)
            pickup = pickup_handler.spawn()
            pickups_in_game.append(pickup)
        else:
            coincount += 1
        if len(pickups_in_game) != 0:
            move_pickups(pickups_in_game)

        running = collide(player_rect, obstacles_in_game)

        render = my_font.render(str(points), False, (0, 0, 0))
        text_surface = render

        hasscored = pickuppickup(pickups_in_game)
        if hasscored:
            hasscored = False
            points += 1


        #drawing:
        draw(obstacles_in_game, player_pos, pickups_in_game, text_surface)

        player_pos.y -= velocity
        player_rect = pygame.Rect.move(player_rect, 0, -velocity)


        if not running:
            player_png = pygame.transform.rotate(player_png, 180)
            i = 0
            while i < 720 - player_pos.y:
                i += 1
                player_pos.y += 1
                player_rect.y += 1
                print(i)
                draw(obstacles_in_game, player_pos, pickups_in_game, text_surface)


        pygame.display.flip()
        clock.tick(60)



main_screen = pygame.display.set_mode((1280, 720))

in_win = True
while in_win:
    main_screen.fill("red")
    pygame.display.flip()

    nokeys = True
    while nokeys:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nokeys = False
                pygame.quit
                in_win = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    nokeys = False
                    pygame.quit
                    in_win = False
                nokeys = False
    if in_win: game()




