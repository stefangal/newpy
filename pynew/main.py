# main.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import logging
import configparser
import fileconf as cg


MAJOR = 0
MINOR = 1
MICRO = 0
__version__ = f"{MAJOR}.{MINOR}.{MICRO}"

logger = logging.getLogger("new_project")
logger.setLevel(logging.DEBUG)


class Run:

    CONFIG_FILE = "config.ini"

    def __init__(self):
        # Logger
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
        )
        self.logger = logging.getLogger("new_project")
        self.log = logging.StreamHandler()
        self.log.setFormatter(formatter)
        self.logger.addHandler(self.log)
        # Configparser
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)
        # Methods to run
        if self.config_file_test():
            self.build_folder_structure()

    def project_details(self):
        print(self.config["GITHUB"]["UserName"])

    def github(self):
        pass

    def pypi(self):

        pass

    def config_file_test(self):
        check = cg.ConfigGenerator()
        if check.config_file_test("config.ini"):
            print("ALL OK\n".rjust(15))
            return True
        return False
        


    def build_folder_structure(self):   
        PATH = self.config["PROJECT"]["ProjectPath"]
        FILE = self.config["PROJECT"]["ProjectName"]
        filepath = os.path.join(PATH, FILE)

        if PATH and FILE and not os.path.exists(filepath):
            os.mkdir(path=os.path.join(PATH, FILE))
            if self.config["TODO"]["TestFolder"] == "True":
                os.mkdir(path=os.path.join(PATH, "tests"))
            if self.config["TODO"]["DocsFolder"] == "True":
                os.mkdir(path=os.path.join(PATH, "docs"))

            self.logger.info("Folder structure ready")

        if os.path.exists(filepath):
            with open(os.path.join(filepath, "main.py"), "w") as file:
                pass
            with open(os.path.join(PATH, ".gitignore"), "w") as file:
                pass
            with open(os.path.join(PATH, "LICENSE"), "w") as file:
                pass
            with open(os.path.join(PATH, "requirements.txt"), "w") as file:
                pass
            with open(os.path.join(PATH, "setup.py"), "w") as file:
                pass
            with open(os.path.join(PATH, "README.MD"), "w") as file:
                pass
        return True

    def build_file_structure(self):
        pass


if __name__ == "__main__":
    run = Run()

