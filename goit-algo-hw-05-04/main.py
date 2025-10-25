def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Please provide both name and phone number."
        except IndexError:
            return "Error: Missing required argument(s)."
        except KeyError:
            return "Error: Contact not found."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name} {contacts[name]}"
    

def show_all(contacts):
    if  contacts:
        result = ["All contacts:"]
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    




def main():
    contacts = {}
    print("Welcome to the assistanst bot!")
    
    while True:
        try:
            user_input = input("Enter a command:")
            command, args = parse_input(user_input)
        
            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("Hello! How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command == "": 
                print("Please enter a command.")
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occured: {e}")


if __name__ == "__main__":
    main()