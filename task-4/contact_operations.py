def validate_contact_args(args: list) -> str:
    
    if len(args) != 2:
        return "Invalid command. Usage: [command] [ім'я] [номер телефону]"

    try:
        name, phone = args
        if not phone.isdigit():
            return "Invalid phone number. Phone number must contain only digits."

    except ValueError:
        return "Invalid command. Usage: [command] [ім'я] [номер телефону]"

    return None


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command. Usage: [command] [ім'я] [номер телефону]"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Invalid command. Usage: [command] [ім'я] [номер телефону]"
        
    return inner


@input_error
def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise IndexError
    
    name, phone = args

    if not phone.isdigit():
        raise ValueError
    
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise IndexError
    
    name, phone = args

    if not phone.isdigit():
        raise ValueError

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    else:
        raise KeyError

@input_error
def show_phone(args: list, contacts: dict) -> str:

    if len(args) != 1:
        raise IndexError
    
    name_lower = args[0].lower()

    for stored_name, phone in contacts.items():

        if name_lower == stored_name.lower():
            return phone
    
    raise KeyError

@input_error
def show_all(contacts: dict) -> str:

    if not contacts:
        return "No contacts saved."
    
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"

        return result.strip()





# @input_error
# def show_all(contacts: dict) -> str:
#     if not contacts:
#         return "No contacts saved."
#     else:
#         result = ""
#         for name, phone in contacts.items():
#             result += f"{name}: {phone}\n"
#         return result.strip()

