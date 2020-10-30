<h1 align="center"> NewPy </h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

<h3 align="center"> 
PERSONAL NEW PYTHON PROJECT AUTOMATION PROGRAM [CLI]
</h3>

<hr>

## OVERVIEW: ##
- [x] Open new Python project by building the structure and prepare initial files automatically via simple command line command ```startnew```. 
- [ ] Prepare github repository
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

$ startnew
or
$ startnew --p <project_name> --l <license_type>
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

For more information see CONTRIBUTING.md

