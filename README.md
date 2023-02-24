# simplesettings-py
Python settings files done simple.
[PyPI Page here](https://pypi.org/project/simplesettings-py)

## Installation
Simply run `python -m pip install simplesettings-py` in your terminal.

## Simple docs
`simplesettings.clear()` Clears the settings file

---

`simplesettings.save()` Saves a variable to the settings file, example:

```py
import simplesettings_py as settings

settings.save("Data", 123)
settings.save("MoreData", "real")
settings.save("MoreMoreData", {"You can save": "a dictionary!"}, table="dictionaries")
settings.save("EvenMoreMoreData", ("A", "B", "C"), table="tuples")
```

Outputted settings file (by default .settings):
```
(main)
Data = 123
MoreData = real

(dictionaries)
MoreMoreData = {'You can save': 'a dictionary!'}

(tuples)
EvenMoreMoreData = ('A', 'B', 'C')
```

---

`simplesettings.save_dict()` Saves an entire dictionary to the settings file in simplesettings format, example:

```py
import simplesettings_py as settings

a_dictionary = {
	"Data": 123,
	"MoreData": "One Two Three",
	"MoreMoreData": {"You can save": "a dictionary!"},
	"EvenMoreMoreData": ("A", "B", "C")
}

settings.save_dict(a_dictionary, table="saved_dict")
```
Outputted settings file:
```
(saved_dict)
Data = 123
MoreData = One Two Three
MoreMoreData = {'You can save': 'a dictionary!'}
EvenMoreMoreData = ('A', 'B', 'C')
```

---

`simplesettings.load()` Loads the settings file into a dictionary; example:

```py
import simplesettings_py as settings

print(settings.load())
```
Output: `{'saved_dict': {'Data': 123, 'MoreData': 'One Two Three', 'MoreMoreData': {'You can save': 'a dictionary!'}, 'EvenMoreMoreData': ('A', 'B', 'C')}}`

You can use this to get certain values, example:

```py
import simplesettings_py as settings

settings = settings.load()
print(settings["saved_dict"]["Data"])
```
Output: `123`

---

`simplesettings.loads()` The same as `simplesettings.load()` but takes a simplesettings string as an argument, example:
```py
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
```
Output: `{'main': {'Data': 123, 'MoreData': 'real'}, 'dictionaries': {'MoreMoreData': {'You can save': 'a dictionary!'}}, 'tuples': {'EvenMoreMoreData': ('A', 
'B', 'C')}}`

Note that the `load()` and `loads()` functions will automatically convert strings of integers, floats, booleans, tuples, lists and dictionaries to the right type, don't forget to convert them back to the type you want (which you should be doing anyway x))

---

Please feel free to create a pull request if you encounter any issues or something that could be improved
