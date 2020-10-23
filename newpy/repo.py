# repo.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html
# pylint: disable=no-name-in-module

import requests
from github import Github


class OpenRepo:
    def list_repos(self, token):
        g = Github(token)
        for repo in g.get_user().get_repos():
            print(repo.name)

    def create_repo(self, token, private):
        g = Github(token)
        user = g.get_user()
        user.create_repo('test repo', private)


if __name__ == "__main__":
    opre = OpenRepo()
