from data_base import *
from useful import *
from input import *

db = DB()
#db.create_table()

def print_table():
    db.print_table()

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

def close():
    db.close()
