import os
import datetime
import pyautogui
from apscheduler.schedulers.background import BlockingScheduler
"""
more_info_img_path: str = os.path.join(os.getcwd(), 'more_info.png')





def click_more_info() -> None:
    coord = pyautogui.locateCenterOnScreen(
        more_info_img_path, confidence=0.9, grayscale=True)
    if coord:
        pyautogui.click(coord)
        print(f'{get_current_time()} | Refresh page!!!')
    else:
        print(f'{get_current_time()} | Element not found.')

if __name__ == "__main__":
    try:
        sched = BlockingScheduler()
        sched.add_job(click_more_info, 'interval', seconds=10)
        sched.get_jobs()
        sched.start()
    except Exception as e:
        print(e)
"""

def get_current_time() -> str:
    current_time = datetime.datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')

def load_img(img_filename: str) -> str:
	img_path: str = os.path.join(os.getcwd(), "img", img_filename)
	try:
		if not os.path.exists(img_path):
			raise FileNotFoundError(f"Image not found: {img_path}")
	except FileNotFoundError as e:
		print(e)
	return img_path

def _find_element(img_path: str) -> None:
	try:
		coord = pyautogui.locateCenterOnScreen(
			img_path,
			confidence=0.9,
			grayscale=True
        )
		pyautogui.click(coord)
		print(f'{get_current_time()} | Target clicked.')
	except pyautogui.ImageNotFoundException :
		print(f'{get_current_time()} | Element not found.')
	except IOError as e:
		print(f"Exception: {e}\n!!!Please check if the file exists in the 'img' folder.")

def target_click(img_path: str, check_interval: int | float) -> None:
	try:
		if not isinstance(check_interval, int | float):
			raise ValueError("Set checking interval as integer or float")
		sched = BlockingScheduler()
		sched.add_job(
			_find_element,
			"interval",
			seconds=check_interval,
			args=(img_path,)
        )
		sched.get_jobs()
		sched.start()
	except ValueError as e:
		print(e)
	except Exception as e:
		print(e)

if __name__ == "__main__":
	img_path = load_img("123.png")
	target_click(img_path, 1.2)
	
	