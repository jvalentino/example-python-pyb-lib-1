# Example Python Library (Part 1)

The purpose of this project is to be a basic python library built using PyBuilder.

Prerequisites

- Git: https://github.com/jvalentino/setup-git

# Setup

## Python

You need python, which you can get via https://python.land/installing-python

If you are on a Mac, use Homebrew and put it on your path.

```bash
brew install python
echo 'export PATH="/opt/homebrew/opt/python@3.10/libexec/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

You can then verify it was installed:

```bash
$ python -V
Python 3.10.9
```

## PyBuilder

You install it with a single command:

```bash
pip install pybuilder
```

You can then verify it was installed:

```bash
$ pyb --version
pyb 0.13.8
```

## Virtual Environment

These commands are used to setup a virtual python environment specific to this project:

```bash
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install pybuilder
pyb install_dependencies
```

# Environment

Note that anytime you want to build this, you must be in the virtual environment, which means you have to run

```bash
. venv/bin/activate
```

# Dependencies

Now you have to install dependencies:

```bash
(venv) ~/workspaces/personal/example-python-pyb-lib-1 $ pyb install_dependencies   
PyBuilder version 0.13.8
Build started at 2023-01-04 11:49:48
------------------------------------------------------------
[INFO]  Building example-python-pyb-lib-1 version 1.0.dev0
[INFO]  Executing build in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1
[INFO]  Going to execute task install_dependencies
[INFO]  Processing plugin packages 'coverage~=6.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'flake8~=4.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'pypandoc~=1.4' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'setuptools>=38.6.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'twine>=1.15.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'unittest-xml-reporting~=3.0.4' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'wheel>=0.34.0' to be installed with {'upgrade': True}
[INFO]  Creating target 'build' VEnv in '/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/venv/build/cpython-3.10.9.final.0'
[INFO]  Creating target 'test' VEnv in '/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/venv/test/cpython-3.10.9.final.0'
[INFO]  Installing all dependencies
[INFO]  Processing dependency packages 'mockito' to be installed with {}
[INFO]  Processing dependency packages 'requests' to be installed with {}
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: example-python-pyb-lib-1
             Version: 1.0.dev0
      Base directory: /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1
        Environments: 
               Tasks: prepare [2171 ms] install_dependencies [761 ms]
Build finished at 2023-01-04 11:49:51
Build took 3 seconds (3803 ms)
```

# Build

You can then run the entire build using `pyb`.

```bash
(venv) ~/workspaces/personal/example-python-pyb-lib-1 $ pyb

PyBuilder version 0.13.8
Build started at 2023-01-04 10:27:31
------------------------------------------------------------
[INFO]  Building example-python-pyb-lib-1 version 1.0.dev0
[INFO]  Executing build in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1
[INFO]  Going to execute task publish
[INFO]  Processing plugin packages 'coverage~=6.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'flake8~=4.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'pypandoc~=1.4' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'setuptools>=38.6.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'twine>=1.15.0' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'unittest-xml-reporting~=3.0.4' to be installed with {'upgrade': True}
[INFO]  Processing plugin packages 'wheel>=0.34.0' to be installed with {'upgrade': True}
[INFO]  Creating target 'build' VEnv in '/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/venv/build/cpython-3.10.9.final.0'
[INFO]  Creating target 'test' VEnv in '/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/venv/test/cpython-3.10.9.final.0'
[INFO]  Requested coverage for tasks: pybuilder.plugins.python.unittest_plugin:run_unit_tests
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/src/unittest/python
[INFO]  Executed 1 unit tests
[INFO]  All unit tests passed.
[INFO]  Building distribution in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/dist/example-python-pyb-lib-1-1.0.dev0
[INFO]  Copying scripts to /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/dist/example-python-pyb-lib-1-1.0.dev0/scripts
[INFO]  Writing setup.py as /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/dist/example-python-pyb-lib-1-1.0.dev0/setup.py
[INFO]  Collecting coverage information for 'pybuilder.plugins.python.unittest_plugin:run_unit_tests'
[WARN]  ut_coverage_branch_threshold_warn is 0 and branch coverage will not be checked
[WARN]  ut_coverage_branch_partial_threshold_warn is 0 and partial branch coverage will not be checked
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/src/unittest/python
[INFO]  Executed 1 unit tests
[INFO]  All unit tests passed.
[INFO]  Overall pybuilder.plugins.python.unittest_plugin.run_unit_tests coverage is 100%
[INFO]  Overall pybuilder.plugins.python.unittest_plugin.run_unit_tests branch coverage is 100%
[INFO]  Overall pybuilder.plugins.python.unittest_plugin.run_unit_tests partial branch coverage is 100%
[INFO]  Overall example-python-pyb-lib-1 coverage is 100%
[INFO]  Overall example-python-pyb-lib-1 branch coverage is 100%
[INFO]  Overall example-python-pyb-lib-1 partial branch coverage is 100%
[INFO]  Building binary distribution in /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/dist/example-python-pyb-lib-1-1.0.dev0
[INFO]  Running Twine check for generated artifacts
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: example-python-pyb-lib-1
             Version: 1.0.dev0
      Base directory: /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1
        Environments: 
               Tasks: prepare [2656 ms] compile_sources [0 ms] run_unit_tests [147 ms] package [8 ms] run_integration_tests [0 ms] verify [0 ms] coverage [235 ms] publish [661 ms]
