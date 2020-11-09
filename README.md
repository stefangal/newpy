<h1 align="center"> NewPy </h1>

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)


<h3 align="center"> 
PERSONAL NEW PYTHON PROJECT AUTOMATION PROGRAM [CLI]
</h3>

<hr>

## OVERVIEW: ##
- [x] Open new Python project by building the structure and prepare initial files automatically via simple command line command ```startnew```. 
- [x] Prepare github repository
## DEVELOPMENT ##

```
# clone the repo
$ git clone https://github.com/stefangal/newpy

# change the working directory to newpy
$ cd newpy

# install the requirements
$ python install .

# now you can run it
$ startnew
```


## INSTALLATION ##

Use ```startnew```  to generate the folders and files in current working directory.

```code
$ pip install startnew

# for arguments help run:
$ startnew --help

# run:
$ startnew
or
$ startnew --p <project_name> --l <license_type> --g <Github_token>

# you'll need a personal access token to open repository on Github
# you can get one from https://github.com/settings/tokens.
```
You will be asked several questions as well as you will be able to choose some default settings.
Regarding Github repository read the **GITHUB section**.

## GETTING STARTED ##


#### Folder structure
[MORE ABOUT THE STRUCTURE](https://docs.python-guide.org/writing/structure/)

```bash
└── app
    ├── tests
    │   └── __init__.py
    ├── docs
    │    
    ├── app
    │   └── __init__.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── setup.py
```
This is the app structure given all the actually available features.
   
#### LICENSE

You can choose from the following abbrevations:
```table
afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0', 'cc_by', 'cc_by_nc',
'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 
'gpl2', 'gpl3', 'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib'
```

### GITHUB

In order to open a new repository for the project via command line, first you will need to
get/create the Github access token. 

[Instructions](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token) how to get access token.

## HOW TO HELP ##

Any help is appriciated.

## CONTRIBUTORS ##

Feel free to contribute and register yourself in AUTHORS.md

For more information see CONTRIBUTING.md

