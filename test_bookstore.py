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
            stock=10,
        )
        
        ebook = BookFactory.create_book(
            "EBook",
            isbn="U013",
            title="Algorithms", 
            author="Eng. Abdelrahman Mohammed",
            year=2020,
            price=30,
            file_type="pdf",
        )
        
        showcase_book = BookFactory.create_book(
            'ShowcaseBook',
            isbn='U001',
            title='Machine learning',
            author='Dr. Mohammed Fathi',
            year=1995
        )
        
        
        # the add process in the inveotary
        inventory.add_book(paper_book)
        inventory.add_book(ebook)
        inventory.add_book(showcase_book)
        
        
        # Remove outdated books which they are greateer than 15 years
        inventory.remove_outdated_books(15)
        
        try:
            inventory.buy_book('U012', 2, email='starnger@example.com', address='123 Quantum St')
        except Exception as e:
            print(e)

        try:
            inventory.buy_book('U013', 1, email='stranger@example.com', address='')
        except Exception as e:
            print(e)

        try:
            inventory.buy_book('U001', 1, email='stranger@example.com', address='')
        except Exception as e:
            print(e)
        

if __name__ == "__main__":
    BookStorFulltest.run_tests()