from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string")
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit string")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for p in self.phones:
            if p.value == old_phone:
                if len(new_phone) != 10 or not new_phone.isdigit():
                    raise ValueError
                p.value = new_phone
                phone_found = True
        if not phone_found:
            raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")

    book.delete("Jane")
