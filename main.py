# main.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import re
import click
import logging
import configparser
from subprocess import check_output

from newpy.config_bc import MissingFileSectionError, ConfigBuildCheck, ConfigRead
from newpy.license import NewLicense
from newpy.setup_manger import PrepareSetup
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
        # Initiallize classes
        self.cbc = ConfigBuildCheck()
        self.cr = ConfigRead()

        self.run()
        
 
    def _config_file_check(self):
        config_file_ok = True
        if self.cbc.check_sections_ok():
            self.logger.info("Sections in config file OK")
        else:
            config_file_ok = False
            self.logger.error("Config file is CORRUPT! Issue with sections")     
        if self.cbc.check_options_ok:           
            self.logger.info("Options in config file OK")
        else:
            config_file_ok = False
            self.logger.error("Config file is CORRUPT! Issue with options")
        if not config_file_ok:
            self.solve_config_file()
        else:
            self.logger.info("Config file is OK, I will use it.")

    def show_config(self):
        cr = ConfigRead()
        cr.visuallize()


    def solve_config_file(self):
        # if config_file_check is False this runs
        print("Issue with config file!")
        gen_or_stop = int(input("Do you want generate new file (1) or stop script (2) and manually correct the config file? >  "))
        if gen_or_stop == 1:
            self.cbc.new_config_file()
        exit(1)

    def run(self):
        os.system('clear')
        self._config_file_check()
        self.show_config()
    

@click.command()
def run(): 
    Newpy()

if __name__ == "__main__":
    Newpy()
    
