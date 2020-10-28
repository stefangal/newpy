<h5 style=color:red align="center">Project is not ready, work in progress</h5>
<h1 align="center"> NewPy </h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

<h3 align="center"> 
PERSONAL NEW PYTHON PROJECT AUTOMATION PROGRAM [CLI]
</h3>

<hr>

## OVERVIEW: ##
Open new Python project by building the structure and prepare initial files automatically via CLI. Very lightweight version of cookie-cutter. 
## DEVELOPMENT ##

```
# clone the repo
$ git clone https://github.com/stefangal/newpy

# change the working directory to Newpy
$ cd newpy

# install the requirements
$ python3 -m pip install -r requirements.txt

# install with pip in local mode
$ pip install -e .

# now you can run it
$ startnew
```



## INSTALLATION ##

It supposed to work the way, that in terminal where you run ```startnew``` there in the current directory it will generate the project.

```code
$ pip install newpy

$ startnew
```
You will be asked several questions as well as you will be able to choose some default settings.

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

## HOW TO HELP ##

Any help is appriciated.

## CONTRIBUTORS ##

Feel free to contribute and register yourself in AUTHORS.md


