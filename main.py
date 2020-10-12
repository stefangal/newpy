# main.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import re
import logging
import configparser

from newpy.config_bc import ConfigBuildCheck
from newpy.license import NewLicense
# from newpy.setup_manger import PrepareSetup
from newpy.repo import OpenRepo

MAJOR = 0
MINOR = 1
MICRO = 0
__version__ = f"{MAJOR}.{MINOR}.{MICRO}"

logger = logging.getLogger("new_project")
logger.setLevel(logging.DEBUG)


class Newpy:
    """
    This is the main logic class.
    > Overall check before run
    > Run based on config.ini file
    > Generate output
    """

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



    

    
    def project_details(self):
        print(self.config["GITHUB"]["UserName"])

    def github(self):
        pass

    def pypi(self):
        pass



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
        with open(os.path.join(self.PATH, "README.md"), "w") as file:
            pass

    def build_requirements_txt(self):
        with open(os.path.join(self.PATH, "requirements.txt"), "w") as file:
            pass

    def build_gitignore(self):
        with open(os.path.join(self.PATH, ".gitignore"), "w") as file:
            pass


if __name__ == "__main__":
    run = Newpy()
