# simplesettings
A simple settings module for Python

## Simple docs
`simplesettings.clear()` Clears the settings file, takes 0 arguments

---

`simplesettings.save()` Saves a variable to the settings file, example:

```py
import simplesettings

simplesettings.save("Data", 123)
simplesettings.save("MoreData", "real")
simplesettings.save("MoreMoreData", {"You can save": "a dictionary!"})
simplesettings.save("EvenMoreMoreData", ("A", "B", "C"))
```

Outputted settings file:
```
Data = 123
MoreData = real
MoreMoreData = {'You can save': 'a dictionary!'}
EvenMoreMoreData = ('A', 'B', 'C')
```

---

`simplesettings.save_dict()` Saves an entire dictionary to the settings file in simplesettings format, example:

```py
import simplesettings

a_dictionary = {
    "Data": 123,
    "MoreData": "One Two Three",
    "MoreMoreData": {"You can save": "a dictionary!"},
    "EvenMoreMoreData": ("A", "B", "C")
}

simplesettings.save_dict(a_dictionary)
```
Outputted settings file:
```
Data = 123
MoreData = One Two Three
MoreMoreData = {'You can save': 'a dictionary!'}
EvenMoreMoreData = ('A', 'B', 'C')
```

---

`simplesettings.load()` Loads the settings file into a dictionary; example:

```py
import simplesettings

print(simplesettings.load())
```
Output: `{'Data': 123, 'MoreData': 'real', 'MoreMoreData': {'You can save': 'a dictionary!'}, 'EvenMoreMoreData': ('A', 'B', 'C')}`

---

`simplesettings.loads()` The same as `simplesettings.load()` but takes a simplesettings string as an argument, example:
```py
import simplesettings

print(simplesettings.loads(
    """
    Data = 123
    MoreData = real
    MoreMoreData = {'You can save': 'a dictionary!'}
    EvenMoreMoreData = ('A', 'B', 'C')
    """
))
```
Output: `{'Data': 123, 'MoreData': 'real', 'MoreMoreData': {'You can save': 'a dictionary!'}, 'EvenMoreMoreData': ('A', 'B', 'C')}`

Note that the `load()` and `loads()` functions will automatically convert strings of integers, floats, booleans, tuples, lists and dictionaries to the right type, don't forget to convert them back to the type you want (which you should be doing anyway x))

---

Please feel free to create a pull request if you encounter any issues or something that could be improved
