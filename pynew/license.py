# license.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
from os import CLD_EXITED, linesep
import shutil
import lice
import lice.core as lc
import sys

# from license.manager import LicenseManager

class NewLicense:
    def download_license(self, path, lictype):
        """
        Choose from: 
         'afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0', 'cc_by', 'cc_by_nc', 
         'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 
         'gpl2', 'gpl3', 'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib'
        """
        os.system(f"lice {lictype} -f {path}/LICENSE")

    def download(self, dst, lictype):
        """
        Generate from templace and download to the path.
        """

        FOLDER = os.path.join(
            os.path.dirname(os.path.abspath(__file__)) + "/templates")
        print(FOLDER)
        if os.path.exists(FOLDER):
            for template_file in os.listdir(FOLDER):
                if lictype in template_file:
                    shutil.copy(os.path.join(FOLDER, template_file), dst)
                    os.rename(os.path.join(dst, template_file),
                              os.path.join(dst, "LICENSE"))

    def save(self, dst, lic_type):
        """
        Generate from templace and download to the path.
        """

        # lc.DEFAULT_LICENSE = lic_type

        # if os.path.exists(dst):
        #     with open(os.path.join(dst, "LICENSE"), "w") as license_file:
        #         print(lc.main().__str__())
        #         for line in lc.main():
        #             license_file.writelines(str(line))

        if os.path.exists(dst):
            manager = LicenseManager(dst)
            manager.get('mit')

if __name__ == "__main__":
    lic = NewLicense()

    # license.download(
    #     "/Users/stefangal/Documents/Coding/Python/Projects/PyNew/DIR", 'agpl3')
    lic.save("/Users/stefangal/Documents/Coding/Python/Projects/PyNew/DIR",
                 'mit')
