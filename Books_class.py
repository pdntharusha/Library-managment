class Book:
    def __init__(self, ISBN_NO, title, Book_format, subject, rental_price, num_of_copies):
        self.ISBN_NO = ISBN_NO
        self.title = title
        self.format = Book_format
        self.subject = subject
        self.rental_price = rental_price
        self.num_of_copies = num_of_copies

    def __str__(self):
        return "{self.ISBN_NO}, {self.title}, {self.Book_format}, {self.subject}, {self.rental_price}, {self.num_of_copies}"
