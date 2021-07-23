#!/usr/bin/env bash

python3 setup.py clean --all
python3 -m pip uninstall elsockets --yes
python3 -m pip install .
