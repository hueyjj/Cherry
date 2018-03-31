#!/usr/bin/env sh

# Generate main window
pyuic5.exe -o cherry_dl/ui/main_ui.py designer/CherryDesigner/mainwindow.ui
# Generate home widget
pyuic5.exe -o cherry_dl/ui/home_ui.py designer/CherryDesigner/home.ui
# Generate progress widget
pyuic5.exe -o cherry_dl/ui/progress_ui.py designer/CherryDesigner/progress.ui
# Generate home widget
pyuic5.exe -o cherry_dl/ui/history_ui.py designer/CherryDesigner/history.ui
# Generate configuration widget
pyuic5.exe -o cherry_dl/ui/config_ui.py designer/CherryDesigner/configuration.ui