import pyautogui
import time
import psutil
from tkinter import simpledialog, ttk 
from tkinter import *

#This is a git test

exename ='msedge.exe'
#print(pyautogui.position())

'''Recieved error "Too early to create dialog window: no default root window" so the below creates a Tk window and hides it '''
root = Tk()
root.withdraw()

'''user input box asking for number of loading reports'''
USER_INP = simpledialog.askstring(title="Loading Reports", 
                                  prompt="Hi production, how many loading reports today?:")

user_inp_to_int = int(USER_INP) 

number_of_loops = user_inp_to_int + 1

'''Click first job and start printing loop'''
pyautogui.click(240, 652)     
pyautogui.click(139, 549)
time.sleep(5) #waits for docs to open

#commit test

def if_process_is_running_by_exename(exename):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == exename:
            return True
    return False

'''loops printing process'''
for i in range(0, number_of_loops):

    time.sleep(5)
    '''Print Document Viewer'''
    pyautogui.click(1968, 33)
    pyautogui.click(1968, 33)
    time.sleep(0.75)

    running = if_process_is_running_by_exename(exename)

    '''Increase copies by 1'''
    pyautogui.click(2332, 282)

    time.sleep(0.2)

    # '''Print Button On Popop '''
    # #pyautogui.click(2212, 414)

    # time.sleep(0.2)

    '''Cancel Button on Popup for testing'''
    pyautogui.click(2289, 409)

    time.sleep(0.2)

    '''Close Document Viewer'''
    pyautogui.click(3829, 7)

    time.sleep(0.5)

    '''Print document viewer for loading report'''
    pyautogui.click(1968, 33)
    pyautogui.click(1968, 33)

    time.sleep(0.5)

    # '''Print Button On Popup'''
    #  pyautogui.click(2212, 414)

    '''Cancel Button on Popup for testing'''
    pyautogui.click(2289, 409)

    time.sleep(0.25)

    '''Close Document Viewer '''
    pyautogui.click(3829, 7)

    if if_process_is_running_by_exename == True:
        pyautogui.click(72, 1058)
        pyautogui.click(72, 1058)
    else:
        pass

    while running == True:
        running = if_process_is_running_by_exename(exename)
        pyautogui.click(822, 367)
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('p')

        '''cancel button on edge for testing'''
        time.sleep(1)
        pyautogui.click(284, 923)

        time.sleep(0.2)
        pyautogui.press('w')
        pyautogui.keyUp('ctrl')
    else:
        pass

    pyautogui.click(685, 603)
    pyautogui.press('down')
    pyautogui.click(139, 549)


