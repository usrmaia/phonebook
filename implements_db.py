from class_db import *
from input import *
from tabulate import tabulate
from os import system

db = DB()
#db.create_table()

def print_table():
    table = db.get_table()
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
    system("pause")

def close():
    db.close()
