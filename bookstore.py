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


class ShowcaseBook(Book):
    def __init__(self, isbn, title, author, year):
        super().__init__(isbn, title, author, year, price = 0)
    
    def buy(self, quantity, email, address):
        raise Exception(f"{self.title} is not for sale")

# ===================================
# BUILD THE FACTORY
# ===================================

class BookFactory:
    @staticmethod
    def create_book(book_type, **kwargs):
        if book_type == "PaperBook":
            return PapaerBook(**kwargs)
        elif book_type == "EBook":
            return EBook(**kwargs)
        elif book_type == "ShowcaseBook":
            return ShowcaseBook(**kwargs)
        else:
            raise Exception("Invalid Book Type")
        

# ========================================
# Iventory Managment
# ========================================


class Inventory:
    def __init__(self):
        self.books = {}
    
    
    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"The {book.title} is added to the inventory")
    
    
    def remove_outdated_books(self, years_threshold):
        current_year = datetime.now().year
        outdated_books = [isbn for isbn, book in self.books.items() if book.is_outdated(current_year, years_threshold)]
        for isbn in outdated_books:
            removed_book = self.books.pop(isbn)
            print("Removed Outdated books")
        return outdated_books
    
    def buy_book(self, isbn, quantity, email, address):
        if isbn not in self.books:
            raise Exception("Quantum book store: Book not found")
        book = self.books[isbn]
        paid_amount = book.buy(quantity, email, address)
        print(f"Quantum book store: Paid amount: ${paid_amount}")
        return paid_amount