# main.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import click
from newpy.cli_builder import Builder


@click.command()
@click.option('--p',
              default='project',
              prompt='The project name: ',
              help='Directory & project name.')
@click.option('--l',
              default='mit',
              prompt='The license type: ',
              help="License type")
@click.option('--g',
              help="Github access token to open private github repository")
def startnew(p, l, g):
    build = Builder(p, l, g)
    build.build_license(l)


# if __name__ == "__main__":
#     startnew()
