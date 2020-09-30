import os
import logging
import configparser
import fileconf as cg


MAJOR = 0
MINOR = 91
MICRO = 0
__version__ = f"{MAJOR}.{MINOR}.{MICRO}"

logger = logging.getLogger("new_project")
logger.setLevel(logging.DEBUG)


class Run:

    CONFIG_FILE = "config.ini"

    def __init__(self):
        # Logger
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
        )
        self.logger = logging.getLogger("new_project")
        self.log = logging.StreamHandler()
        self.log.setFormatter(formatter)
        self.logger.addHandler(self.log)
        # Configparser
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)
        # Methods to run
        self.build_folder_structure()

    def project_details(self):
        print(self.config["GITHUB"]["UserName"])

    def github(self):
        pass

    def pypi(self):

        pass

    def config_file_test(self):
        if self.CONFIG_FILE != "config.ini":
            return False

    def build_folder_structure(self):
        check = cg.ConfigGenerator()
        if check.config_file_test("config.ini"):
            print("all OK ")
        PATH = self.config["PROJECT"]["ProjectPath"]
        FILE = self.config["PROJECT"]["ProjectName"]
        filepath = os.path.join(PATH, FILE)

        if PATH and FILE and not os.path.exists(filepath):
            os.mkdir(path=os.path.join(PATH, FILE))
            os.mkdir(path=os.path.join(PATH, "tests"))
            os.mkdir(path=os.path.join(PATH, "docs"))
            self.logger.info("Folder structure ready")

        if os.path.exists(filepath):
            with open(os.path.join(filepath, "main.py"), "w") as file:
                pass
            with open(os.path.join(PATH, ".gitignore"), "w") as file:
                pass
            with open(os.path.join(PATH, ".LICENSE"), "w") as file:
                pass
            with open(os.path.join(PATH, "requirements.txt"), "w") as file:
                pass
            with open(os.path.join(PATH, "setup.py"), "w") as file:
                pass
            with open(os.path.join(PATH, "README.MD"), "w") as file:
                pass
        return True

    def build_file_structure(self):
        pass


if __name__ == "__main__":
    run = Run()

