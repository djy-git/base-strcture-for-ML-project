# base-structure-for-ML-project
The base structure of machine learning project

# 1 Directory structure 

```bash
ROOT
├── README.md
│
├── algorithm
│   ├── README.md
│   └── dummy.algo
│
├── doc-sphinx
│   └── README.md
│
├── etc
│   └── dummy
│
├── input
│   └── dummy
│
├── log
│   └── dummy.log
│
├── output
│   └── dummy
│
├── playground
│   ├── env.py
│   ├── playground.ipynb
│   └── playground.py
│
├── setup.py
│
└── src
    ├── configs
    │   ├── __init__.py
    │   ├── config.py
    │   └── config_user.py
    ├── envs
    │   ├── __init__.py
    │   ├── SignalHandler.py
    │   ├── Logger.py
    │   ├── base_env.py
    │   ├── env.py
    │   └── util.py
    └── main.py
```


# 2 Description
## 2.1 `/algorithm`
The algorithms are here.  
Despite a lot of searches, I couldn't find a good algorithm(pseudo-code) editor.  
So I created a new file type ***.algo** that can be viewed in Pycharm.  
See the details in `/algorithm/README.md` 

## 2.2 `/doc-sphinx` 
An automatic documentation is assisted by [SPHINX](https://www.sphinx-doc.org/en/master/)  
See the details in `/doc-sphinx/README.md`

## 2.3 `/etc` 
You can put anything in this directory.  
e.g. backup files

## 2.4 `/input` 
This directory is for input data.  
Mainly, the cached DB data are in here.

## 2.5 `/log` 
Logs generated by `Logger` are stored in here.

## 2.6 `/output` 
Output files from the program are stored in here.

## 2.7 `/playground` 
Example codes can be executed in here.

## 2.8 `/setup.py`
This controls the access to the source codes in `src` directory and has information of the project.

## 2.9 `/src` 
This directory has the source codes of the project.

### 2.9.1 `/src/configs` 
The modules in this directory(package) handles the configuration variables commonly used in the project.  
See the details in each module's head comment.

### 2.9.2 `/src/envs` 
The modules in this package constructs the environment commonly used in the project.  
See the details in each module's head comment.

### 2.9.3 `/src/main.py`
This module is invoked in `setup.py`.  
The action in `main.py` is controlled by the command received from `setup.py`.

### 2.9.4 `/src/Logger.py`
This module controls the logging.  


# 3 Environment dependency
```
config_user.py → config.py        → env.py
                 base_env.py      → env.py
                 SignalHandler.py → env.py → util.py
```

# 4 How to use `Logger`
Just import `Logger.py`. Then, `print()` is logged in terminal and log file in `/log` both.
