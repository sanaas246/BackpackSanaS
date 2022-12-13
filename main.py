class Backpack: 
    def __init__(self, color, size, items, open):
        self.color = color
        self.size = size 
        self.items = [ ]
        self.open = False

    def openBag(self):
        self.open = True
        print("Backpack is open")

    def closeBag(self):
        self.open = False
        print("Backpack is closed")

    def putin(self,item):
        if self.open == True:
            if item in self.items:
                self.items.append(item)
                print(f"These items are in your bag: {self.items}")
        else:
            print("Backpack not open")

    def takeout(self,item):
        if self.open == True:
            if item in self.items:
                self.items.pop(item)
                print(f"These items are in your bag: {self.items}")
        else:
            print("Backpack not open")

bag1 = Backpack("blue", "small", [], False)
print(bag1.open)