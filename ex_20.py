class Printer:
    def __init__(self, model):
        self.model = model
        print(f'A new printer "{model}" has arrived')

    def pages_print(self, *args):
        [print(x) for x in args]


p1 = Printer("HP OfficeJet Pro 9015e")
list_to_print = ["apple", "banana", "cherry"]

p1.pages_print(list_to_print)
