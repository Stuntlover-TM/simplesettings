import ast
import os


def _init(filename):
    if not os.path.isfile(filename):
        open(filename, "w").close()


def clear(filename=".settings"):
    open(filename, "w").close()


def save_dict(dictionary, filename=".settings"):
    _init(filename)
    with open(filename, "r") as variablesf:
        variables = loads(variablesf.read())

    for key, value in dictionary.items():
        variables[key] = value

    with open(filename, "w") as ssfile:
        for name, value in variables.items():
            ssfile.write(f"{name} = {value}\n")


def save(name, value, filename=".settings"):
    save_dict({name: value}, filename=filename)


def load(filename=".settings"):
    _init(filename=filename)
    return_dict = {}
    with open(filename, "r") as ssfile:
        varlines = ssfile.read().split("\n")
        for line in varlines:
            try:
                name = line.split("=")[0].strip()
                value = ast.literal_eval(line.split("=")[1].split("#")[0].strip())
                return_dict[name] = value
            except:
                try:
                    name = line.split("=")[0].strip()
                    value = line.split("=")[1].split("#")[0].strip()
                    return_dict[name] = value
                except: continue
    return return_dict


def loads(string):
    return_dict = {}
    varlines = string.split("\n")
    for line in varlines:
        try:
            name = line.split("=")[0].strip()
            value = ast.literal_eval(line.split("=")[1].split("#")[0].strip())
            return_dict[name] = value
        except:
            try:
                name = line.split("=")[0].strip()
                value = line.split("=")[1].split("#")[0].strip()
                return_dict[name] = value
            except: continue
    return return_dict
