#!/usr/bin/env sh
#TODO Include python optimization https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-with-python-optimizations

pyinstaller cherry_dl/__main__.py \
    -n cherry-dl \
    --noconfirm \
    --noconsole