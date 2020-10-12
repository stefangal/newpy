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

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from main import Run


class PrepareSetup(Run):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIG_FILE)

    def get_personaldata(self) -> dict:
        try:
            author_git = sp.check_output("git config --get user.name".split())
            author = author_git.decode('utf-8').strip()
            year = str(datetime.date.today().year)
            project_name = self._get_projectname()
            project_path = self._get_projectpath()
            email = sp.check_output("git config --get user.email".split()).decode('utf-8').strip()
  
            return {
                "author": author,
                "year": year,
                "projectname": project_name,
                "projectpath":project_path,
                "email": email
            }
        except Exception:
            pass

    def fill_setup_template(self):
        git_data = self.get_personaldata()
        PATH = git_data.get('projectpath')

        with open("pynew/templ_setup.py", 'r') as template_setupfile:
            with open(os.path.join(PATH, "setup.py"), 'w') as new_setupfile:
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