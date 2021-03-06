import os

def backfill_vectors():
    outputparams = {}
    dead = [99999, 99999, 99999]

    with open("Outputparams.txt") as f:
        for line in f:
            name, value = line.split("=")
            name = name.rstrip(" ")
            outputparams[name] = value.rstrip('\n')

    duration = int(outputparams["Duration"])
    predatorcount = int(outputparams["totalpreds"])
    preycount = int(outputparams["totalprey"])
    plantcount = int(outputparams["totalplants"])
    dir = "vectors"
    x = 0
    while x < plantcount+preycount+predatorcount:
        if x < plantcount:
            dir = 'plantvectors'
        else:
            dir = 'vectors' \
                      ''
        for files in os.walk(dir):
            filelist = list(files[2])
            for file in filelist:
                if "vectors" in file:
                    with open(f"{dir}//{file}", "r") as f:
                        x += 1
                        positions = []
                        vectors = []
                        t = 0
                        birth = 0
                        line = f.read().splitlines(True)
                        birth = int(line[0])
                        del line[0]
                        for k in line:
                            k = k.rstrip("\n")
                            positions = k.split(',')
                            for a in range(0, 3):
                                positions[a] = float(positions[a])

                            vectors.append(positions)


                    with open(f"{dir}//{file}", "w") as f:
                        for i in vectors:

                            while t < birth:
                                vectors.insert(0, dead)
                                t += 1
                            while len(vectors) < duration:
                                vectors.append(dead)

                        for i in vectors:
                            for e in range(3):
                                f.write(str(i[e]))
                                if e != 2:
                                    f.write(str(","))
                            f.write("\n")

if __name__ == '__main__':
    backfill_vectors()


