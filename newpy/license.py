# license.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import subprocess as sp


class NewLicense:
    """
    To get the required LICENSE file.
    Credit to Jeremy Carbaugh for the 'lice' the License file genarator: https://github.com/licenses/lice
    """
    def download(self, dst, lictype):
        """
        Generating LICENSE file. Some data are gathered from git config.

        Choose license type from: 
         'afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0', 'cc_by', 'cc_by_nc', 
         'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 
         'gpl2', 'gpl3', 'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib'
        """

        sp.Popen(f"lice {lictype} -f {dst}/LICENSE", shell=True).wait()


if __name__ == "__main__":
    license = NewLicense()
    license.download(
        "/Users/stefangal/Documents/Coding/Python/Projects/Newpy/DIR", 'mit')
