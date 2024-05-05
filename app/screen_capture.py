import os
from ppadb.device import Device
from pathlib import Path


class Capture:

    def __init__(self, device: Device):
        self.main_device = device
        self.base_dir = Path(__file__).resolve().parent.parent
        self.__create_dir()

    def __create_dir(self):
        if os.path.exists(f"{self.base_dir}/temp"):
            return
        print(f"Creating temp Directory In {self.base_dir}")
        os.mkdir(f"{self.base_dir}/temp")

    def capture(self):
        _command = "screencap -p sdcard/tinder_check.png"
        self.main_device.shell(_command)
        self.__save()

    def __save(self):
        self.main_device.pull(
            "/sdcard/tinder_check.png", f"{self.base_dir}/temp/temp.png"
        )
