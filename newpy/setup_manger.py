# setup_manager.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html

import subprocess as sp
import datetime
import sys
import os

from colorama import init, Fore, Style
from config_bc import ConfigRead

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


class PrepareSetup:
    def _get_personaldata(self) -> dict:
        try:
            author_git = sp.check_output("git config --get user.name".split())
            author = author_git.decode('utf-8').strip()
            year = str(datetime.date.today().year)
            email = sp.check_output(
                "git config --get user.email".split()).decode('utf-8').strip()

            return {"author": author, "year": year, "email": email}
        except Exception:
            pass
    
    def _line_action(self, line, git_value, to_replace, prefix=None):
        # prefix = 'pkg-'
        if to_replace in line:
            git_data = self._get_personaldata()
            print(f"{Fore.YELLOW}{line.strip().split('=')[0]}", end=" = ")
            get_item = input(f"{Fore.GREEN}{prefix}{git_data.get(git_value)}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}")
            if get_item == "":
                get_item = prefix + git_data.get(git_value)
                line = line.replace(to_replace, get_item)

    def fill_setup_template(self, projectpath):
        
        os.system("clear")
        print(f"{Fore.CYAN}Fill setup.py...")
        head_message = "Enter or leave empty if default is OK:"
        print(f"{Fore.GREEN}{head_message}{Style.RESET_ALL}")
        print(len(head_message) * "=")
        with open("newpy/templ_setup.py", 'r') as template_setupfile:
            with open(os.path.join(projectpath, "setup.py"),
                      'w') as new_setupfile:
                for line in template_setupfile.readlines():
                    if "pkg-YOUR-USERNAME-HERE" in line:
                        print(f"{Fore.YELLOW}{line.strip().split('=')[0]}",
                              end=" = ")
                        get_name = input(
                            f"{Fore.GREEN}pkg-{git_data.get('author')}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                        )
                        if get_name == "":
                            get_name = "pkg-" + git_data.get('author')
                        line = line.replace("example-pkg-YOUR-USERNAME-HERE",
                                            get_name)
                    if "0.0.1" in line:
                        print(f"{Fore.YELLOW}{line.strip().split('=')[0]}",
                              end=" = ")
                        get_version = input(
                            f"{Fore.GREEN}{line.strip().split('=')[1]}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                        )
                        if get_version == "":
                            get_version = line.strip().split('=')[1]
                        line = line.replace("0.0.1",
                                            get_version)
                    elif "Example Author" in line:
                        print(f"{Fore.YELLOW}{line.strip().split('=')[0]}",
                              end=" = ")
                        get_author = input(
                            f"{Fore.GREEN}{git_data.get('author')}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                        )
                        if get_author == "":
                            get_author = git_data.get('author')
                        line = line.replace("Example Author", get_author)
                    elif "author@example.com" in line:
                        print(f"{Fore.YELLOW}{line.strip().split('=')[0]}",
                              end=" = ")
                        get_email = input(
                            f"{Fore.GREEN}{git_data.get('email')}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                        )
                        if get_email == "":
                            get_email = git_data.get('email')
                        line = line.replace("author@example.com", get_email)
                    elif "A small example package" in line:
                        print(f"{Fore.YELLOW}{line.strip().split('=')[0]}",
                              end=" = ")
                        get_description = input(f"{Fore.GREEN}")
                        line = line.replace("A small example package",
                                            get_description)
                    elif ">=3.6" in line:
                        get_python_req = line.strip().split('=', maxsplit=1)
                        print(f"{Fore.YELLOW}{get_python_req[0]}",
                              end=" = ")
                        get_python = input(f"{get_python_req[1]}{Fore.GREEN}")
                        if get_python == "":
                            get_python = get_python_req[1]
                        line = line.replace(">=3.6", get_python)

                    new_setupfile.write(line)
                    print(f"+{Fore.BLUE}{line}{Style.RESET_ALL}")

        print(
            f"{Fore.RED}Please review setup.py and change, add what is neccessary.{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    ps = PrepareSetup()
    ps.fill_setup_template(".")