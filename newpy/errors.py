# errors.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php


class ConfigFileErrors(Exception):
    """Base exception class
    
    All NewPy exceptions should be subclass this class.
 """


class MissingConfigFileError(ConfigFileErrors):
    """
    Exception for the project when the config.ini file is missing.
    """
    def __init__(self, file) -> None:
        self.file = file

    def __str__(self) -> str:
        return f"File config.ini is missing or filename is incorrect! Check {self.file} !"
    

class MissingSectionError(ConfigFileErrors):
    """
    Exception for the project when section is missing or incorrectly written in the config.ini file.
    """
    pass


class MissingOptionError(ConfigFileErrors):
    """
    Exception for the project when option is missing or incorrectly written in the config.ini file.
    """
    pass
