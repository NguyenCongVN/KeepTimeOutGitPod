import os
import pyautogui
import time

pyautogui.FAILSAFE = False

def click_image_center(path : str) -> bool:
    try:
        x, y = pyautogui.locateCenterOnScreen(path)
        pyautogui.click(x, y)
        return True
    except:
        return False
    

def click_center_of_screen():
    x, y = pyautogui.size()
    pyautogui.click(x/2, y/2)

if __name__ == '__main__':
    
    # im1 = pyautogui.screenshot()
    # im2 = pyautogui.screenshot('openworkspace.png')
    
    # check if user-data-dir name google_data exists
    if not os.path.exists('google_data'):
        os.mkdir('google_data')
    # run chrome in full screen with user-data-dir in a new thread that not block the main thread
    os.system('chromium --start-maximize --user-data-dir=google_data &')
    
    # find button restore if exists
    # set a timeout of 60 seconds
    start_time = time.time()
    while click_image_center('restore.png') == False:
        time.sleep(1)
        if time.time() - start_time > 60:
            break
    
    
    while True:
        # find Open workspace button
        if not click_image_center('openworkspace.png'):
            click_center_of_screen()
            time.sleep(3)
        
        # switch tab
        pyautogui.hotkey('ctrl', 'tab')
        
        # ask user need to a pause of program or not. timeout if user not press any key in 5 seconds
        
        if pyautogui.confirm(text='Do you need to pause the program?', buttons=['Yes', 'No'], timeout=5) == 'Yes':
            # if yes, ask user how long to pause
            while True:
                try:
                    pause_time = int(pyautogui.prompt(text='How long to pause (in seconds)?', default='60'))
                    break
                except:
                    pass
            # pause the program
            time.sleep(pause_time)
            