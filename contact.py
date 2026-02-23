'''
Names:
Date:
Group:
Description:
'''

class Contact: 

    def __init__(self, fn, ln, ph, addr, city, zip):
        self._first_name = fn
        self._last_name = ln
        self._phone_number = ph
        self._address = addr
        self._city = city
        self._zip_code = zip

    def __lt__(self, other):
        #Compares the last names of two contacts, and if they are the same, compares the first names
        if self._last_name == other._last_name:
            return self._first_name < other._first_name
        return self._last_name < other._last_name
    
    def __str__(self):
        #Formats the contact information into a string for easy printing
        return f"{self._first_name} {self._last_name}\n{self._phone_number}\n{self._address}\n{self._city} {self._zip_code}"
