class Lecture_CD:
    
    def __init__(self, CD_number, title, subject, rental_price, num_of_copies):
        self.CD_number = CD_number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.num_of_copies = num_of_copies

    def __str__(self):
        return "{self.CD_number}, {self.title},  {self.subject}, {self.rental_price}" \
               ", {self.num_of_copies}"
