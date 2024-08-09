class Educational_DVD:
    
    def __init__(self, DVD_number, title, subject, rental_price, num_of_copies):
        self.DVD_number = DVD_number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.num_of_copies = num_of_copies

    def __str__(self):
        return "{self.DVD_number}, {self.title},  {self.subject}, {self.rental_price}" \
               ", {self.num_of_copies}"
