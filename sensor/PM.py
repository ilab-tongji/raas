#coding=UTF-8

import time
import serial
import binascii


def my_pm():
    # try:
    #     ser = serial.Serial(port="COM3", baudrate=9600)
    #     return get_data(ser)
    # except:
    #     ser.close()
    pm_data = {'pm25': '18', 'pm10': '10'}
    return pm_data


def get_data(ser):

    data = ser.read(10)  # 读取串口10个字节数据
    all = str(binascii.hexlify(data))  # 获取端口需要数据，转为十六进制字符串
    low_1 = int(str(binascii.hexlify(data))[6], 16)  # 每个数位转为十进制数
    low_2 = int(str(binascii.hexlify(data))[7], 16)
    low_25 = low_1 * 16 + low_2  # pm2.5数值转为十进制
    high_1 = int(str(binascii.hexlify(data))[8], 16)
    high_2 = int(str(binascii.hexlify(data))[9], 16)
    high_25 = high_1 * 16 + high_2

    low_3 = int(str(binascii.hexlify(data))[10], 16)
    low_4 = int(str(binascii.hexlify(data))[11], 16)
    low_10 = low_3 * 16 + low_4
    high_3 = int(str(binascii.hexlify(data))[12], 16)
    high_4 = int(str(binascii.hexlify(data))[13], 16)
    high_10 = high_3 * 16 + high_4  # pm10数值转为十进制

    pm2_5 = ((high_25 * 256) + low_25) / 10  # 转为pm2.5含量
    pm10 = ((high_10 * 256) + low_10) / 10  # 转为pm10含量
    pm_data = {'pm25': pm2_5, 'pm10':pm10}
    return pm_data


if __name__ == '__main__':
    my_pm()

