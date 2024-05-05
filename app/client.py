import sys
import time
from ppadb.client import Client
from app.unlocker import Unlock
from app.check import TinderCheck
from app.inputs import Swipe
from app.screen_capture import Capture
from app.ai import AI


class Client(Client):
    def __init__(self, passwd):
        super().__init__()
        self.main_device = None
        self.ai = AI()
        self.passwd = passwd
        self.__show_connected_devices()
        self.__select_main_device()
        self.__unlock_phone()
        self.__check_tinder()

    def __show_connected_devices(self):
        print(f"Total Connected Devices {len(self.devices())}\n")
        for idx, device in enumerate(self.devices()):
            print(f"Device #{idx + 1}'s Serial: {device.serial}")

    def __select_main_device(self):
        self.main_device = (
            self.devices()[0] if len(self.devices()) > 0 else self.__close()
        )
        print(f"\nSelecting Main Device as {self.main_device.serial}")

    def __check_tinder(self):
        tinder = TinderCheck(self.main_device)
        if tinder.exists:
            time.sleep(5)
            self.__start()

    def __start(self):
        while True:
            screen = Capture(self.main_device)
            screen.capture()
            time.sleep(1)
            Swipe(self.main_device, self.ai).decide()

    def __unlock_phone(self):
        Unlock(self.main_device, self.passwd)

    def __close(self):
        sys.exit(f"Device Not Detected. Device Count {len(self.devices())}")
