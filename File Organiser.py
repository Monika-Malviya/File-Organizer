import os
import pathlib
import shutil

fileFormate = {
    "web" : [".html5" , ".html", ".htm", ".xhtml"],
    "picture" : [".jpeg", ".jpg", ".tiff", ".gif",
                  ".bmp", ".png "],
    "Text Files" : [".txt", ".csv"],
    "Document Files": [".docx", ".pdf", ".odt"],
    "Spreadsheet Files" : [".xlsx", ".ods"],
    "Presentation Files": [".pptx", ".odp"],
    "Image Files": [".jpg", ".png", ".gif", ".bmp", ".svg"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac"],
    "Video Files": [".mp4", ".avi", ".mkv", ".mov"],
    "Compressed Files": [".zip", ".rar", ".tar.gz"],
    "Executable Files": [".exe", ".bat", ".sh"],
    "Database Files": [".db", ".sql", ".mdb"],              
}

fileTypes = list(fileFormate.keys())
fileFormates =list(fileFormate.values())

print(fileFormates)
print(fileTypes)

for file in os.scandir():
    fileName = pathlib.Path(file)
    fileFormateType = fileName.suffix.lower()

    src = str(fileName)
    dest = "Other"
    if fileFormateType == " " :
        print(f" {src} has not file formate")
    else:
        for formates in fileFormates:
            if fileFormateType in formates:
                folder = fileTypes[fileFormates.index(formates)]
                print(folder)
                if os.path.isdir(folder) == False:
                   os.mkdir(folder)
                   dest = folder    
        else:
            if os.path.isdir("Other") == False:
                os.mkdir("Other")

    print(src, " moved to ", dest, " ! ")
    shutil.move(src , dest)

print("File Organizer Started")
input("\n Press enter to Exit")                