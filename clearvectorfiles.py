import os
def clearvectorfiles():
    for files in os.walk("vectors"):
        filelist = list(files[2])
        print(filelist)
        for file in filelist:
            if "vectors" in file:
                print(file)
                dir = os.path.join("vectors/", file)
                os.remove(dir)

    return