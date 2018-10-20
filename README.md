# GaleMenu - Simple Menu Generator

GaleMenu is a simple menu generator for Python.

## Installation
To install GaleMenu, run `pip install galemenu`.

To include it in your project, import it like so:
```python
import galemenu
```
## Use

### Creating a menu
```python
menu = galemenu.menu(name, [border], [prompt], [text], [error])
```
**name** - the title of the menu

**border** - the underline of the title (optional - default `=`)

**prompt** - the characters shown before the input prompt (optional - default `>`)

**text** - the text shown before the prompt (optional - blank by default)

**error** - the message shown if an invalid menu choice made (optional - default `Please choose an option from the menu.`)

### Adding options to menu
```python
menu.additem(function, name, [parameters])
```
**function** - the function that the menu option points to

**name** - the display name of the menu option

**parameters** - an array of parameters to pass to the function (optional)

### Displaying the menu
```python
menu.start()
```
This will start the menu and display it at the point when it is

### Example
```python
import galemenu

def coolFunction(text):
    print(text)

menu = galemenu.menu("The best menu")
menu.addItem(coolFunction, "Item number 1", ["hey"])
menu.addItem(coolFunction, "Item number 2", ["hey2"])

menu.start()
```
This menu, called "The best menu", has 2 options - `Item number 1` and `Item number 2`. They each pass a single parameter to the function `coolFunction`.

![this is where the picture of the menu is supposed to be](https://i.gyazo.com/2b2f686fb76517d4b525f728502c19fd.png)
