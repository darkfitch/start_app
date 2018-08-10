# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import pywinauto

path = [{'微信':"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"},{'QQ':"D:\QQ\Bin\QQScLauncher.exe"}]
list_item =list([list(dicts.keys()) for dicts in path])
config_file = 'config.json'
def get_path():
    sys_version = sys.version
    if sys_version[0] == '3':
        pass
    current_path = os.getcwd()
    file_list = os.listdir(current_path)
    for item in file_list:
        config_path = ''
        if config_file in item:
            config_path = os.path.join(current_path,config_file)
            break
    try:
        with open(config_path, 'r') as f:
            temp = []
            for i in f:
                temp.append(i)
            # temp = f.readline()
            print(temp)


            temp_a = json.load(f)
            print(temp_a)


    except Exception as e:
        print(e)
        # with open()


def start_app():
    app = pywinauto.Application()
    while True:
        for index in range(len(list_item)):
            print(index+1, ':' + list_item[index][0])
        print('按0退出')
        print('='*50)
        try:
            get_input = int(input('input index:'))
            if get_input == 0:
                break
            else:
                real_path = list(path[get_input-1].values())[0]
                # 开启程序的方法1
                # os.startfile(real_path)

                # 开启程序 方法二:
                try:
                    app.start(real_path)
                    
                except:
                    pass
                print('\n\n')

        except Exception as e:
            print ('输入序号异常,即将退出')
            time.sleep(1)
            a = '异常退出'
            break

if __name__ == '__main__':
    # start_app()
    get_path()

