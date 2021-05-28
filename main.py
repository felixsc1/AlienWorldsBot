#%% imports
import pyautogui as gui
import time


# %%  Tutorial stuff

# gui.size()
# gui.moveTo(0,1,duration=1)

# try:
#     while True:
#         x_cord,y_cord = gui.position()
#         print(f'x={x_cord}, y={y_cord}')
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Exit")

# %% Mining Functions


def find_and_click(image):
    while True:
        try:
            _x,_y = gui.locateCenterOnScreen(image, grayscale=True)
            break
        except:
            time.sleep(1)
            print('waiting for button...')
            continue
    gui.click(_x,_y)


# find_and_click('minebutton.PNG')
# print('button is here!')

#%% Main Loop

#For a window dragged to left half of screen

def mining_cycle():
    # click START mining
    print('--- Start mining!')
    find_and_click('minebutton.PNG')
    time.sleep(5)

    #CLAIM
    print('--- Claiming')
    find_and_click('claimbutton.PNG')
    time.sleep(5)

    #APPROVE
    print('--- Approving')
    find_and_click('approve.PNG')
    time.sleep(5)

    #MINING HUB
    print('--- Returning and waiting')
    find_and_click('mininghubbutton.PNG')


charge_time = 15*60+30
try:
    i = 1
    while True:
        mining_cycle()
        print(f"Mining run #{i} completed, waiting {charge_time} seconds")
        time.sleep(charge_time)
except KeyboardInterrupt:
    print("Exit")

        