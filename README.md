# Cherry
A youtube-dl gui application.

# Virtualenv
Create virtualenv
```
virtualenv ~/.virtualenvs/cherry-dl
```

Install requirements
```
pip install -r requirements.txt
```

Activate virtualenv (in a shell, then cd to project directory)
```
source ~/.virtualenvs/cherry-dl/Scripts/activate
```

Check virtualenv (path to virtualenv location)
```
pip -V
```

Deactivate virtualenv (when in virtualenv)
```
deactivate
```

# Building (workflow)
1. Make UI with QT Creator

    a. Generate python code of UI
    ```
    ./build_ui.sh
    ```
2. Use Pyinstaller to convert python to windows executable
    ```
    ./build_cherry-dl.sh
    ```
3. Use Inno setup to create installer for executable

# Running
```
cd cherry-dl
python cherry_dl
```