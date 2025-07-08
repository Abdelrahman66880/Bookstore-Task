from bookstore import Inventory, BookFactory

class BookStorFulltest:
    @staticmethod
    def run_tests():
        inventory = Inventory()
        
        paper_book = BookFactory.create_book(
            "PaperBook", 
            isbn = "U012",
            title = "DataStructure", 
            author="Abdelrahman Mohammed",
            year=2010,
            price= 50,
            stock=10
        )
        
        inventory.add_book(paper_book)


if __name__ == "__main__":
    BookStorFulltest.run_tests()