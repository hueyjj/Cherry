#!/usr/bin/env sh
#TODO Include python optimization https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-with-python-optimizations

echo "Converting .ui files to .py files"
./build_ui.sh
echo "Converting .qrc files to .py files"
./build_resources.sh

pyinstaller cherry_dl/__main__.py \
    -n cherry-dl \
    --noconfirm \
    --noconsole