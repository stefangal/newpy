# main.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import configparser
import logging
import os
import re

from pynew.fileconf import ConfigGenerator


MAJOR = 0
MINOR = 1
MICRO = 0
__version__ = f"{MAJOR}.{MINOR}.{MICRO}"

logger = logging.getLogger("new_project")
logger.setLevel(logging.DEBUG)


class Run:
    """
    This is the main logic class.
    > Overall check before run
    > Run based on config.ini file
    > Generate output
    """
    CONFIG_FILE = "config.ini"

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    PATH = config["PROJECT"]["ProjectPath"]
    FILE = config["PROJECT"]["ProjectName"]
    PROJECT_PATH = os.path.join(PATH, FILE)

    def __init__(self):
        # Logger
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
        )
        self.logger = logging.getLogger("new_project")
        self.log = logging.StreamHandler()
        self.log.setFormatter(formatter)
        self.logger.addHandler(self.log)
        # Initial checks
        self.project_in_config_check()
        print(self.pypi_in_config_check())
        # Methods to run ON DEVELOPMENT stage
        if self.config_file_test():
            self.build_folder_structure()

    def project_in_config_check(self):
        if self.PATH and self.FILE:
            print(
                f"\033[93mSTATUS:\033[0m Project folder:\033[94m...{self.PATH[-10:]}/{self.FILE}\033[0m OK"
            )
            return True
        self.logger.error('Something wrong with config.ini PROJECT section!!!')
        return False

    def pypi_in_config_check(self):
        author = self.config['PYPI']['Author']
        author_email = self.config['PYPI']['AuthorEmail']
        _pattern_email = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}"
        email_format = re.search(_pattern_email, author_email)
        description = self.config['PYPI']['Description']
        version = self.config['PYPI']['Version']
        release = self.config['PYPI']['Release']
        return all([author, email_format, description, version, release])

    def project_details(self):
        print(self.config["GITHUB"]["UserName"])

    def github(self):
        pass

    def pypi(self):
        pass

    def config_file_test(self):
        check = ConfigGenerator()
        if check.config_file_test("config.ini"):
            print("ALL OK\n".rjust(15))
            return True
        return False

    def build_folder_structure(self):
        if self.PATH and self.FILE and not os.path.exists(self.PROJECT_PATH):
            os.mkdir(path=self.PROJECT_PATH)
            if self.config["TODO"]["TestFolder"] == "True":
                os.mkdir(path=os.path.join(self.PATH, "tests"))
            if self.config["TODO"]["DocsFolder"] == "True":
                os.mkdir(path=os.path.join(self.PATH, "docs"))

        self.logger.info("Folder structure ready")

        return True

    def build_license(self):
        with open(os.path.join(self.PATH, "LICENSE"), "w") as file:
            pass

    def build_setup_py(self):
        with open(os.path.join(self.PATH, "setup.py"), "w") as file:
            pass

    def build_readme_md(self):
        with open(os.path.join(self.PATH, "README.MD"), "w") as file:
            pass

    def build_requirements_txt(self):
        with open(os.path.join(self.PATH, "requirements.txt"), "w") as file:
            pass

    def build_gitignore(self):
        with open(os.path.join(self.PATH, ".gitignore"), "w") as file:
            pass


if __name__ == "__main__":
    run = Run()
