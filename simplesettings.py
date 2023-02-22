import csv
import ast
import io
import os


def _init():
    if not os.path.isfile(".settings"):
        with open(".settings", "w", newline="") as cachefile:
            writer = csv.writer(cachefile, delimiter="|")
            writer.writerow(["name", "value"])


def clear():
    with open(".settings", "w", newline="") as cachefile:
        writer = csv.writer(cachefile, delimiter="|")
        writer.writerow(["name", "value"])  


def save(name, value):
    _init()
    with open(".settings", "a", newline="") as cachefile:
        writer = csv.writer(cachefile, delimiter="|")
        writer.writerow([name, value])


def load():
    _init()
    with open(".settings", "r") as cachefile:
        reader = csv.DictReader(cachefile, delimiter="|")
        cachedicts = list(reader)
        return_cache = {}

        for dictionary in cachedicts:
            for i, j in dictionary.items():
                try:
                    return_cache[dictionary["name"]] = ast.literal_eval(str(dictionary["value"]))# if isinstance(j, dict) else None
                except: return_cache[dictionary["name"]] = j
        return return_cache


def loads(str):
    _init()
    reader = csv.DictReader(io.StringIO(str.strip()), delimiter="|")
    cachedicts = list(reader)
    return_cache = {}

    for dictionary in cachedicts:
        for i, j in dictionary.items():
            try:
                return_cache[dictionary["name"]] = ast.literal_eval(str(dictionary["value"]))# if isinstance(j, dict) else None
            except: return_cache[dictionary["name"]] = j
    return return_cache
