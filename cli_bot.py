from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit:
            super.__init__(value)
        else:
            raise ValueError
        
    def phone_validator(self, value):
        if len(value) == 10 and value.isdigit():
            return value
        else:
            raise TypeError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
        return self.phones
          
    def remove_phone(self, phone_number):
        self_phones = [phone for phone in self.phones if str(phone) != phone_number]
        return self_phones
          
    def search_phone(self, value):
        for phone in self.phones:
            if value in phone:
                return phone
            else:
                raise ValueError
          
    def edit_phone(self, old_phone, new_phone):
        if not Phone.is_valid(new_phone):
            raise ValueError
        
        for phone in self.phones:
            if phone == old_phone:
                phone = new_phone
        raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data

    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            raise ValueError
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError