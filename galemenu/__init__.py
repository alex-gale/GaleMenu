# Menu Classes

class menu(object):
    def __init__(self, name="Menu Name", border="=", prompt=">", text=""):
        # Define variables
        self.menuName = name
        self.menuBorder = border
        self.prompt = prompt
        self.text = text
        self.menuItems = []

    def addItem(self, function, name="Option", parameters=[]):
        # Add an item to the menu
        newItem = menuItem(function, name, parameters)
        self.buffer = newItem
        self.menuItems.append(newItem)

    def start(self):
        #Print the top bit
        print(self.menuName)
        for i in range(len(self.menuName) - 1):
            print(self.menuBorder, end="")
        print(self.menuBorder)

        #Print the options
        for i in range(len(self.menuItems)):
            print(i, end=": ")
            print(self.menuItems[i].optionName)

        # take user input
        print(self.text)
        while True:
            userInput = input(self.prompt + " ")
            try:
                self.menuItems[int(userInput)].execute()
                break
            except IndexError:
                print("Please choose an option from the menu.")
            except ValueError:
                print("Please choose an option from the menu.")

class menuItem(object):
    def __init__(self, optionFunc, optionName, parameters):
        # Define variables
        self.optionName = optionName
        self.optionFunc = optionFunc
        self.parameters = parameters

    def execute(self):
        # Exec the function with parameters
        self.optionFunc(*self.parameters)
