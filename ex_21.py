class Printer:
    def __init__(self, model):
        self.model = model
        print(f'A new printer "{model}" has arrived')

    def pages_print(self, thislist):
        [print(x) for x in thislist]


class PocketPrinter(Printer):
    pass

pp = PocketPrinter("Xiaomi Mi")
list_to_print = ["photo1", "photo2", "photo3"]

pp.pages_print(list_to_print)
