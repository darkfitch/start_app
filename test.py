# -*- coding:utf-8 -*-

import os
import time
import pyautogui
import pywinauto
from pywinauto.application import Application
import random
import PIL


if __name__ == '__main__':
    app = Application()
    # print(pyautogui.size())
    # print(pyautogui.position())
    x,y = pyautogui.size()
    # pyautogui.moveRel(500,500,2)

    t_path = 'D:\QQ\Bin\QQScLauncher.exe'

    # times = 10
    # while times > 0:
    #     pyautogui.moveRel(random.randint(-x/2,x/2),random.randint(-y/2,y/2))
    #     times -= 1
    #     time.sleep(0.5)d
    # pyautogui.hotkey('ctrl','shift','-')
    # a = pyautogui.hotkey('win','r')
    # a = pyautogui.hotkey('win','d')
    # app.connect(u'运行')
    # a = pyautogui.typewrite(t_path+'\n')
    pyautogui.press(['right','right'])
    # pyautogui.alert('弹窗')
    # pyautogui.confirm('弹窗')
    # temp_a = pyautogui.prompt('弹窗')
    # print(temp_a)
    # time.sleep(1)
    # pyautogui.screenshot('a.png')
    # pyautogui.screenshot('a.jpg')
    # size1 = pyautogui.locateOnScreen('a.jpg')
    # size2 = pyautogui.locateOnScreen('a.png')
    # print(size1)
    # print(size2)
    # pyautogui.scroll(200)
    temp = pyautogui.password()
    print(temp)

    # 其实已经拿到进程了,说明这个app是有效的 应该也可以使用pywinauto的方法去操控窗口了
    # pid = os.getpid()
    # app.connect(process=pid)
    # print(pid)
    #
    # print(pid)
