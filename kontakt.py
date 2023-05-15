import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL)''')

def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    c.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    print("Contact added successfully")

def edit_contact():
    id = int(input("Enter contact id: "))
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    c.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, id))
    conn.commit()
    print("Contact updated successfully")

def delete_contact():
    id = int(input("Enter contact id: "))
    c.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    print("Contact deleted successfully")

def view_contacts():
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    if len(contacts) == 0:
        print("No contacts found")
    else:
        print("Contacts:")
        for contact in contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Email:", contact[2])
            print("Phone:", contact[3])
            print("")

create_table()

while True:
    print("1. Add contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. View contacts")
    print("5. Exit")
    choice = input("Enter choice (1-5): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        view_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice")

conn.close()