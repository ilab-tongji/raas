# coding=UTF-8
import serial
import time
import re


def my_sensor():
    flag = True
    try:
        ser = serial.Serial(port="COM4", baudrate=9600)        #读取串口com4数据
        #while True:
        for i in range(0, 2):
            data = ser.readline()
            data = data.strip()                                #去除空格换行
            str_data = bytes.decode(data)
            value = re.findall('\d+.?\d+', str_data)  # 只要数字
            if flag is True:
                hcho = value
                flag = False
            elif flag is False:
                light = value
                flag = True
            #time.sleep(2)                                      #两秒刷新
    except:
        ser.close()

    result = {"HCHO": str(hcho[0]), "light": str(light[0])}
    return result


if __name__ == '__main__':
    my_sensor()