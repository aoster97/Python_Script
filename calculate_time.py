from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

url = "https://www.bilibili.com/video/BV1fh411y7R8/?p=48&vd_source=6248bbe156e0f31bc6697c05cf70952c"

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):  # 如果是时间格式
            return self.add_time(other)
        else:  # 如果是数字格式
            return self.increment(other)

    def __radd__(self, other):
        """右加方法"""
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time2int() + other.time2int()
        return int2time(seconds)

    def increment(self, seconds):
        seconds += self.time2int()
        return int2time(seconds)

    def time2int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds


def int2time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# time = Time(2, 3, 5)
# duration = Time(8, 5, 6)
# print(time + duration)
# print(time + 1337)
# print(1337 + time)
#
# t1 = Time(22, 43)
# t2 = Time(20, 41)
# t3 = Time(23, 37)
# total = sum([t1, t2, t3])
# print(total)

def opendriver():
    driver = webdriver.Chrome()
    return driver


def main(start, end):
    driver = opendriver()
    # 寻找时间元素
    sleep(10)
    driver.get(url)
    the_ul = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[7]/div[2]/ul')
    lis = the_ul.find_elements(By.TAG_NAME, 'li')

    time_list = []
    for index, value in enumerate(lis):
        xpath = '/html/body/div[2]/div[2]/div[2]/div/div[7]/div[2]/ul/li[{0}]/a/div/div[2]'.format(index + 1)
        txt = value.find_element(By.XPATH, xpath).text
        if txt == '':
            list_p = driver.find_element(By.CLASS_NAME, 'cur-list')
            ActionChains(driver) \
                .move_to_element(list_p) \
                .perform()
            scroll_origin = ScrollOrigin.from_element(list_p)
            ActionChains(driver) \
                .scroll_from_origin(scroll_origin, 0, 10000) \
                .perform()
        print("TXT{0}: ".format(index + 1), txt)

        if (index >= start + 1) and (index <= end + 1):
            time_list.append(txt)

    print('**************************************************************')
    for index3 in range(len(time_list)):
        print(time_list[index3])
    print('**************************************************************')

    time_tot = Time(0, 0, 0)
    for index2 in range(len(time_list)):
        minandsec = time_list[index2].split(":")
        v_m = int(minandsec[0])
        v_s = int(minandsec[1])
        time1 = Time(0, v_m, v_s)
        time_tot = time_tot + time1
    print("总时间是:{0}".format(time_tot))

    return 0


if __name__ == '__main__':
    # 计算第一集到
    main(1, 3)
    print('结束')
