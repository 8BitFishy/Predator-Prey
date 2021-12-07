import os
def clearvectorfiles():
    clear_list = [["animation_data", ["vectors", "params"]], ["vectors", ["vector"]], ["plantactors", ["actor"]], ["plantvectors", ["vectors"]], ["actors", ["actor"]], ["log", ["log", "stats", "Stats", "params", "Parameters"]]]
    for i in range(len(clear_list)):
        for files in os.walk(clear_list[i][0]):
            filelist = list(files[2])
            for file in filelist:
                for j in range(len(clear_list[i][1])):
                    if clear_list[i][1][j] in file:
                        dir = os.path.join(f"{clear_list[i][0]}/", file)
                        os.remove(dir)

    '''
    for files in os.walk("animation_data"):
        filelist = list(files[2])
        for file in filelist:
            if "vectors" in file:
                dir = os.path.join("vectors/", file)
                os.remove(dir)
                
                
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
    '''
    return