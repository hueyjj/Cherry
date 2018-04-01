import os
import json

class Config(object):
    homedir = os.path.expanduser('~')
    appdir = ".cherry-dl"
    savedir = os.path.join(homedir, appdir)

    userPath = os.path.join(savedir, "config.json")
    defaultPath = os.path.join(homedir, "Downloads")

    defaultConfig = {
        "saveDirectory": defaultPath,
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
        if os.path.exists(self.userPath) and os.path.isfile(self.userPath):
            self.loadUserConfig()
        else:
            self.loadDefaultConfig()
        
    def getConfig(self):
        return self.config
    
    def getYoutubedlConfig(self):
        return self.config["youtubedl"]

    def loadUserConfig(self):
        with open(self.userPath, 'r') as infile:
            self.config = json.load(infile)
    
    def loadDefaultConfig(self):
        self.config = self.defaultConfig
        self.saveConfig()

    def saveConfig(self):
        with open(self.userPath, 'w') as outfile:
            json.dump(self.config, outfile, indent=True)
    
    def setFormat(self, newFormat):
        self.getYoutubedlConfig()["format"] = newFormat