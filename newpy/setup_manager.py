# setup_manager.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html
# pylint: disable=no-name-in-module

import subprocess as sp
import datetime
import sys
import os

from colorama import init, Fore, Style

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


class PrepareSetup:
    """
    Prepare setup.py file
    """
    def __init__(self):
        init()

    def _get_personaldata(self):
        try:
            author_git = sp.check_output("git config --get user.name".split())
            author = author_git.decode('utf-8').strip()
            year = str(datetime.date.today().year)
            email = sp.check_output(
                "git config --get user.email".split()).decode('utf-8').strip()

            return {"author": author, "year": year, "email": email}
        except Exception:
            pass

    def _item(self, line, git_value, to_replace, git, prefix=None):
        if to_replace in line:
            git_data = self._get_personaldata()
            print(f"{Fore.YELLOW}{line.strip().split('=')[0]}", end=" = ")
            if git and prefix:
                get_item = input(
                    f"{Fore.GREEN}{prefix}{git_data.get(git_value)}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                )
                if get_item == "":
                    get_item = prefix + git_data.get(git_value)
            elif git:
                get_item = input(
                    f"{Fore.GREEN}{git_data.get(git_value)}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                )
                if get_item == "":
                    get_item = git_data.get(git_value)
            else:
                get_item = input(
                    f"{Fore.GREEN}{line.strip().split('=', maxsplit=1)[1]}{Style.RESET_ALL} press Enter if OK or enter new: {Fore.GREEN}"
                )
                if get_item == "":
                    get_item = str(line.strip().split('=', maxsplit=1)[1])
            return to_replace, get_item

    def fill_setup_template(self, projectpath):
        print(f"{Fore.CYAN}Fill setup.py...")
        head_message = "Enter or leave empty if default is OK:"
        print(f"{Fore.GREEN}{head_message}{Style.RESET_ALL}")
        print(len(head_message) * "=")
        with open(
                os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "templ_setup.py"), 'r') as template_setupfile:
            with open(os.path.join(projectpath, "setup.py"),
                      'w') as new_setupfile:
                for line in template_setupfile.readlines():
                    if "pkg-YOUR-USERNAME-HERE" in line:
                        line = line.replace(
                            *self._item(line,
                                        "author",
                                        "pkg-YOUR-USERNAME-HERE",
                                        prefix="pkg-",
                                        git=True))
                    elif "0.0.1" in line:
                        line = line.replace(
                            *self._item(line, None, "0.0.1", git=False))
                    elif "Example Author" in line:
                        line = line.replace(*self._item(line,
                                                        "author",
                                                        "Example Author",
                                                        prefix=None,
                                                        git=True))
                    elif "author@example.com" in line:
                        line = line.replace(*self._item(line,
                                                        "email",
                                                        "author@example.com",
                                                        prefix=None,
                                                        git=True))
                    elif "A small example package" in line:
                        line = line.replace(
                            *self._item(line,
                                        None,
                                        "A small example package",
                                        prefix=None,
                                        git=False))
                    elif ">=3.6" in line:
                        line = line.replace(*self._item(
                            line, None, ">=3.6", prefix=None, git=False))
                    new_setupfile.write(line)
                    print(f"{Fore.BLUE}{line}{Style.RESET_ALL}")

        print(
            f"{Fore.RED}Please review setup.py, .gitignore and change/add what is neccessary.{Style.RESET_ALL}\n"
        )


if __name__ == "__main__":
    ps = PrepareSetup()
    ps.fill_setup_template(".")