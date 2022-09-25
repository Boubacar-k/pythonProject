import zipfile
from zipfile import ZipFile

with ZipFile("C:/Users/PC/Desktop/ODC.zip") as f:
    with f.open("Test.txt") as file:
        print(file.read())