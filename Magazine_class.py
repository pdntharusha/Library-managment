class Magazine:
    def __init__(self, magazine_no, title, Magazine_color, subject, rental_price, num_of_copies):
        self.magazine_no = magazine_no
        self.title = title
        self.Magazine_color = Magazine_color
        self.subject = subject
        self.rental_price = rental_price
        self.num_of_copies = num_of_copies

    def __str__(self):
        return "{self.magazine_no}, {self.title}, {self.Magazine_color}, {self.subject}, {self.rental_price}" \
               ", {self.num_of_copies}"
