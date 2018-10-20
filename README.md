## Installation
To install GaleMenu, run `pip install galemenu`.

To include it in your project, import it like so:
```python
import galemenu

menu = galemenu.menu("Cool Title")
...
```
## Use

### Creating a menu
```python
import galemenu

menu = galemenu.menu(title, [border], [imputPrompt])
```
**title** - the title of the menu
**border** - the underline of the title
**inputPrompt** - the characters shown before the input prompt
