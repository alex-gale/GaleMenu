# Menu Classes

class menu(object):
    def __init__(self, menuName="Menu Name", border="=", inputPrompt=">"):
        # Define variables
        self.menuName = menuName
        self.menuBorder = border
        self.inputPrompt = inputPrompt
        self.menuItems = []

    def addItem(self, itemFunc, itemName="Option", parameters=[]):
        # Add an item to the menu
        newItem = menuItem(itemName, itemFunc, parameters)
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
        print("Choose an option")
        while True:
            userInput = input(self.inputPrompt + " ")
            try:
                self.menuItems[int(userInput)].execute()
                break
            except IndexError:
                print("Please choose an option from the menu.")
            except ValueError:
                print("Please choose an option from the menu.")

class menuItem(object):
    def __init__(self, optionName, optionFunc, parameters):
        # Define variables
        self.optionName = optionName
        self.optionFunc = optionFunc
        self.parameters = parameters

    def execute(self):
        # Exec the function with parameters
        self.optionFunc(*self.parameters)
