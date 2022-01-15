import implements_db as db
from tabulate import tabulate
from os import system
from useful import *
from datetime import datetime

def header():
    date = datetime.now()
    #print(f"{date.year}/{date.strftime('%B')}/{date.day} - {date.hour}:{date.minute}")
    title = "\033[33m" + "PHONEBOOK " + date.strftime("%c") + "\033[0;0m"
    print(title.center(67, " "))

    total_contacts = db.count_lines()
    total_pages = total_contacts // 5 + 1
    print(f"There are a total of {total_contacts} registered contacts".center(55, " "))
    print(f"Page {page}/{total_pages}".rjust(56, "-"))

def print_contacts():
    table = db.print_table(page)
    header = ["ID", "Name", "Phone", "Type Contact"]

    print(tabulate(table, header, tablefmt = "simple"))

def select_option():
    print("\n[P]: Previous Page \t[N]: Next Page\n")
    print("[I]: Insert Contact \t[E]: Edit Contact \n[R]: Remove Contact \t[F]: Filter \n[L]: To Locate \t\t[Q]: Exit")
    option = input("\nSelect An Option: ")
    option = option.lower()

    global page

    match option:
        case "p": page = decrement(page)
        case "n": page = increment(page)
        case "i": db.insert()
        case "e": db.update()
        case "r": db.delete()
        case "f": db.filter()
        case "l": db.to_locate()
        case "q": 
            db.close()
            exit(0)
        case _: pass

page = 1
while True:
    system("cls")
    progress_bar()
    system("cls")
    header()
    print_contacts()
    select_option()