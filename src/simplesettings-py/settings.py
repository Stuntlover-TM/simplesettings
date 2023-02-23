import ast
import os


def _init(filename):
    if not os.path.isfile(".settings"):
        open(filename, "w").close()

def clear(filename=".settings"):
    open(filename, "w").close()


def save_dict(dictionary, filename=".settings", table="main"):
    _init(filename)

    with open(filename, "r") as ssfile:
        variables = loads(ssfile.read())

    for key, value in dictionary.items():
        try:
            variables[table][key] = value
        except:
            variables[table] = {}
            variables[table][key] = value

    with open(filename, "w") as ssfile:
        first_write = True
        for table_name, table_dict in variables.items():
            ssfile.write(f"\n({table_name})\n") if not first_write else ssfile.write(f"({table_name})\n")
            first_write = False

            for name, value in table_dict.items():
                ssfile.write(f"{name} = {value}\n")


def save(key, value, filename=".settings", table="main"):
    save_dict({key: value}, filename=filename, table=table)


def load(filename=".settings"):
    _init(filename=filename)
    return_dict = {}

    with open(filename, "r") as ssfile:
        varlines = ssfile.read().split("\n")

        for line in varlines:
            if line.strip().startswith("(") and line.strip().endswith(")"):
                table_name = line.strip().split("(")[1].replace(")", "")
                return_dict[table_name] = {}
                is_table = True
                continue
            else:
                is_table = False

            try:
                if not is_table:
                    name = line.split("=")[0].strip()
                    value = ast.literal_eval(line.split("=")[1].split("#")[0].strip())
                    return_dict[table_name][name] = value
            except:
                try:
                    if not is_table:
                        name = line.split("=")[0].strip()
                        value = line.split("=")[1].split("#")[0].strip()
                        return_dict[table_name][name] = value
                except:
                    continue

    return return_dict

def loads(string):
    return_dict = {}
    varlines = string.split("\n")

    for line in varlines:
        if line.strip().startswith("(") and line.strip().endswith(")"):
            table_name = line.strip().split("(")[1].replace(")", "")
            return_dict[table_name] = {}
            is_table = True
            continue
        else:
            is_table = False

        try:
            if not is_table:
                name = line.split("=")[0].strip()
                value = ast.literal_eval(line.split("=")[1].split("#")[0].strip())
                return_dict[table_name][name] = value
        except:
            try:
                if not is_table:
                    name = line.split("=")[0].strip()
                    value = line.split("=")[1].split("#")[0].strip()
                    return_dict[table_name][name] = value
            except:
                continue

    return return_dict
