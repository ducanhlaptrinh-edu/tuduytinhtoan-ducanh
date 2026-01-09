class Book() : 
    def __init__(self , title , author , year) : 
        self.title = title
        self.author = author
        self.year = int(year)

class Library() : 
    def __init__(self) : 
        self.books = []

    def add(self , book) : 
        self.books.append(book)

    def count_by_author(self , name) : 
        count = 0 
        for book in self.books : 
            if book.author == name : 
                count += 1 
        return count

    def find_by_year(self , year) : 
        count = 0 
        for book in self.books : 
            if book.year == year : 
                count += 1 
        return count

if __name__ == "__main__" : 
    library = Library() # tạo một biến library duy nhất và dùng đi dùng lại , tránh gọi nhiều Library() nó sẽ tạo ra library mới rỗng
    n = int(input("Enter the number of operations : "))
    for _ in range(n) : 
        user_input = input()
        parts = user_input.split(' ', 1)
        command = parts[0]
        descr = parts[1]

        if command == "ADD" : 
            inf_book = descr.split(";")
            book = Book(inf_book[0],inf_book[1],inf_book[2])
            library.add(book)

        elif command == "COUNT" : 
            author = descr
            print(library.count_by_author(author))

        elif command == "COUNTYEAR" :
            year = int(descr)
            print(library.find_by_year(year))


