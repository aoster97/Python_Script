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


time = Time(2, 30, 5)
duration = Time(8, 5, 6)
print(time)
print(duration)
print(time + duration)
print(time + 1337)
print(1337 + time)

t1 = Time(22, 43)
t2 = Time(20, 41)
t3 = Time(23, 37)
total = sum([t1, t2, t3])
print(total)
