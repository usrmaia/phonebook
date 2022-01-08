from useful import *

def input_id():
    try:
        id = int(input("Inform Contact ID: "))
        return int(id)
    except:
        return 0

def input_name():
    name = input("Name and Last Name: ")
    name = format_name(name)

    return name

def input_phone():
    country_code = input("Country Code: ")
    DDD = input("DDD: ")
    phone = input("Phone: ")
    phone = format_phone(country_code, DDD, phone)

    return phone

def input_type_contact():
    print("Types of Contact: ")
    print("[1]: Spouse \t[2]: Crush \n[3]: Friend \t[4]: Family \n[5]: Work \t[6]: Known")
    type_contact = input("Select An Option: ")
    type_contact = format_type_contact(type_contact)

    return type_contact