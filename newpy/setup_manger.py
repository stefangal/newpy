# setup_manager.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html

import subprocess as sp
import datetime
import configparser
import sys
import os

from colorama.initialise import init

from config_bc import ConfigRead

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# from main import Run


class PrepareSetup:
    def __init__(self, _conf):        
        self.conf_read = _conf
        self.PROJECT_PATH = None
        self.FILE = None

    def _get_personaldata(self) -> dict:
        try:
            author_git = sp.check_output("git config --get user.name".split())
            author = author_git.decode('utf-8').strip()
            year = str(datetime.date.today().year)
            email = sp.check_output("git config --get user.email".split()).decode('utf-8').strip()
  
            return {
                "author": author,
                "year": year,
                "email": email
            }
        except Exception:
            pass

    def fill_setup_template(self, projectpath):
        git_data = self._get_personaldata()
 
        with open("newpy/templ_setup.py", 'r') as template_setupfile:
            with open(os.path.join(projectpath, "setup.py"), 'w') as new_setupfile:
                for line in template_setupfile.readlines():                    
                    if "example-pkg-YOUR-USERNAME-HERE" in line:
                        line = line.replace("YOUR-USERNAME-HERE", git_data.get('author'))
                    elif "Example Author" in line:
                        line = line.replace("Example Author", git_data.get('author'))
                    elif "author@example.com" in line:
                        line = line.replace ("author@example.com", git_data.get('email'))
                    new_setupfile.write(line)
    

if __name__ == "__main__":
    ps = PrepareSetup()
    print(ps.get_personaldata())
    # ps.fill_setup_template()