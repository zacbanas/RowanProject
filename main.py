import pygame as pg
import variables as v
import characters as char
import images as i

#setting window size
display_width = 900
display_height = 600

pg.init()

gameDisplay = pg.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


class Gamerun(object):

    def __init__(self, diswid, dishit):
        self.display_width = diswid
        self.display_height = dishit

    def main(self):
        gameDone = False


        while not gameDone:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        #v.heroy_change -= 3
                        v.heromapyc -= 3
                        v.camyc += 5
                        v.heroFace = 1
                        v.step += 1
                        v.heroState = 'moving'
                    if event.key == pg.K_DOWN:
                        #v.heroy_change += 3
                        v.heromapyc += 3
                        v.camyc -= 5
                        v.heroFace = 3
                        v.step += 1
                        v.heroState = 'moving'
                    if event.key == pg.K_LEFT:
                        #v.herox_change -= 3
                        v.heromapxc -= 3
                        v.camxc += 5
                        v.heroFace = 4
                        v.step += 1
                        v.heroState = 'moving'
                    if event.key == pg.K_RIGHT:
                        #v.herox_change += 3
                        v.heromapxc += 3
                        v.camxc -= 5
                        v.heroFace = 2
                        v.step += 1
                        v.heroState = 'moving'
                    if event.key == pg.K_p:
                        if v.pause == 0:
                            v.pause = v.pause + 1
                        if v.pause == 1:
                            v.pause = v.pause - 1
                if event.type == pg.KEYUP:
                    v.heroy_change = 0
                    v.herox_change = 0
                    v.heromapxc = 0
                    v.heromapyc = 0
                    v.camxc = 0
                    v.camyc = 0
                    v.heroState = 'still'

            v.heromapx += v.heromapxc
            v.heromapy += v.heromapyc
            v.camerax += v.camxc
            v.cameray += v.camyc


            if v.pause == 1:
                pause = char.PauseMenu()

                gameDisplay.fill(red)
                pause.draw()

                pg.display.update()
                v.clock.tick(30)


            if v.pause == 0:
                gameDisplay.fill(black)


                camera = char.Camera()

                hero = char.Hero()
                # blue1 = char.BlueRect(480, 325)
                # blue1.draw()

                pg.draw.rect(i.mappy, blue, (450, 300, 10, 10))



                camera.draw()
                pg.draw.rect(i.mappy, blue, (459, 300, 10, 10))
                hero.draw()



                pg.display.update()
                v.clock.tick(30)

if __name__ == '__main__':
    Gamerun(display_width, display_height).main()

