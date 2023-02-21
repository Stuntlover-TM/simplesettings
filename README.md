# simplesettings
A simple settings module for Python that uses the csv and ast modules

The settings file is not supposed to be readable for humans, and instead only for parsing for programs
The human readable version is [in this repo](shh I didnt add a link yet)

## Simple docs
`simplesettings.clear()` Clears the .settings file leaving only `name|value` behind, takes 0 arguments


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


`simplesettings.load()` Loads the .settings file into a dictionary, example:

```py
import simplesettings

print(simplesettings.load())
```
Output:
`{'PlayerKey': 10}`

Please feel free to create a pull request
