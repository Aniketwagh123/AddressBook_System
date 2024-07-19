class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")
        self.address_book: AddressBook = AddressBook()
        self.__run()

    def __menu(self) -> None:
        print(f'{"-"*10} Select Option {"-"*10}')
        print('1. Add Contact')
        print('2. Show All Contacts')
        print('3. Exit')

    def __run(self) -> None:
        while True:
            self.__menu()
            option: int = int(input('Enter your option: '))
            if option == 1:
                self.__add_contact()
            elif option == 2:
                self.__show_all_contacts()
            elif option == 3:
                print("Exiting Address Book Program")
                break
            else:
                print("Invalid option, please try again.")

    def __add_contact(self) -> None:
        self.address_book.add_contact()

    def __show_all_contacts(self) -> None:
        contacts: list[Contact] = self.address_book.get_all_contacts()
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(contact)


class AddressBook:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def add_contact(self) -> None:
        first_name: str = input("Enter First Name: ")
        last_name: str = input("Enter Last Name: ")
        address: str = input("Enter Address: ")
        city: str = input("Enter City: ")
        state: str = input("Enter State: ")
        zip_code: int = int(input("Enter Zip Code: "))
        phone_number: int = int(input("Enter Phone Number: "))
        email: str = input("Enter Email: ")
        contact: Contact = Contact(first_name, last_name, address, city,
                                   state, zip_code, phone_number, email)
        for c in self.__contacts:
            if contact == c:
                print(
                    f"Sorry, the contact with first name: {first_name} and last name: {last_name} already exists in AddressBook")
                return
        self.__contacts.append(contact)

    def get_all_contacts(self):
        return self.__contacts


class Contact:
    def __init__(self, first_name: str, last_name: str, address: str, city: str, state: str, zip_code: int, phone_number: int, email: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__address: str = address
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: int = zip_code
        self.__phone_number: int = phone_number
        self.__email: str = email

    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name} {self.__address} {self.__city} {self.__state} {self.__zip_code} {self.__phone_number} {self.__email}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Contact):
            return self.__first_name == other.__first_name and self.__last_name == other.__last_name
        return False


if __name__ == "__main__":
    AddressBookMain()