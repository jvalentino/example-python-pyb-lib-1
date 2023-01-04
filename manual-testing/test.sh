#!/bin/sh
set -x
virtualenv venv
. venv/bin/activate
pip install ../target/dist/example-python-pyb-lib-1-1.0.dev0/dist/example-python-pyb-lib-1-1.0.dev0.tar.gz
python hi.py