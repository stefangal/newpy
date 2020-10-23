<h1 align="center"> NewPy </h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

<h3 align="center"> 
PERSONAL AUTOMATION PROGRAM [CLI]
</h3>

<hr>
## OVERVIEW: ##
Open new Python project by building the structure and prepare files automatically. Very lightweight version of cookie-cutter which in this case is build up on using config.ini file. All the settings should be set there and you are ready to go.
<h5 style=color:red>Project is not ready, work in progress</h5>

#### TODO:
   - [x] **Folders** structure builder
   - [ ] **Files** 
     - [x] File: **README.md** 
     - [ ] File: **.gitignore**
     - [x] File: **requiremnets.txt**
     - [x] File: **LICENSE**     
   - [ ] New **REPO** on Github
   - [ ] **Git push** on REPO

## INSTALLATION ##
```code
pip install -r requirements.txt
python startnew
```

**Hints**
   -  using [configparser](https://docs.python.org/3/library/configparser.html) module to parse form config.ini
   -  when running 'python startnew' the config.ini should be filled, so there should be a check for minimum required data
  


## GETTING STARTED ##
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

## HOW TO HELP ##

Any help is appriciated.

## CONTRIBUTORS ##

Feel free to contribute and register yourself in AUTHORS.md


