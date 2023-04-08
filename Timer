import winsound as ws
from datetime import datetime, timedelta
from threading import Thread
class Timer:
    def __init__(self):
        self._stop = None
        self._start = datetime.now()

    def reset(self):
        """Changes timer start time to now and returns 00:00:00"""
        self._start = datetime.now()
        return '00:00:00'

    def elapsed_time(self) -> str:
        """Returns the elapsed time since the start time was set"""
        time_diff = datetime.now() - self._start
        self._stop = time_diff
        return str(time_diff)[2:7] + ':' + str(time_diff)[8:10]

    def stop(self):
        """returns the last value from the previous elapsed_time call"""
        if self._stop:
            return str(self._stop)[2:7] + ':' + str(self._stop)[8:10]
        return 'TIMER ERROR'


class Calc:
    def __init__(self):
        self.__maxsize = 10

    def solve(self, expression) -> str:
        """Uses eval on given arithmetic expression"""
        if not expression:
            return '0'
        try:
            result = eval(expression)
            result = str(round(result, 2)) if isinstance(result, float) else str(result)
            if len(result) > self.__maxsize:
                return 'DCSAOvfl'
            return result
        except Exception as e:
            return f'DCSAErr:\n\t{e}'


class Alarm:
    def __init__(self):
        self.on = False
        self.gotime = None
        self.repeats = 3
        self.tune = 'intro.wav'
        self.set('10.30.00')
        self.snd = Thread(target=self.sound, daemon=True)
        self.snd.start()

    def toggle(self, on=0):
        """Toggle alarm on/off and returns alarm time and state"""
        self.on = on
        return self.get_gotime()

    def get_gotime(self):
        """Returns alarm time and state"""
        if self.gotime:
            return ("On->" if self.on else "Off->") + self.gotime.strftime('%H:%M:%S')
        else:
            return ("On->" if self.on else "Off->"), "00.00.00"

    def set(self, time):
        """Takes a time as a string from user to set the alarms gotime
         Expected input time string format: 00.00.00 """
        td = datetime.today()
        try:
            hrs, mins, sec = time.split('.')
            self.gotime = datetime(year=td.year, month=td.month, day=td.day,
                                   hour=int(hrs), minute=int(mins), second=int(sec))
            return self.get_gotime()
        except Exception as e:
            return f'AlarmErr:\n\t{e}'

    def sound(self):
        """Sounds alarm if the current time is within a minute of go time"""
        try:
            if self.on:
                if abs(datetime.now() - self.gotime) < timedelta(minutes=1):
                    for i in range(self.repeats):
                        ws.PlaySound(self.tune, ws.SND_FILENAME)
                        self.repeats -= 1
        except Exception as e:
            return f'AlarmErr:\n\t{e}'

if __name__ == '__main__':
    ...
