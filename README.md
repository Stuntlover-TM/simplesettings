# simplesettings
A simple settings module for Python

## Simple docs
`simplesettings.clear()` Clears the settings file leaving only `name|value` behind, takes 0 arguments

---

`simplesettings.save()` Saves a variable to the settings file, takes 2 arguments, name and value; example:

```py
import simplesettings

PlayerKey = "10"

simplesettings.save("PlayerKey", PlayerKey)
```

Outputted settings file:
```
PlayerKey = 10
```

---

`simplesettings.save_dict()` Saves an entire dictionary to the settings file in simplesettings format; example:

```py
import simplesettings

a_dictionary = {
    "Data": 123,
    "DictData": {"You can save": "a dictionary!"},
    "MoreData": ("A", "B", "C")
}

simplesettings.save_dict(a_dictionary)
```
Outputted settings file:
```
Data = 123
DictData = {'You can save': 'a dictionary!'}
MoreData = ('A', 'B', 'C')
```

---

`simplesettings.load()` Loads the settings file into a dictionary; example:

```py
import simplesettings

print(simplesettings.load())
```
Output: `{'Data': 123, 'DictData': {'You can save': 'a dictionary!'}, 'MoreData': ('A', 'B', 'C')}`

`simplesettings.loads()` The same as `simplesettings.load()` but takes a simplesettings string as an argument, example:
```py
import simplesettings

print(simplesettings.loads(
    """
    Data = 123
    DictData = {'You can save': 'a dictionary!'}
    MoreData = ('A', 'B', 'C')
    """
))
```
Output: `{'Data': 123, 'DictData': {'You can save': 'a dictionary!'}, 'MoreData': ('A', 'B', 'C')}`

Note that the `load()` and `loads()` functions will automatically convert strings of integers, floats, booleans, tuples, lists and dictionaries to the right type, don't forget to convert them back to the type you want (which you should be doing anyway x))

---

Please feel free to create a pull request if you encounter any issues or something that could be improved
