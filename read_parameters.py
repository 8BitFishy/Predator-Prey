
def read_parameters():

    parameters = {}

    with open("Parameters.txt") as f:
        for line in f:
            if not line in ['\n', '\r\n']:
                name, value = line.split("=")
                name = name.rstrip(" ")
                parameters[name] = value.rstrip('\n')


    parameters["predatorsize"] = float(parameters["predatorsize"])
    parameters["preysize"] = float(parameters["preysize"])
    parameters["groundsize"] = int(parameters["groundsize"])

    parameters["predatorcount"] = int(parameters["predatorcount"])
    parameters["predatorlifespan"] = int(parameters["predatorlifespan"])
    parameters["predatorwalkspeed"] = int(parameters["predatorwalkspeed"])
    parameters["predatorviewdistance"] = int(parameters["predatorviewdistance"])
    parameters["predlongevity"] = int(parameters["predlongevity"])
    parameters["predmatingpenalty"] = int(parameters["predmatingpenalty"])
    parameters["predmatingwait"] = int(parameters["predmatingwait"])
    parameters["predbornwait"] = int(parameters["predbornwait"])
    parameters["predeatinggain"] = int(parameters["predeatinggain"])
    parameters["predeatingwait"] = int(parameters["predeatingwait"])
    parameters["predfertility"] = int(parameters["predfertility"])

    parameters["preycount"] = int(parameters["preycount"])
    parameters["preywalkspeed"] = int(parameters["preywalkspeed"])
    parameters["preyviewdistance"] = int(parameters["preyviewdistance"])
    parameters["preylifespan"] = int(parameters["preylifespan"])
    parameters["preylongevity"] = int(parameters["preylongevity"])
    parameters["preymatingpenalty"] = int(parameters["preymatingpenalty"])
    parameters["preymatingwait"] = int(parameters["preymatingwait"])
    parameters["preybornwait"] = int(parameters["preybornwait"])
    parameters["preyeatinggain"] = int(parameters["preyeatinggain"])
    parameters["preyeatingwait"] = int(parameters["preyeatingwait"])
    parameters["preyfertility"] = int(parameters["preyfertility"])

    parameters["plantcount"] = int(parameters["plantcount"])
    parameters["plantsize"] = float(parameters["plantsize"])

    return(parameters)