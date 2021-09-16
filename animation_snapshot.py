import os

def snapshot_range():
    start = int(input("Enter start frame: "))
    end = int(input("Enter end frame: "))
    if end == -1:
        outputparams = {}
        with open("Outputparams.txt") as f:
            for line in f:
                name, value = line.split("=")
                name = name.rstrip(" ")
                outputparams[name] = value.rstrip('\n')

        end = int(outputparams["Duration"]) + 1
    print(f"Generating files for animation from {start} to {end}")
    frames = [start, end]
    return frames


def generate_animation_files():
    frames = snapshot_range()
    newpath = 'animation_data'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for files in os.walk(newpath):
        filelist = list(files[2])
        for file in filelist:
            if "vectors" in file:
                dir = os.path.join(f"{newpath}/", file)
                os.remove(dir)

    plants = predators = prey = 0
    start = frames[0]
    end = frames[1]
    for j in range(2):
        if j == 0:
            dir = "vectors"
        else:
            dir = "plantvectors"

        for files in os.walk(dir):

            filelist = list(files[2])

            for file in filelist:
                if "vectors" in file:
                    with open(f"{dir}//{file}", "r") as f:
                        filename = file.split(" ")
                        actor_type = filename[0]
                        actor_number = filename[1]
                        line = f.read().splitlines(True)
                        birth = int(line[0])
                        death = int(line[1])


                        if birth < end and (death > start or death == -1):

                            if actor_type == 'predator':
                                predators += 1
                            elif actor_type == 'prey':
                                prey += 1
                            else:
                                plants += 1

                            print(f"{actor_type} {actor_number}, born {birth}, died {death} is alive in this period")
                            with open(f"{newpath}//{file}", "w") as g:
                                for i in range(len(line)):
                                    if i == 0 or i == 1:
                                        continue
                                    elif i < start or i > end:
                                        continue
                                    else:
                                        line[i] = line[i].rstrip("\n")
                                        positions = line[i].split(',')
                                        for e in range(3):
                                            g.write(str(positions[e]))
                                            if e != 2:
                                                g.write(str(","))
                                        g.write("\n")

                        else:
                            print(f"{actor_type} {actor_number}, born {birth}, died {death} is not alive in this period")

    print(f"{predators} predators, {prey} prey & {plants} plants alive in this period")

    with open(f"{newpath}//animation_params.txt", 'w') as p:
        p.write(str(f"Duration = {end - start}"))
        p.write(str(f"\ntotalpreds = {predators}"))
        p.write(str(f"\ntotalprey = {prey}"))
        p.write(str(f"\ntotalplants = {plants}"))

    return


if __name__ == '__main__':

    generate_animation_files()
