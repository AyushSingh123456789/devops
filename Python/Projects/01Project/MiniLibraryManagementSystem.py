class Members:
    def __init__(self, member_name, book_name):
        self.member_name = member_name
        self.book_name = book_name


# class Library:
#     def __init__(self):
#         book = Members(member_name, book_name)
      
class Books():
    
    def __init__(self):
        self.books = ["A Tale of Two Cities", "The Little Prince", "The Lord Of The Rings", "The Alchemist", "Bhagavad Gita", "Scouting For Boys"]
    
    def borrowed_books(self, member_name, book_name):
        for book in self.books:
            if book.lower() == book_name.lower():
                self.books.remove(book)
                print(f"Book named {book} has been successfully borrowed to {member_name}")
                return
        print("Sorry, the book {book} is not available right now")
            
    def returned_books(self, member_name, book_name):
        if book_name in self.books:
            print(f"{book_name} is already in the library")
            return
        self.books.append(book_name)
        print(f"The book {book_name} has been returned successfully by {member_name}")
        
    def display_books(self):
        print(", ".join(self.books))
        

          
book = Books()

while True:

    choice = input("Enter your choice: \n1)Borrow a Book \n2)Return a Book \n3)Display all the available books \n4)Quit \n")
    if choice == "1":
        member_name = input("Enter your name: ")
        book_name = input("Enter the name of the book you're borrowing: ")
        book.borrowed_books(member_name, book_name)
        
    elif choice == "2":
        member_name = input("Enter your name: ")
        book_name = input("Enter the name of the book you're returning: ")
        book.returned_books(member_name, book_name)
        
    elif choice == "3":
        book.display_books()
        
    elif choice == "4":
        print("Bye")
        break
