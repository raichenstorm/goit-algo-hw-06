from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit:
            super.__init__(value)
        else:
            raise ValueError("The phone you entered is invalid")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
          
    def remove_phone(self, phone_number):
        self_phones = [phone for phone in self.phones if str(phone) != phone_number]
          
    def search_phone(self, value):
        for phone in self.phones:
            if value in str(phone):
                return str(phone)
        return "There is no such phone number in database"
          
    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if str(phone) == old_value:
                phone.value = new_value
                return "Phone number edited successfully."
        return "There is no such phone number in database"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record 
        return "Your record has been added successfully"

    def find_record(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            return "There is no record by your name in database"
    
    def remove_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return "There is no record by your name in database"