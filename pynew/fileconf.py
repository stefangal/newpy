# fileconf.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from configparser import ConfigParser, Error, ParsingError
import os
from colorama import init, Fore, Style
from shutil import copyfile


class MissingSectionError(ParsingError):
    """Raised when a key-value pair is found before any section header."""
    def __init__(self, filename, line):
        Error.__init__(
            self, 'File contains no section headers.\nfile: %r,\n%r' %
            (filename, line))
        self.source = filename
        self.line = line
        self.args = (filename, line)


class ConfigGenerator:
    """
    =========== debug ===========
    content = {
        "PROJECT": {
            "ProjectName": "project",
            "ProjectPath": "/Users/stefangal/Documents/Coding/Python/Projects",
        },
        "GITHUB": {
            "UserName": "stefangal",
            "GithubRepo": "True",
            "GitPush": "True",
            "GitToken": "8a35fdf7e3cf5a2e3dd5934a732faa776dfd6702",
            "Private": "True"
        },
        "TODO": {
            "DocsFolder": "True",
            "TestFolder": "True",
        },
        "PYPI": {
            "Author": "Stefan Gal",
            "AuthorEmail": "xxx@xxx.com",
            "Description": "xxx",
            "Version": "0.0.1",
            "Release": "False",
        },
    }
    =========== debug ===========
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_FILE_PATH = os.path.join(ROOT_DIR, 'config.ini')
    CONFIG_TEMPLATE_FILE_PATH = os.path.join(ROOT_DIR, 'templ_config.ini')

    def __init__(self):
        init()
        self.template_config = ConfigParser()
        self.template_config.read(self.CONFIG_TEMPLATE_FILE_PATH)
        self.config = ConfigParser()
        self.config.read(self.CONFIG_FILE_PATH)

    def new_config_file(self):
        """
        Generate new config.ini file.
        """
        try:
            copyfile(self.CONFIG_TEMPLATE_FILE_PATH, self.CONFIG_FILE_PATH)
            print(f"\n{Fore.GREEN} + CREATED: {self.CONFIG_FILE_PATH}")
        except Exception as e:
            print(
                f"\n{Fore.RED} + FAILED TO CREATE: {self.CONFIG_FILE_PATH}\n")
            raise e
        finally:
            print(Style.RESET_ALL)

    def check_sections_ok(self) -> bool:
        """
        Check sections available compared to the template in the config file.
        """
        missing_section, missing_line_nr = [], []
        for section in self.template_config.sections():
            if section not in self.config.sections():
                with open(self.CONFIG_TEMPLATE_FILE_PATH, 'r') as file:
                    for line_nr, line in enumerate(file, 1):
                        if section in line:
                            missing_section.append(section)
                            missing_line_nr.append(line_nr)
        if missing_section:
            raise MissingSectionError(
                self.CONFIG_FILE_PATH,
                f'{Fore.RED} + Missing section: {missing_section} on lines {missing_line_nr}'
            )
        return True

    def check_options_ok(self) -> bool:
        """
        Check options available compared to the template in the config file.
        """
        structure, missing_option = [], []
        file_ok = True
        for section in self.config.sections():
            for option in self.config.options(section):
                structure.append((section, option))
        for section in self.template_config.sections():
            for option in self.template_config.options(section):
                if (section, option) not in structure:
                    file_ok = False
                    missing_option.append(str(section + "->" + option))
        if not file_ok:
            raise Error(
                f"{Fore.RED} + Missing or corrupt option: {missing_option}")
        return file_ok


if __name__ == "__main__":
    run = ConfigGenerator()
    # run.new_config_file()
    run.check_sections_ok()
    run.check_options_ok()