import os
import json


class Config(object):
    homeDir = os.path.expanduser('~')
    appDirName = ".cherry-dl"
    userSaveDir = os.path.join(homeDir, appDirName)

    userConfigPath = os.path.join(userSaveDir, "config.json")
    defaultSavePath = os.path.join(homeDir, "Downloads")

    defaultConfig = {
        "saveDirectory": defaultSavePath,
        "youtubedl": {
            "format": "m4a",
            "ignoreerrors": "True",
            "writethumbnail": "True",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "EmbedThumbnail"
            }]
        }
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

    def setFormat(self, newFormat):
        self.getYoutubedlConfig()["format"] = newFormat

    # TODO Set video, audio, or both
