# fileconf.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from configparser import ConfigParser, Error, ParsingError
from shutil import copyfile
import os
import re
from colorama import init, Fore, Style

from errors import MissingConfigFileError, MissingSectionError, MissingOptionError


class MissingFileSectionError(ParsingError):
    """
    Raised when a key-value pair is found before any section header.
    """
    def __init__(self, filename, line):
        super().__init__(
            self, 'File contains no section headers.\nfile: %r,\n%r' %
            (filename, line))
        self.source = filename
        self.line = line
        self.args = (filename, line)


class ConfigBuildCheck:
    """For checking and building the config.ini file"""
    def __init__(self):
        init()
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(self.root_dir, 'config.ini')
        self.config_template_file_path = os.path.join(self.root_dir,
                                                      'templ_config.ini')
        self.template_config = ConfigParser()
        self.template_config.read(self.config_template_file_path)
        self.config = ConfigParser()
        self.config.read(self.config_file_path)

    def new_config_file(self):
        """Generate new config.ini file."""
        try:
            copyfile(self.config_template_file_path, self.config_file_path)
            print(f"\n{Fore.GREEN} + CREATED: {self.config_file_path}")
        except Exception as exc:
            print(
                f"\n{Fore.RED} + FAILED TO CREATE: {self.config_file_path}\n")
            raise exc
        finally:
            print(Style.RESET_ALL)

    def check_sections_ok(self) -> bool:
        """Check sections available compared to the template in the config file."""
        missing_section, missing_line_nr = [], []
        for section in self.template_config.sections():
            if section not in self.config.sections():
                with open(self.config_template_file_path, 'r') as file:
                    for line_nr, line in enumerate(file, 1):
                        if section in line:
                            missing_section.append(section)
                            missing_line_nr.append(line_nr)
        if missing_section:
            raise MissingSectionError()
        return True

    def check_options_ok(self) -> bool:
        """Check options available compared to the template in the config file."""
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


class ConfigRead:
    """
    Read in the config.ini data.
    """

    _CONFIG_FILE = "config/config.ini"

    def __init__(self):
        self.config = ConfigParser()
        self.path = self.config["PROJECT"]["projectpath"]
        self.file = self.config["PROJECT"]["projectname"]
        self.project_path = os.path.join(self.path, self.file)

        if len(self.config.read(self._CONFIG_FILE)) == []:
            raise MissingConfigFileError(self._CONFIG_FILE)

    def project_in_config_check(self):
        return True if os.path.exists(self.project_path) else False
        # builder = Builder(self.project_path, self.config)
        # builder.folder_structure()

    def pypi_in_config_check(self):
        author = self.config['PYPI']['Author']
        author_email = self.config['PYPI']['AuthorEmail']
        _pattern_email = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}"
        email_format = re.search(_pattern_email, author_email)
        description = self.config['PYPI']['Description']
        version = self.config['PYPI']['Version']
        release = self.config['PYPI']['Release']
        return all([author, email_format, description, version, release])

    @property
    def get_project_name(self):
        return self.file if self.file else None

    @property
    def get_project_path(self):
        return self.path if self.path else None

    @property
    def get_project_folder(self):
        return os.path.join(self.get_project_path, self.get_project_name)


if __name__ == "__main__":
    # cbc = ConfigBuildCheck()
    # run.new_config_fi0jnuih76tle()
    # cbc.check_sections_ok()
    # cbc.check_options_ok()
    cr = ConfigRead()
    cr.project_in_config_check()