#checking args
def checking_args(args, length, schema):
  if len(args) != length:
      raise ValueError(f"Please enter the correct schema: {schema}")

  return args

#validate phone
def validate_phone(phone):
  if not phone.isdigit():
    raise ValueError("Phone number must contain only digits")

  return phone

#parse input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#add contact
def add_contact(args, contacts):
    try:
      name, phone = checking_args(args, 2, "[command] [name] [phone]")
      phone = validate_phone(phone)
    except ValueError as error:
      return str(error)

    if name in contacts:
      return "This user already exists in the contact list, please use command 'change [name] [phone]' instead."
    contacts[name] = phone
    return "Contact added."

#change contact
def change_contact(args, contacts):
    try:
      name, phone = checking_args(args, 2, "[command] [name] [phone]")
      phone = validate_phone(phone)
    except ValueError as error:
      return str(error)
    contacts[name] = phone
    return "Contact changed."

#Show phone
def show_phone(args, contacts):
    try:
      name, = checking_args(args, 1, "[command] [name]")
    except ValueError as error:
      return str(error)
    
    if name not in contacts:
       return "Contact not found"
    
    return f"The {name.capitalize()}'s phone is:  {contacts[name]}"

#Show all
def show_all(contacts):
    if not contacts:
       return "No contacts found"
    
    list = []

    for name, phone in contacts.items():
       list.append(f"{name.capitalize():<10} {phone}")

    return "\n".join(list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
