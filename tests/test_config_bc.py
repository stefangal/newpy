import pytest
from ..newpy.config_bc import ConfigBuildCheck
from configparser import ConfigParser, Error, ParsingError
from colorama import init, Fore, Style
from shutil import copyfile
import os
import re


class TestMethods:

    @pytest.fixture(scope='function')
    def start_init(self):
        init()
        self.template_config = ConfigBuildCheck()
        self.template_config = ConfigParser()
        self.template_config.read(ConfigBuildCheck.CONFIG_TEMPLATE_FILE_PATH)
        self.config = ConfigParser()
        self.config.read(ConfigBuildCheck.CONFIG_FILE_PATH)

    def test_nr1(self, start_init):
        missing_section, missing_line_nr = [], []
        for section in  self.template_config.sections():
                if section not in self.config.sections():
                    with open(ConfigBuildCheck.CONFIG_TEMPLATE_FILE_PATH, 'r') as file:
                        for line_nr, line in enumerate(file, 1):
                            if section in line:
                                missing_section.append(section)
                                missing_line_nr.append(line_nr)
        print(missing_section)
        assert  missing_section == ['PROJECT', 'GITHUB', 'TODO', 'PYPI']