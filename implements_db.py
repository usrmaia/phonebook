from class_db import *
from input import *
from format import *
from tabulate import tabulate
from os import system

db = DB()
#db.create_table()

def count_lines():
    count = db.get_count()
    count = format_message(str(count))
    return int(count)

def print_table(page):
    page -= 1 # A primeira posição para o usuário é 1 mas em python é 0
    table = db.get_table()
    position_contact = 5 * page
    table = table[position_contact:position_contact + 5]
    return table

def insert():
    name = input_name()
    phone = input_phone()
    type_contact = input_type_contact()

    db.insert(name, phone, type_contact)

def update():
    id = input_id()
    name = input_name()
    phone = input_phone()
    type_contact = input_type_contact()

    db.update(id, name, phone, type_contact)

def delete():
    id = input_id()

    db.delete(id)

def filter():
    type_contact = input_type_contact()
    table = db.get_filter(type_contact)
    headers = ["ID", "Name", "Phone", "Type Contact"]
    print(tabulate(table, headers, tablefmt = "simple"))
    input("Press Key To Continue...")

def close():
    db.close()