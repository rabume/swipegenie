from ppadb.device import Device
import time
from pathlib import Path
from app.ai import AI

import os


class Swipe:

    def __init__(self, device: Device, ai: AI):
        self.main_device = device
        self.ai = ai

    def __closing_msg(self):
        _command = "input keyevent 111"
        self.main_device.shell(_command)
        time.sleep(2)

    def __swipe_right(self):
        print("[>] Swiping Right")
        _command = "input swipe 100 500 500 500 50"
        self.main_device.shell(_command)
        self.__closing_msg()

    def __swipe_left(self):
        print("[<] Swiping Left")
        _command = "input swipe 100 500 -500 500 50"
        self.main_device.shell(_command)
        self.__closing_msg()

    def decide(self):
        if os.getenv("ALWAYS_SWIPE_RIGHT") == "true":
            print("[>] Swiping Right")
            self.__swipe_right()
            return

        path = Path("./temp/temp.png")
        image = path.read_bytes()

        swipe = self.ai.swipe(image)

        if swipe == "left":
            self.__swipe_left()
        else:
            self.__swipe_right()
