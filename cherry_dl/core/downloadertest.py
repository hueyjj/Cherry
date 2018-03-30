from downloader import MetaInformation

url = r"https://www.youtube.com/watch?v=eHir_vB1RUI"
m = MetaInformation()
m.load(url)

print(type(m.title))
#print(m.title)
#print(m.description)
print(m.thumbnail)

