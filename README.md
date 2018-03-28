# Cherry
A youtube-dl gui application.

# Developing
1. Make UI with QT Creator

    a. Generate python code of UI

        pyuic5 -o cherryui.py designer/CherryDesigner/mainwindow.ui

2. Use Pyinstaller to convert python to windows executable
3. Use Inno setup to create installer for executable