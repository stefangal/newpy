# builder.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
# pylint: disable=no-name-in-module
import os
from license import NewLicense
from setup_manger import PrepareSetup
from configparser import ConfigParser  # debugging
from config_bc import ConfigRead

class Builder:
    def __init__(self, projectpath, _conf):
        self._config = _conf
        self.PROJECT_PATH = projectpath
        self.PATH = "/".join(projectpath.split("/")[:-1])
        self.FILE = "".join(projectpath.split("/")[-1])
        print(self.PATH)
        print(self.FILE)
        print(self.PROJECT_PATH)

    def folder_structure(self):
        """Building folders: PROJECT, test and docs folders"""

        if self.PATH and self.FILE and not os.path.exists(self.PROJECT_PATH):
            print("Structure building starts")
            os.mkdir(path=self.PROJECT_PATH)

            self.build_docs_folder()
            self.build_test_folder()
            self.build_license()
            self.build_setup_py()
            self.build_requirements_txt()
            self.build_readme_md()
            self.build_gitignore()
            

    def build_test_folder(self):
        if self._config["TODO"]["testfolder"] == "True":
            os.mkdir(path=os.path.join(self.PROJECT_PATH, "tests"))

    def build_docs_folder(self):
        if self._config["TODO"]["docfolder"] == "True":
            os.mkdir(path=os.path.join(self.PROJECT_PATH, "docs"))

    def build_license(self):
        license_type = self._config['PROJECT']['licensetype']
        print(license_type)
        license_set = ('afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0',
                       'cc_by', 'cc_by_nc', 'cc_by_nc_nd', 'cc_by_nc_sa',
                       'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 'gpl2', 'gpl3',
                       'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib')
        if license_type in license_set:
            lic = NewLicense()
            lic.download(self.PROJECT_PATH, license_type)

    def build_setup_py(self):
        ps = PrepareSetup(self._config)
        ps.fill_setup_template(self.PROJECT_PATH)

    def build_readme_md(self):
        with open(os.path.join(self.PROJECT_PATH, "README.md"), "w") as file:
            pass

    def build_requirements_txt(self):
        with open(os.path.join(self.PROJECT_PATH, "requirements.txt"), "w") as file:
            pass

    def build_gitignore(self):
        with open(os.path.join(self.PROJECT_PATH, ".gitignore"), "w") as file:
            pass


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config/config.ini")
    builder = Builder(
        "/Users/stefangal/Documents/Coding/Python/Projects/TEST1",
        config)
    builder.folder_structure()