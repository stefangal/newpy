import os
import configparser



MAJOR = 0
MINOR = 91
MICRO = 0

__version__ = f'{MAJOR}.{MINOR}.{MICRO}'


class Run:

    CONFIG_FILE = 'config.ini'

    def __init__(self):
        self.config = configparser.ConfigParser()
        
    def project_details(self):
        self.config.read(self.CONFIG_FILE)
        print(self.config['GITHUB']['UserName'])

    def github(self):
        pass

    def pypi(self):

        pass

    def build_structure(self):
        pass

    def start(self):
        self.project_details()
if __name__ == "__main__":
    run = Run()
    run.start()