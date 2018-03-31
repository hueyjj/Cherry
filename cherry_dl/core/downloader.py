from __future__ import unicode_literals
import urllib.request as request
import os

from PyQt5 import (
    QtCore, 
)
from PyQt5.QtCore import (
    QThread,
    QRunnable,
    QObject,
    pyqtSignal,
)

import youtube_dl

class MetaInformationSignal(QObject):
    metaDownloaded = pyqtSignal(dict)
    unableToRetrieveMeta = pyqtSignal(str)

class MetaInformation(QRunnable):
    ''' Stores meta information of the current youtube link '''

    def __init__(self, url):
        super(MetaInformation, self).__init__()
        self.url = url

        self.signal = MetaInformationSignal()

    def run(self):
        meta = self._downloadInformation()
        if meta:
            self.signal.metaDownloaded.emit(meta)
        else:
            self.signal.unableToRetrieveMeta.emit(self.url) 

    def _downloadInformation(self):
        with youtube_dl.YoutubeDL() as ytdl:
            try:
                meta = ytdl.extract_info(self.url, download=False)
            except youtube_dl.DownloadError as err:
                print(err)
                return None
            except Exception as err:
                print("Something went wrong beyond the program's scope.")
                print(err)
        if meta:
            return {
                "title": meta["title"],
                "description": meta["description"],
                "thumbnail": self._downloadImage(meta["thumbnail"]),
            }
        return None
    
    def _downloadImage(self, url):
        with request.urlopen(url) as f:
            image = f.read()
        return image

class DownloaderSignal(QObject):
    downloadComplete = pyqtSignal()
    unableToRetrieveMeta = pyqtSignal()

class Downloader(QRunnable):
    ''' Downloads videos with respect to user options '''

    def __init__(self, url, saveDir, opts=None):
        super().__init__()
        self.url = url
        self.saveDir = saveDir
        self.opts = opts

    def run(self):
        self._download()
    
    def _download(self):
        # Save last location before changing into save directory
        last = os.getcwd()
        os.chdir(self.saveDir)

        with youtube_dl.YoutubeDL(self.opts) as ytdl:
            ytdl.download([self.url])

        # Return to last location
        os.chdir(last)
