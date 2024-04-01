from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self, value):
        if len(value) == 10 and value.isdigit:
            super().__init__(value)
        else:
            raise ValueError
            
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone.validate():
            self.phone.append(Phone(phone))
        else:
            print("Невірний номер телефону")

    def remove_phone(self, phone):
        if phone.validate():
            for id, phone_record in enumerate(self.phones):
                if phone_record == phone:
                    self.phones.pop(id)
        
    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                if Phone(new_phone).validate():
                    self.phones[idx] = Phone(new_phone)
                    print("Номер телефону успішно змінено.")
                else:
                    print("Невірний формат нового номеру телефону.")
                return
        print("Такого номеру телефону не існує.")

    def find_phone()


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self, contacts):
        self.contacts = contacts

    def add_record(self, record):
        if record in self.contacts:
            return "Your phone is already in database"
        else:
            self.contacts.append(record)
        

    def search_by_name():
        pass

    def contact_remove():