# license.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import shutil


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

        FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/templates")

        if os.path.exists(FOLDER):
            for template_file in os.listdir(FOLDER):
                if lictype in template_file:
                    shutil.copy(os.path.join(FOLDER, template_file), dst)
                    os.rename(os.path.join(dst, template_file), "LICENSE")


if __name__ == "__main__":
    license = NewLicense()

    license.download(
        "/Users/stefangal/Documents/Coding/Python/Projects/PyNew/DIR", 'agpl3')
