contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))

while True:
    choose = int(
        input(
            "Menu: \n1. Add new contact\n2. Search contact\n3. Display contact\n4. Edit\n5. Delete\n"
        )
    )
    if choose == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
    elif choose == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "contact number is:", contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choose == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choose == 4:
        edit_contact = input("Enter the contact to be edit: ")
        if edit_contact in contact:
            phone = input("Enter mobile number: ")
            contact[edit_contact] = phone
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choose == 5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
