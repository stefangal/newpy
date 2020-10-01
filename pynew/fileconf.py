# fileconf.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import configparser


class ConfigGenerator(object):
    content = {
        "PROJECT": {
            "ProjectName": "project",
            "ProjectPath": "/Users/stefangal/Documents/Coding/Python/Projects",
        },
        "GITHUB": {
            "UserName": "stefangal",
            "GithubRepo": "True",
            "GitPush": "True",
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

    def new_config_file(self, path):
        config = configparser.ConfigParser()
        with open(os.path.join(path, "config_tmp.ini"), "w") as configfile:
            for section, values in self.content.items():
                config[section] = {}
                for key, value in values.items():
                    config[section][key] = value
            config.write(configfile)

    def config_file_test(self, file):
        file_OK = True
        config = configparser.ConfigParser()
        config.read(file)

        print(9 * "_", end="")
        print("Sections", end="")
        print(9 * "_")
        # sections available correctly
        for section in self.content:
            # print(section)
            if not section in config:
                print(section,
                      "\033[93m \tCorrupt or missing\033[0m".rjust(35))
                file_OK = False
                print(
                    "\033[91mCannot test further... Please check config file\n"
                )
                break
            else:
                print(section, "\033[92m \t\tOK\033[0m".rjust(20))
        if not file_OK:
            return file_OK

        print(11 * "_", end="")
        print("Keys", end="")
        print(11 * "_")

        # keys available correctly
        for section, values in self.content.items():
            for value in values:
                if value not in config[section]:
                    print(value.strip(),
                          "\033[93m \tCorrupt or missing\033[0m")
                    file_OK = False
                else:
                    print(value.strip(), "\033[92m \tOK\033[0m".rjust(21))

        return file_OK


# if __name__ == "__main__":
#     run = ConfigGenerator()
#     # run.new_config_file('.')
#     run.config_file_test("config_tmp.ini", "config.ini")
