import configparser
import os

self_py_name = os.path.basename(__file__)


class Config(object):
    pass


class IniConfig(Config):
    def __init__(self, read_file_name: str = None):
        self.c = configparser.ConfigParser()
        self.read_file_name = read_file_name
        if self.read_file_name is not None:
            self.read(self.read_file_name)

    def add_section(self, a: str):
        self.c.add_section(a)

    def set(self, section: str, k: str, v: str):
        if not self.c.has_section(section):
            self.c.add_section(section)
        self.c.set(section, k, v)

    def write(self, file_name: str):
        self.c.write(open(file_name, "w"))

    def write_back_to_read_file(self):
        self.write(self.read_file_name)

    def read(self, file_name: str):
        self.c.read(file_name)

    def get(self, section: str, k: str):
        return self.c.get(section, k)

    def getint(self, section: str, k: str):
        return self.c.getint(section, k)

    def getfloat(self, section: str, k: str):
        return self.c.getfloat(section, k)

    def getboolean(self, section: str, k: str):
        return self.c.getboolean(section, k)

    def __str__(self):
        return self.read_file_name
