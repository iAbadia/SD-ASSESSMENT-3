import json
import persistence as ps


class Config:

    def __init__(self):
        self.jconfig = ps.get_config()

    def get_colorblind(self):
        return self.jconfig["colorblind"]

    def get_lowres(self):
        return self.jconfig["lowres"]

    def get_reduceflicker(self):
        return self.jconfig["reduceflicker"]

    def set_colorblind(self, colorblind):
        self.jconfig["colorblind"] = colorblind
        ps.save_config(self.jconfig)

    def set_lowres(self, lowres):
        self.jconfig["lowres"] = lowres
        ps.save_config(self.jconfig)

    def set_reduceclicker(self, reduceclicker):
        self.jconfig["reduceclicker"] = reduceclicker
        ps.save_config(self.jconfig)
