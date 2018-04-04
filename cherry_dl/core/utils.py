import os
import sys
import json

# Modified version of https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
        print("sys._MEIPASS: " + basePath)
    except Exception:
        print("No sys._MEIPASS found for %s" % relativePath)
        basePath = os.path.dirname(__file__)

    return os.path.join(basePath, relativePath)

class Config(object):
    homeDir = os.path.expanduser('~')
    appDirName = ".cherry-dl"
    userSaveDir = os.path.join(homeDir, appDirName)

    userConfigPath = os.path.join(userSaveDir, "config.json")
    defaultSavePath = os.path.join(homeDir, "Downloads")

    # FIXME Embedding thumbnail requires ffmpeg and atomicparsely. Include as dependencies in project later?
    defaultConfig = {
        "saveDirectory": defaultSavePath,
        "format": "m4a",
        "video": 'best',
        "youtubedl": {
            "format": "best[ext=m4a]",
            "ignoreerrors": "True",
            "writethumbnail": "True",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "EmbedThumbnail"
            }]
        }
    }
    userYoutubeOpts = {
    }

    def __init__(self):
        # Check if user configuration exists
        if os.path.exists(self.userConfigPath) and os.path.isfile(self.userConfigPath):
            self.loadUserConfig()
        else:
            self.loadDefaultConfig()

    def loadUserConfig(self):
        with open(self.userConfigPath, 'r') as infile:
            self.config = json.load(infile)

    def loadDefaultConfig(self):
        if not os.path.exists(self.userSaveDir):
            os.makedirs(self.userSaveDir)

        self.config = self.defaultConfig
        self.saveConfig()

    def resetConfig(self):
        self.loadDefaultConfig()

    def saveConfig(self):
        with open(self.userConfigPath, 'w') as outfile:
            json.dump(self.config, outfile, indent=True)

    def getConfig(self):
        return self.config

    def getYoutubedlConfig(self):
        return self.config["youtubedl"]

    def setSaveDir(self, newDir):
        self.config["saveDirectory"] = newDir
    
    def getFormat(self):
        return self.getYoutubedlConfig()["format"]

    def setFormat(self, newFormat):
        c = self.getConfig()
        c["format"] = newFormat

        yt = self.getYoutubedlConfig()
        yt["format"] = self.createFormat(c["video"], c["format"])
    
    def setVideo(self, newVideo):
        c = self.getConfig()
        c["video"] = newVideo

        yt = self.getYoutubedlConfig()
        yt["format"] = self.createFormat(c["video"], c["format"])

    def createFormat(self, videoOpt, formatOpt):
        return "%s[ext=%s]" % (videoOpt, formatOpt)