import os
def clearvectorfiles():

    for files in os.walk("vectors"):
        filelist = list(files[2])
        for file in filelist:
            if "vectors" in file:
                dir = os.path.join("vectors/", file)
                os.remove(dir)

    for files in os.walk("plantvectors"):
        filelist = list(files[2])
        for file in filelist:
            if "vectors" in file:
                dir = os.path.join("plantvectors/", file)
                os.remove(dir)

    for files in os.walk("actors"):
        filelist = list(files[2])
        for file in filelist:
            if "characteristics" in file:
                dir = os.path.join("actors/", file)
                os.remove(dir)

    for files in os.walk("log"):
        filelist = list(files[2])
        for file in filelist:
            if "log" in file or "Stats" in file or 'stats' in file or "Parameters" or "params" in file:
                dir = os.path.join("log/", file)
                os.remove(dir)

    return