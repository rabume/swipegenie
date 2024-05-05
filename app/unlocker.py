from ppadb.device import Device
import time


class Unlock:

    def __init__(self, device: Device, passwd: str):
        self.main_device = device
        self.passwd = passwd
        self.status = True
        self.__check_status()
        self.__unlock()

    def __check_status(self):
        _command = "dumpsys power | grep 'mWakefulness='"
        status = str(self.main_device.shell(_command).split("=")[1].strip())
        self.status = status in ("Asleep", "Dozing")

    def __unlock(self):
        self.__check_status()

        _open_command = "input keyevent 26"
        _unlock_command = (
            f"input swipe 600 600 0 0 && input text {self.passwd} && input keyevent 66"
        )

        if self.status:
            self.main_device.shell(_open_command)
            time.sleep(1)

        self.main_device.shell(_unlock_command)
