#part 1: create customer class

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    #property decorator for customer id
    #getting customer id
    @property
    def customer_id(self):
        return self._customer_id

    #setting the customer id
    @customer_id.setter
    def customer_id(self, value):
    #ensures that entered value for customer id is an integer
        if isinstance(value, int):
            self._customer_id = value
        else:
            raise ValueError("Customer ID must be an integer.")

    #property decorator for first_name
    #getting first name
    @property
    def first_name(self):
        return self._first_name

    #setting first name
    @first_name.setter
    def first_name(self,value):
        #ensures first name is a string
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError("First name must be a string.")

    #property decorator for last_name
    #getting last name
    @property
    def last_name(self):
        return self._last_name

    #setting last name
    @last_name.setter
    def last_name(self,value):
        #ensures last name is a string
        if isinstance(value, str):
            self._last_name = value
        else:
            raise ValueError("Last name must be a string.")

    #property decorator for email
    #getting email
    @property
    def email(self):
        return self._email

    #setting email with validation
    @email.setter
    def email(self, value):
        if "@" in value:
            self._email = value
        else:
            raise ValueError ("Invalid email address. Must contain '@'.")


    #property decorator for phone_number
    #getting phone_number
    @property
    def phone_number(self):
        return self._phone_number

    #setting phone_number
    @phone_number.setter
    def phone_number(self, value):
        if value.isdigit() and len(value) == 10:
            self._phone_number = value
        else:
            raise ValueError("Phone number must be a valid 10-digit number.")

    #creating a method get_phone_number
    def get_phone_number(self):
        return self.phone_number

# Using main to test instances of our customer class

if __name__ == "__main__":
    # Create a customer instance
    customer = Customer(1, "John", "Doe", "john.doe@example.com", "1234567890")

    # Print customer details
    print("Customer ID:", customer.customer_id)
    print("First Name:", customer.first_name)
    print("Last Name:", customer.last_name)
    print("Email:", customer.email)
    print("Phone Number:", customer.get_phone_number())

    # Update the customer's email and phone number
    customer.email = "jane.doe@example.com"
    customer.phone_number = "0987654321"

    # Print updated details
    print("\nUpdated Customer Info:")
    print("Email:", customer.email)
    print("Phone Number:", customer.get_phone_number())
