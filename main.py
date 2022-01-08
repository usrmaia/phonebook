import implements_db as db
from tabulate import tabulate
from os import system
from useful import *
from datetime import datetime

def header():
    date = datetime.now()
    #print(f"{date.year}/{date.strftime('%B')}/{date.day} - {date.hour}:{date.minute}")
    print("PHONEBOOK    " + date.strftime("%c"))

    total = db.count_lines()
    print(f"There are a total of {total} registered contacts")

def print_contacts():
    table = db.print_table(page)
    headers = ["ID", "Name", "Phone", "Type Contact"]

    print(tabulate(table, headers, tablefmt = "simple"))

def select_option():
    print("\n[P]: Previous Page \t[N]: Next Page\n")
    print("[I]: Insert Contact \t[E]: Edit Contact \n[R]: Remove Contact \t[F]: Filter \n[Q]: Exit")
    option = input("\nSelect An Option: ")
    option = option.lower()

    global page

    match option:
        case "p":
            page = decrement(page)
        case "n":
            page = increment(page)
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

page = 1

while True:
    system("cls")
    header()
    print_contacts()
    select_option()