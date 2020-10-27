<h5 style=color:red align="center">Project is not ready, work in progress</h5>
<h1 align="center"> NewPy </h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

<h3 align="center"> 
PERSONAL AUTOMATION PROGRAM [CLI]
</h3>

<hr>

## OVERVIEW: ##
Open new Python project by building the structure and prepare files automatically. Very lightweight version of cookie-cutter which in this case is build up on using config.ini file. All the settings should be set there and you are ready to go.

## INSTALLATION ##
```code
# clone the repo
$ git clone https://github.com/stefangal/newpy

# change the working directory to Newpy
$ cd newpy

# install the requirements
$ python3 -m pip install -r requirements.txt

$ startnew
```

## GETTING STARTED ##

#### config.ini
Data needed to use newpy is in config.ini file:
```
[PROJECT]
projectname = project
projectpath = /Users/stefangal/Documents/Coding/Python/Projects
licensetype =  mit
;Licensetypes:
;'afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0',
;'cc_by', 'cc_by_nc', 'cc_by_nc_nd', 'cc_by_nc_sa',
;'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 'gpl2', 'gpl3',
;'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib'

[GITHUB]
username = stefangal
githubrepo = True
gitpush = True
gittoken = 8a35fdf7e3cf5a2e3dd5934a732faa776dfd6702
private = True

[TODO]
docsfolder = True
testfolder = True

[PYPI]
author = Stefan Gal
authoremail = xxx@xxx.com
description = xxx
version = 0.0.1
release = False
```

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
In config.ini define the type of LICENSE you'd like to generate. 
You can choose from the following abbrevations:

afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0', 'cc_by', 'cc_by_nc',
'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd', 'cc_by_sa', 'cddl', 'epl', 
'gpl2', 'gpl3', 'isc', 'lgpl', 'mit', 'mpl', 'wtfpl', 'zlib'



## HOW TO HELP ##

Any help is appriciated.

## CONTRIBUTORS ##

Feel free to contribute and register yourself in AUTHORS.md


