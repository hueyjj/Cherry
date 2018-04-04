# Cherry
A youtube-dl gui application.

![0.1.0 home](https://raw.githubusercontent.com/hueyjj/cherry-dl/master/screenshots/home.PNG)

![0.1.0 config](https://raw.githubusercontent.com/hueyjj/cherry-dl/master/screenshots/config.PNG)

# Release
A portable and installer version are available.
[The current release can be downloaded here](https://github.com/hueyjj/cherry-dl/releases/tag/0.1)

# Virtualenv (developing)
Create virtualenv
```
virtualenv ~/.virtualenvs/cherry-dl
```

Activate virtualenv (in a shell, then cd to project directory)
```
source ~/.virtualenvs/cherry-dl/Scripts/activate
```

Install requirements
```
pip install -r requirements.txt
```

Check virtualenv (path to virtualenv location)
```
pip -V
```

Deactivate virtualenv (when in virtualenv)
```
deactivate
```

# Running (developing)
```
cd cherry-dl
python cherry_dl
```

# Building (workflow)
1. Make UI with QT Creator

    a. Generate python code of UI
    ```
    ./build_ui.sh
    ```
2. Build resources 

    a. Generate python code for resources
    ```
    ./build_resources.sh
    ```
3. Use Pyinstaller to convert Python application to windows executable
    ```
    ./build_cherry-dl.sh
    ```
    The resulting binary and related program files can be found in path/to/cherry-dl/dist/cherry-dl/, which can be distributed as is.

    At this point, the program can be run by running the cherry-dl.exe in path/to/cherry-dl/dist/cherry-dl/
 

4. (Extra) Use Inno Setup Compiler to create installer for the exe and its related files

    A script (InnoSetupScript_cherry-dl.iss) is provided as an example of how it should it look like (note: my script will not work on other system since it uses absolute path). The ideal method when building the installer program is to create it using the setup wizard provided by Inno Setup Compiler.
