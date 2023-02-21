# simplesettings
A simple settings module for Python that uses the csv and ast modules

The settings file is not supposed to be readable for humans, and instead only for parsing for programs
The human readable version is [in this repo](shh I didnt add a link yet)

## Simple docs
`simplesettings.clear()` Clears the .settings file leaving only `name|value` behind, takes 0 arguments

---

`simplesettings.save()` Saves a variable to the .settings file, takes 2 arguments, name and value; example:

```py
import simplesettings

PlayerKey = "10"

simplesettings.save("PlayerKey", PlayerKey)
```

Outputted .settings file:
```csv
name|value
PlayerKey|10
```

---

`simplesettings.load()` Loads the .settings file into a dictionary; example:

```py
import simplesettings

print(simplesettings.load())
```
Output: `{'PlayerKey': 10}`

Note that the `simplesettings.load()` function will automatically convert strings of integers, floats, tuples, lists and dictionaries to the right type,
don't forget to convert them back to the type you want (which you should be doing anyway x))

---

Please feel free to create a pull request if you encounter any issues or something that could be improved
