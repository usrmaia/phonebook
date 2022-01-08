from string import ascii_lowercase

def format_name(name):
    return name[:15]

def format_message(message):
    invalid_characters = ascii_lowercase + "()-+.[],"
    for letter in invalid_characters:
        message = message.replace(letter, "")

    return message

def format_phone(country_code, DDD, phone):
    country_code = format_message(country_code)
    DDD = format_message(DDD)
    phone = format_message(phone)
    
    phone = f"+{country_code} {DDD} {phone}"
    return phone[:16]

def format_type_contact(type_contact):
    match type_contact:
        case "1": return "Spouse"
        case "2": return "Crush"
        case "3": return "Friend"
        case "4": return "Family"
        case "5": return "Work"
        case "6": return "Known"
        case _: return "Known"