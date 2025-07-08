from abc import ABC, abstractmethod
from datetime import datetime


class Book(ABC):
    def __init__(self, isbn, title, author, year, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        
        
    @abstractmethod
    def buy(self, quantity, email, address):
        pass
    
    def is_outdated(self, current_year, years_threshold):
        return (current_year - self.year) > years_threshold



# =======================
# Different types o Books
# ========================


class PapaerBook(Book):
    def __init__(self, isbn, title, author, year, price, stock):
        super().__init__(isbn, title, author, year, price)
        self.stock = stock
    
    def buy(self, quantity, email, address):
        if self.stock < quantity:
            raise Exception("Papaer book not enough stcok")
        
        self.stock -= quantity
        total = self.price  * quantity
        print(f"Shipping paper book {self.title} ot {address}")
        return total


class EBook(Book):
    def __init__(self, isbn, title, author, year, price, file_type):
        super().__init__(isbn, title, author, year, price)
        self.file_type = file_type
        
    
    def buy(self, quantity, email, address):
        total = self.price * quantity
        print(f"we will send the {self.title} to the {address}")
        return total


