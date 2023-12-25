import pyautogui as pg
from pyautogui import ImageNotFoundException
from typing import Tuple
import time

def find_center(fp: str) -> Tuple[int, int]:
    """
    Attempts to find play button, returns center of button if found.
    (loading time est 1.5s)
    """
    try:
        image = pg.locateOnScreen(fp)
        if image:
            return image.left + image.width / 2, image.top + image.height / 2
    except ImageNotFoundException:
        return None

def do_turn(direction: str):
    """
    direction: 'left' or 'right'
    wait: time to wait before making turn
    """
    print('Releasing up arrow key')
    pg.keyUp('up')
    print('Holding {} arrow key'.format(direction))
    pg.keyDown(direction)
    time.sleep(0.2)
    print('Releasing {} arrow key'.format(direction))
    pg.keyUp(direction)

def play_round():
    print('Holding up arrow key')
    pg.keyDown('up')

    while True:
        pg.keyDown('up')
        if find_center('images/arrow_left.png'):
            do_turn('left')
            break
        elif find_center('images/arrow_right.png'):
            do_turn('right')
            break

        elif (dead := find_center('images/death.png')):
            print('YO I DIED HOW? FIX ME')
            pg.press('space')
            time.sleep(0.2)
            print('Respawned. hopefully')



def main():
    while True:
        print('Finding game enterance...')
        time.sleep(1)
        pg.moveTo(100, 100)

        if (mine := find_center('images/mine.png')):
            pg.click(mine)
            print('Going into mine.')
            time.sleep(3)

        if (cart := find_center('images/cart_surfer.png')):
            pg.click(cart)
            print('Clicked cart surfer')
            time.sleep(2)
            break

        if (done := find_center('images/done.png')):
            print('Missed done button, clicking now.')
            pg.click(done)
            time.sleep(0.5)

    while not (yes := find_center('images/yes.png')):
        print('Cant find yes button. sleeping')
        time.sleep(1)
    pg.click(yes)
    print('Clicked yes button')

    while not (button := find_center('images/play_button.png')):
        print('Play button not found, retrying...')
        time.sleep(1)
    
    print('Play button found, clicking...')
    pg.doubleClick(button)

    print('Sleeping for 0.3s...')
    time.sleep(0.3)

    lives = 2
    while True:
        pg.keyDown('up')
        if (death := find_center('images/death.png')):
            if lives == 0:
                while not (x_btn := find_center('images/quit.png')):
                    print('Cant find quit button. sleeping')
                    time.sleep(1)
                pg.click(x_btn)
                print('Clicked quit button')
                break
            else:
                lives -= 1
                print('Died, respawning')
                pg.press('space')
                time.sleep(0.1)
    
    while not (done := find_center('images/done.png')):
        print('Cant find done button. sleeping')
        time.sleep(1)
    pg.click(done)
    print('Clicked done button')
    time.sleep(0.5)

    '''
    while True:
        if (done := pg.locateOnScreen('images/done.png')):
            print('Game complete!')
            pg.click(done)
            break

        if (dead := pg.locateOnScreen('images/death.png')):
            print('YO I DIED HOW? FIX ME')
            pg.press('space')
            time.sleep(0.5)
            print('Respawned. hopefully')
        
        play_round()

    print('Game done!')
    time.sleep(1)
    '''

if __name__ == '__main__':
    while True:
        main()