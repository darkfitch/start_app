# -*- coding: utf-8 -*-

import os
import sys
import time

path = [{'微信':"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"},{'QQ':"D:\QQ\Bin\QQScLauncher.exe"}]
list_item =list([list(dicts.keys()) for dicts in path])
config_file = 'config.txt'
def get_path():
    print(sys.version)
    current_path = os.getcwd()
    file_list = os.listdir(current_path)
    print(file_list)
    for item in file_list:
        config_path = ''
        if config_file in item:
            config_path = os.path.join(current_path,config_file)
            break
    try:
        with open(config_path, 'rb') as f:
            temp = f.readlines()
            print(temp)
    except Exception as e:
        print(e)
        # with open()


def start_app():
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
                os.startfile(real_path)
                print('\n\n')

        except Exception as e:
            print ('输入序号异常,即将退出')
            time.sleep(1)
            a = '异常退出'
            break

if __name__ == '__main__':
    # start_app()
    get_path()

