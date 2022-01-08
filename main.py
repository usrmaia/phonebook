import implements_db as db

def select_option():
    print("[I]: Insert Contact \t[E]: Edit Contact \n[R]: Remove Contact \t[Q]: Exit")
    option = input("Select An Option: ")
    option = option.lower()

    match option:
        case "i":
            db.insert()
        case "e":
            db.update()
        case "r":
            db.delete()
        case "q":
            db.close()
        case _:
            pass


select_option()