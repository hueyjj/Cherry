from __future__ import unicode_literals
import urllib.request as request

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

class MetaInformation(QRunnable):
    ''' Stores meta information of the current youtube link '''

    def __init__(self, url):
        super(MetaInformation, self).__init__()
        self.url = url

        self.signal = MetaInformationSignal()

    def _downloadImage(self, url):
        with request.urlopen(url) as f:
            image = f.read()
        return image

    def _downloadInformation(self):
        if self.url:
            with youtube_dl.YoutubeDL() as ytdl:
                meta = ytdl.extract_info(self.url, download=False)
            if meta:
                return {
                    "title": meta["title"],
                    "description": meta["description"],
                    "thumbnail": meta["thumbnail"],
                }
        return None
    
    def run(self):
        meta = self._downloadInformation()
        if meta:
            self.signal.metaDownloaded.emit(meta)
        else:
            # FIXME Tell whoever connected that there is not information some other way
            self.signal.metaDownloaded.emit({}) 