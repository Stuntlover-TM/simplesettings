import ast
import os


def _init(filename):
    """
    Called by most functions by default, simply creates the file if it does not already exist.
    """
    if not os.path.isfile(filename):
        open(filename, "w").close()

def clear(filename=".settings"):
    """
    Clear the settings file.
    """
    open(filename, "w").close()


def save_dict(dictionary, filename=".settings", table="main"):
    """
    Saves an entire dictionary to the settings file in simplesettings format, example:

    
    import simplesettings_py as settings

    a_dictionary = {
	    "Data": 123,
	    "MoreData": "One Two Three",
	    "MoreMoreData": {"You can save": "a dictionary!"},
	    "EvenMoreMoreData": ("A", "B", "C")
    }

    settings.save_dict(a_dictionary, table="saved_dict")
    """
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
    """
    Saves a variable to the settings file, example:

    
    import simplesettings_py as settings

    settings.save("Data", 123)
    settings.save("MoreData", "real")
    settings.save("MoreMoreData", {"You can save": "a dictionary!"}, table="dictionaries")
    settings.save("EvenMoreMoreData", ("A", "B", "C"), table="tuples")
    """
    save_dict({key: value}, filename=filename, table=table)


def load(filename=".settings"):
    """
    Loads the settings file into a dictionary; example:

    
    import simplesettings_py as settings

    print(settings.load())
    """
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
    '''
    The same as simplesettings.load() but takes a simplesettings string as an argument, example:

    
    import simplesettings_py as settings

    print(settings.loads(
    """
    (main)
    Data = 123
    MoreData = real
  
    (dictionaries)
    MoreMoreData = {'You can save': 'a dictionary!'}
  
    (tuples)
    EvenMoreMoreData = ('A', 'B', 'C')
    """
    ))
    '''
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
