# license.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of PyNew and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import requests
import lice


class LicenseGenerator:
    def connect_api(self):
        url = "https://developer.github.com/v3/licenses"
        con = requests.get(url)
        print(con.content)

    def download_license(self, path, lictype):
        os.system(f"lice {lictype} -f {path}/LICENSE")

    def license_listing(self, file):
        with open(file, "r") as licfile:
            lic_list = licfile.readlines()
            ls = [x.rstrip("\n").replace("\\", "\\t\\t\\t") for x in lic_list]
            print(
                "\nAVAILABLE LICENSES [use abbrevation for the config.ini file"
            )
            print(59 * "#")
            for row in ls:
                lic, abrev = row.split(";")
                print("" + lic + "\033[94m" + "\r\t\t\t\t\t\t\t" + abrev +
                      "\033[0m")


if __name__ == "__main__":
    # license = LicenseGenerator()
    # license.license_listing("pynew/licenses.db")
    # license.download_license(
        # "/Users/stefangal/Documents/Coding/Python/Projects/PyNew/DIR", 'mit')
