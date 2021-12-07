
def read_parameters():

    parameters = {}

    with open("Parameters.txt") as f:
        for line in f:
            if not line in ['\n', '\r\n']:
                name, value = line.split("=")
                name = name.rstrip(" ")
                parameters[name] = value.rstrip('\n')

    inputparameters = {}

    '''
    parameters["predatorsize"] = float(parameters["predatorsize"])
    parameters["preysize"] = float(parameters["preysize"])
    parameters["groundsize"] = int(parameters["groundsize"])
    parameters["offload"] = int(parameters["offload"])
    parameters["plantsize"] = float(parameters["plantsize"])
    parameters["predatorviewdistance"] = int(parameters["predatorviewdistance"])
    parameters["preyviewdistance"] = int(parameters["preyviewdistance"])
    parameters["predatorwalkspeed"] = int(parameters["predatorwalkspeed"])
    parameters["preywalkspeed"] = int(parameters["preywalkspeed"])
    parameters["predmatingwait"] = int(parameters["predmatingwait"])
    parameters["predbornwait"] = int(parameters["predbornwait"])
    parameters["predeatingwait"] = int(parameters["predeatingwait"])
    parameters["predfertility"] = int(parameters["predfertility"])
    parameters["preymatingwait"] = int(parameters["preymatingwait"])
    parameters["preybornwait"] = int(parameters["preybornwait"])
    parameters["preyeatingwait"] = int(parameters["preyeatingwait"])
    parameters["preyfertility"] = int(parameters["preyfertility"])

    
    '''

    parameters["predatorsize"] = 5
    parameters["preysize"] = 3
    parameters["plantsize"] = 1.5

    parameters["predatorviewdistance"] = 60
    parameters["preyviewdistance"] = 50
    parameters["predatorwalkspeed"] = 8
    parameters["preywalkspeed"] = 6
    parameters["predmatingwait"] = 8
    parameters["preymatingwait"] = 4
    parameters["predbornwait"] = 10
    parameters["preybornwait"] = 5
    parameters["predeatingwait"] = 8
    parameters["preyeatingwait"] = 4
    parameters["predfertility"] = 80
    parameters["preyfertility"] = 30

    parameters["offload"] = 200


    inputparameters["groundsize"] = int(parameters["groundsize"])

    inputparameters["predatorcount"] = int(parameters["predatorcount"])
    inputparameters["predatorlifespan"] = int(parameters["predatorlifespan"])
    inputparameters["predlongevity"] = int(parameters["predlongevity"])
    inputparameters["predmatingpenalty"] = int(parameters["predmatingpenalty"])
    inputparameters["predeatinggain"] = int(parameters["predeatinggain"])

    inputparameters["preycount"] = int(parameters["preycount"])
    inputparameters["preylifespan"] = int(parameters["preylifespan"])
    inputparameters["preylongevity"] = int(parameters["preylongevity"])
    inputparameters["preymatingpenalty"] = int(parameters["preymatingpenalty"])
    inputparameters["preyeatinggain"] = int(parameters["preyeatinggain"])

    inputparameters["plantcount"] = int(parameters["plantcount"])

    parameters.update(inputparameters)
    params = [parameters, inputparameters]
    return(params)