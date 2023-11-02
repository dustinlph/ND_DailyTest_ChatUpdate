import os
import datetime
import pyautogui
from apscheduler.schedulers.background import BlockingScheduler

more_info_img_path: str = os.path.join(os.getcwd(), 'more_info.png')


def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')


def click_more_info():
    print(more_info_img_path)
    coord = pyautogui.locateCenterOnScreen(
        more_info_img_path, confidence=0.9, grayscale=True)
    if coord:
        pyautogui.click(coord)
        print(f'{get_current_time()} | Refresh page!!!')
    else:
        print(f'{get_current_time()} | Element not found.')


sched = BlockingScheduler()
sched.add_job(click_more_info, 'interval', seconds=10)
sched.get_jobs()
sched.start()
