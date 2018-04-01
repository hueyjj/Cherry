from downloader import MetaInformation, Downloader

url = r"https://www.youtube.com/watch?v=eHir_vB1RUI"
#m = MetaInformation()

#print(type(m.title))
##print(m.title)
##print(m.description)
#print(m.thumbnail)

defaultYoutubeOpts = {
    "format": "m4a",
    "ignoreerrors": True,
    "writethumbnail": True,
    "outtmpl": "%(title)s.%(ext)s",
    "postprocessors": [{
        "key": "EmbedThumbnail",
    }],
}
dl = Downloader(url, r"C:/users/jj/downloads", defaultYoutubeOpts)
dl.run()




