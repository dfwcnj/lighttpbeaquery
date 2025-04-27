#!/bin/sh

python3 -m venv pyenv
.  pyenv/bin/activate
pip install --upgrade pip
pip3 install beaquery
pip3 install plotly

