import csv
from customer import Customer

# CSV file name
csv_file = "customer_data.csv"

# Load customer records from the CSV file
def load_customers():
    customer_list = []
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 5:  # Ensure the row contains 5 columns
                    customer_id, first_name, last_name, email, phone_number = row
                    customer = Customer(int(customer_id), first_name, last_name, email, phone_number)
                    customer_list.append(customer)
    except FileNotFoundError:
        print("CSV file not found, starting with an empty customer list.")
    return customer_list

# Save customer records to the CSV file
def save_customers(customers):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        for customer in customers:
            writer.writerow([customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone_number])

# Create a new customer and add to the list
def create_customer(customers):
    try:
        customer_id = int(input("Enter customer ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number (10 digits): ")

        customer = Customer(customer_id, first_name, last_name, email, phone_number)
        customers.append(customer)
        save_customers(customers)
        print("Customer added successfully.")
    except ValueError as error:
        print(f"Error: {error}")

# Edit an existing customer
def edit_customer(customers):
    try:
        index = int(input("Enter the index of the customer to edit: ")) - 1
        if 0 <= index < len(customers):
            customer = customers[index]
            print(f"Editing Customer: {customer.first_name} {customer.last_name}")

            first_name = input(f"Enter new first name (current: {customer.first_name}): ") or customer.first_name
            last_name = input(f"Enter new last name (current: {customer.last_name}): ") or customer.last_name
            email = input(f"Enter new email (current: {customer.email}): ") or customer.email
            phone_number = input(f"Enter new phone number (current: {customer.phone_number}): ") or customer.phone_number

            customer.first_name = first_name
            customer.last_name = last_name
            customer.email = email
            customer.phone_number = phone_number

            save_customers(customers)
            print("Customer edited successfully.")
        else:
            print("Invalid customer index.")
    except ValueError as error:
        print(f"Error: {error}")

# Delete a customer
def delete_customer(customers):
    try:
        index = int(input("Enter the index of the customer to delete: ")) - 1
        if 0 <= index < len(customers):
            deleted_customer = customers.pop(index)
            save_customers(customers)
            print(f"Customer {deleted_customer.first_name} {deleted_customer.last_name} deleted successfully.")
        else:
            print("Invalid customer index.")
    except ValueError as error:
        print(f"Error: {error}")

# Display all customers
def display_customers(customers):
    if not customers:
        print("No customers found.")
        return

    print("\nCustomer List:")
    print("==============")
    for i, customer in enumerate(customers, start=1):
        print(f"{i}. ID: {customer.customer_id}, Name: {customer.first_name} {customer.last_name}, Email: {customer.email}, Phone: {customer.phone_number}")

# Main function to run the application
def main():
    customers = load_customers()

    while True:
        print("\nCustomer Management System")
        print("==========================")
        print("1. Create New Customer")
        print("2. Edit Existing Customer")
        print("3. Delete Existing Customer")
        print("4. Display Customers")
        print("5. Quit")
        print()

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            create_customer(customers)
        elif choice == "2":
            display_customers(customers)
            edit_customer(customers)
        elif choice == "3":
            display_customers(customers)
            delete_customer(customers)
        elif choice == "4":
            display_customers(customers)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
