# Quiz 9 question 3
try:
    contacts = open("customers.csv")

    for contact in contacts:
        print(contact.strip())
    contacts.close()
except IOError:
    print("Error opening file :( ")
finally:
    print("Ending program")