dict_my = {
    "book1": 111,
    "book2": 222,
    "book3": 333,
    "book4": 444,
    "book5": 555
}


def search(book):
    if dict_my.get(book) != None:
        print(f'In the "{book}" {dict_my.get(book)} pages')
    else:
        print("Doesn't exist")


search('book1')
