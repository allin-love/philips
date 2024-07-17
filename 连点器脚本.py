import pyautogui  #这个库得安一下
import time

# 假设的按钮的屏幕坐标,可由截图软件等获得
button1_coords = (1829, 294)  # 右移按键位置
button2_coords = (1763, 251)  # 下移按键位置
button3_coords = (1695, 291)  # 左移按键位置

try:
    for _ in range(10):#扫描十个来回

        for _ in range(10):#  #从左到右扫描
            pyautogui.click(button1_coords)  # 点右移按钮十次
            time.sleep(0.5)  # 每次点击后短暂等待0.5秒

        pyautogui.click(button2_coords)  # 点击下移按钮一次

        time.sleep(0.5)  # 等待一段时间

        for _ in range(10):
            pyautogui.click(button3_coords)  # 点左移按钮十次
            time.sleep(0.5)  # 在每次点击后短暂等待0.5秒

        pyautogui.click(button2_coords)  # 点击下移按钮一次

        time.sleep(0.5) # 等待一段时间


finally:
    print("Script execution finished.")