# Simple Contact Book
# Create a contact book using a dictionary
contact_book = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Suresh": "9988776655"
}   
# Print all contacts
print("Contact Book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")
# Ask user for a name
search_name = input("Enter the name to search: ")
# Display the phone number if found
if search_name in contact_book:
    print(f"Phone number of {search_name}: {contact_book[search_name]}")
else:
    print("Contact not found")
