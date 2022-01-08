import implements_db as db
from tabulate import tabulate
from os import system

def print_db():
    table = db.print_table()
    headers = ["ID", "Name", "Phone", "Type Contact"]

    print(tabulate(table, headers, tablefmt = "simple"))
    print("\n[P]: Previous Page \t[N]: Next Page\n")

def select_option():
    print("[I]: Insert Contact \t[E]: Edit Contact \n[R]: Remove Contact \t[F]: Filter \n[Q]: Exit")
    option = input("\nSelect An Option: ")
    option = option.lower()

    match option:
        case "i":
            db.insert()
        case "e":
            db.update()
        case "r":
            db.delete()
        case "f":
            db.filter()
        case "q":
            db.close()
            exit()
        case _:
            pass

while True:
    system("cls")
    print_db()
    select_option()