Build finished at 2023-01-04 10:27:35
Build took 4 seconds (4536 ms)
(venv) ~/workspaces/personal/example-python-pyb-lib-1 $ 
```

The result will be reports and assets under target:

- dist
  - example-python-pyb-lib-1-1.0.dev0
    - dist
      - example_python_pyb_lib_1-1.0.dev0-py3-none-any.whl
      - example-python-pyb-lib-1-1.0.dev0.tar.gz
- logs
  - venv_build_install_logs
- reports
  - example-python-pyb-lib-1_coverage
  - example-python-pyb-lib-1_coverage.json
  - example-python-pyb-lib-1_coverage.xml

# Manualing Testing It

From the manual-testing directory, run the following script:

```bash
$ ./test.sh

+ virtualenv venv
created virtual environment CPython3.10.9.final.0-64 in 499ms
  creator CPython3Posix(dest=/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/john.valentino/Library/Application Support/virtualenv)
    added seed packages: certifi==2022.12.7, charset_normalizer==2.1.1, example_python_pyb_lib_1==1.0.dev0, idna==3.4, pip==22.3.1, requests==2.28.1, setuptools==65.6.3, urllib3==1.26.13, wheel==0.38.4
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
+ . venv/bin/activate
++ '[' venv/bin/activate = ./test.sh ']'
++ deactivate nondestructive
++ unset -f pydoc
++ '[' -z '' ']'
++ '[' -z '' ']'
++ hash -r
++ '[' -z '' ']'
++ unset VIRTUAL_ENV
++ '[' '!' nondestructive = nondestructive ']'
++ VIRTUAL_ENV=/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv
++ '[' darwin21 = cygwin ']'
++ '[' darwin21 = msys ']'
++ export VIRTUAL_ENV
++ _OLD_VIRTUAL_PATH=/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv/bin:/opt/homebrew/opt/python@3.10/libexec/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
++ PATH=/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv/bin:/Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv/bin:/opt/homebrew/opt/python@3.10/libexec/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
++ export PATH
++ '[' -z '' ']'
++ '[' -z '' ']'
++ _OLD_VIRTUAL_PS1=
++ '[' x '!=' x ']'
+++ basename /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/manual-testing/venv
++ PS1='(venv) '
++ export PS1
++ alias pydoc
++ true
++ hash -r
+ pip install ../target/dist/example-python-pyb-lib-1-1.0.dev0/dist/example-python-pyb-lib-1-1.0.dev0.tar.gz
Processing /Users/john.valentino/workspaces/personal/example-python-pyb-lib-1/target/dist/example-python-pyb-lib-1-1.0.dev0/dist/example-python-pyb-lib-1-1.0.dev0.tar.gz
  Preparing metadata (setup.py) ... done
Requirement already satisfied: requests in ./venv/lib/python3.10/site-packages (from example-python-pyb-lib-1==1.0.dev0) (2.28.1)
Requirement already satisfied: charset-normalizer<3,>=2 in ./venv/lib/python3.10/site-packages (from requests->example-python-pyb-lib-1==1.0.dev0) (2.1.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./venv/lib/python3.10/site-packages (from requests->example-python-pyb-lib-1==1.0.dev0) (1.26.13)
Requirement already satisfied: certifi>=2017.4.17 in ./venv/lib/python3.10/site-packages (from requests->example-python-pyb-lib-1==1.0.dev0) (2022.12.7)
Requirement already satisfied: idna<4,>=2.5 in ./venv/lib/python3.10/site-packages (from requests->example-python-pyb-lib-1==1.0.dev0) (3.4)
Building wheels for collected packages: example-python-pyb-lib-1
  Building wheel for example-python-pyb-lib-1 (setup.py) ... done
  Created wheel for example-python-pyb-lib-1: filename=example_python_pyb_lib_1-1.0.dev0-py3-none-any.whl size=2002 sha256=262778abf239795a951297bf2ba19e72e0b3704b099e209764ed5922b7c5c088
  Stored in directory: /Users/john.valentino/Library/Caches/pip/wheels/09/5a/a1/173eab7e9788ed1bb686160a5539ba7322fdbafc9836318e1e
Successfully built example-python-pyb-lib-1
Installing collected packages: example-python-pyb-lib-1
  Attempting uninstall: example-python-pyb-lib-1
    Found existing installation: example-python-pyb-lib-1 1.0.dev0
    Uninstalling example-python-pyb-lib-1-1.0.dev0:
      Successfully uninstalled example-python-pyb-lib-1-1.0.dev0
Successfully installed example-python-pyb-lib-1-1.0.dev0
+ python hi.py
Hello world of Python
200%    
```

This script executes a python file that includes the library we just built:

hy.py

```python
from helloworld import helloworld
from helloworld import rest
import sys

helloworld(sys.stdout)
rest(sys.stdout)
```

The script just runs the following commands:

```bash
virtualenv venv
. venv/bin/activate
pip install ../target/dist/example-python-pyb-lib-1-1.0.dev0/dist/example-python-pyb-lib-1-1.0.dev0.tar.gz
python hi.py
```



# How did I create this project?

```bash
$ pyb --version
pyb 0.13.8
~/workspaces/personal/example-python-pyb-lib-1 $ pyb --start-project
Project name (default: 'example-python-pyb-lib-1') : 
Source directory (default: 'src/main/python') : 
Docs directory (default: 'docs') : 
Unittest directory (default: 'src/unittest/python') : 
Scripts directory (default: 'src/main/scripts') : 
Use plugin python.flake8 (Y/n)? (default: 'y') : 
Use plugin python.coverage (Y/n)? (default: 'y') : 
Use plugin python.distutils (Y/n)? (default: 'y') : 

Created 'setup.py'.

Created 'pyproject.toml'.
```

