from base import *
from devices import *

class Renesas_PKS5D9ser(Board):
    @staticmethod
    def match(dev):
        return dev["vid"] =="0403" and dev["pid"]=="6001"

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        pass
    
    def __init__(self,info={},dev={}):
        super().__init__(info,dev)
        self._info["name"] = "Renesas PK-S5D9 Serial"
