# base-strcture-for-ML-project
The base structure of machine learning project

### 1. Directory structure 

```bash
ROOT
├── README.md
├── algorithm
│   ├── README.md
│   └── dummy.algo
├── doc-sphinx
│   ├── Makefile
│   ├── README.md
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py
│       ├── configs.rst
│       ├── envs.rst
│       ├── index.rst
│       ├── main.rst
│       └── modules.rst
├── etc
│   └── dummy
├── input
│   └── dummy
├── log
│   └── dummy
├── output
│   └── dummy
├── playground
│   ├── env.py
│   ├── playground.ipynb
│   └── playground.py
├── setup.py
└── src
    ├── configs
    │   ├── __init__.py
    │   ├── config.py
    │   └── config_user.py
    ├── envs
    │   ├── Logger.py
    │   ├── SignalHandler.py
    │   ├── __init__.py
    │   ├── base_env.py
    │   ├── base_pkg.py
    │   ├── base_util.py
    │   └── env.py
    └── main.py
```


### 2. Description
1. `algorithm` directory  
The algorithms are here.  
Despite a lot of searches, I couldn't find a good algorithm(pseudo-code) editor.  
So I created a new file type ***.algo** that can be viewed in Pycharm.  
See the details in `/algorithm/README.md` 

2. `doc-sphinx` directory
