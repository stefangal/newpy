# cli-builder.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
# pylint: disable=no-name-in-module

import os
import logging

try:
    from newpy.license import NewLicense
    from newpy.setup_manager import PrepareSetup
    from newpy.repo import OpenRepo
except Exception:
    from .license import NewLicense
    from .setup_manager import PrepareSetup
    from .newpy.repo import OpenRepo

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')
logging.getLogger(__name__)


class Builder:
    license_set = ('afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0', 'cc_by',
                   'cc_by_nc', 'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd',
                   'cc_by_sa', 'cddl', 'epl', 'gpl2', 'gpl3', 'isc', 'lgpl',
                   'mit', 'mpl', 'wtfpl', 'zlib')

    def __init__(self, project_name, lic_type, token=None):
        self.token = token
        self.lic_type = lic_type
        self.curr_working_dir = os.getcwd()
        self.project_name = project_name
        self.project_path = os.path.join(self.curr_working_dir,
                                         self.project_name)

        self._folder_structure()

        if self.token:
            self._create_repo(token)

    def _folder_structure(self):
        """Building folders: PROJECT, test and docs folders"""

        # if os.path.exists(self.project_path):
        print("\n")
        os.mkdir(path=self.project_path)
        self._build_init_file(self.project_path),
        self._build_test_folder(), self._build_docs_folder(),
        self._build_readme_md(), self.build_setup_py(),
        self._build_requirements_txt(), self._build_gitignore()

    def _build_init_file(self, path):
        try:
            with open(os.path.join(path, "__init__.py"), "w"):
                return
        except Exception as e:
            logging.error('Issue creating __init__.py file ', e)

    def _build_test_folder(self):
        test_path = os.path.join(self.project_path, "tests")
        try:
            os.mkdir(path=test_path)
            print("Test path: ", test_path)
            self._build_init_file(test_path)
            return
        except Exception as e:
            logging.error('Issue with creating tests folder ', e)

    def _build_docs_folder(self):
        docs_path = os.path.join(self.project_path, "docs")
        try:
            os.mkdir(path=docs_path)
            print("Docs path: ", docs_path)
            return
        except Exception as e:
            logging.error('Issue with creating docs folder ', e)

    def _build_readme_md(self):
        try:
            with open(os.path.join(self.project_path, "README.md"),
                      "w") as file:
                line = f'<h1 align="center"> {self.project_name} </h1>'
                file.write(line)
                return
        except Exception as excp:
            logging.error('Issue with creating README.md file ', excp)

    def build_license(self, lic_type):
        lic = NewLicense()
        try:
            if lic_type in self.license_set:
                lic.download(self.project_path, lic_type)
                print("INFO: LICENSE type used: ", "mit")
            else:
                lic.download(self.project_path, 'mit')
                print("LICENSE type incorrect. Using as default: ", lic_type)
            return
        except Exception as e:
            logging.error('Issue with creating LICENSE file ', e)

    def build_setup_py(self):
        ps = PrepareSetup()
        ps.fill_setup_template(self.project_path)

    def _build_requirements_txt(self):
        req_path = os.path.join(self.project_path, "requirements.txt")
        try:
            with open(req_path, "w"):
                return
        except Exception as e:
            logging.error('Issue with creating requirements.txt file ', e)

    def _build_gitignore(self):
        gitign_path = os.path.join(self.project_path, ".gitignore")
        gitign_templ_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "templ_gitignore.py")
        try:
            with open(gitign_templ_path, "r") as gitignore_template:
                with open(gitign_path, "w") as gitignore_new:
                    for row in gitignore_template.readlines():
                        gitignore_new.writelines(row)
            return

        except Exception as e:
            logging.error('Issue with creating .gitignore file ', e)

    def _create_repo(self, token):
        repo = OpenRepo()
        repo.create_new_repo(self.project_name, token)


if __name__ == "__main__":
    pass