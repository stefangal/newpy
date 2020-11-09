# repo.py
# Copyright (C) 2020 Stefan Gal (stefan.mail.sk@gmail.com) and contributors
#
# This module is part of NewPy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html
# pylint: disable=no-name-in-module

from github import Github
import logging

logging.basicConfig(level=logging.INFO)


class OpenRepo:
    """
    Create new Github repository.
    """
    def create_new_repo(self, repo_name, token):
        """Create new repository.
        
        Parameters
        ----------
        repo_name : str
            Name of the new repository
        token : str
            Github access token
        """
        g = Github(token)
        user = g.get_user()
        user.create_repo(name=repo_name, private=True)
        print("INFO: Private repository on github is created.")


if __name__ == "__main__":
    repo = OpenRepo()