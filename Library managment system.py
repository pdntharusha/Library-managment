from Books_class import Book
from Educational_DVD_class import Educational_DVD
from Lecture_CD_class import Lecture_CD
from Magazine_class import Magazine



class Library:
    def __init__(self):
        self.resources = []
        self.Book = []
        self.magazin = []
        self.education_dvd = []
        self.education_cd = []

    def add_resource(self, resources):
        self.resources.append(resources)
        print("Added to the library System Successfully..........!")

    def remove_resource(self, resources):
        if resource in self.resources:
            self.resources.remove(resources)
            print("Removed  from the library System Successfully............!")
        else:
            print("Resource not founded in the library System.")

    def available_resources(self, subject):

        available_resources = []

        if source == "Book":
            for Book in self.resources:
                if isinstance(Book, Book) and Book.subject == subject and Book.num_of_copies > 0:
                    available_resources.append(Book)
            return available_resources


        elif source == "Magazine":
            for magazine in self.resources:
                if isinstance(magazine, Magazine) and magazine.subject == subject and magazine.num_of_copies > 0:
                    available_resources.append(magazine)
            return available_resources



        elif source == "Educational DVD":

            for DVD in self.resources:
                if isinstance(DVD, Educational_DVD) and DVD.subject == subject and DVD.num_of_copies > 0:
                    available_resources.append(DVD)
            return available_resources

        elif source == "Lecture CD":

            for CD in self.resources:
                if isinstance(CD, Lecture_CD) and CD.subject == subject and CD.num_of_copies > 0:
                    available_resources.append(CD)
            return available_resources

    def unavailable_resourses(self, subject):
        unavailable_sourses = []
        if source == "Book":
            for Book in self.resources:
                if isinstance(Book, Book) and Book.subject == subject and Book.num_of_copies == 0:
                    unavailable_sourses.append(Book)
            return unavailable_sourses


        elif source == "Magazine":
            for magazine in self.resources:
                if isinstance(magazine, Magazine) and magazine.subject == subject and magazine.num_of_copies == 0:
                    unavailable_sourses.append(magazine)
            return unavailable_sourses


        elif source == "Lecture CD":
            for DVD in self.resources:
                if isinstance(DVD, Educational_DVD) and DVD.subject == subject and DVD.num_of_copies == 0:
                    unavailable_sourses.append(DVD)
            return unavailable_sourses


        elif source == "Educational DVD":
            for cd in self.resources:
                if isinstance(cd, Lecture_CD) and cd.subject == subject and cd.num_of_copies == 0:
                    unavailable_sourses.append(cd)
            return unavailable_sourses

    def update_Book(self, ISBN_NO):
        for Book in self.Book:
            if Book.ISBN_NO == ISBN_NO:
                Book.num_of_copies += 1
                print(
                    "Book with ISBN Number {ISBN_NO} has been updated. Total number of copies now available: {book.num_of_copies}")
                break
        else:
            print("No Book with ISBN Number {ISBN_NO} found in the library.")

    def filter_by_subject(self, subject):
        filtered_resources = []
        for resources in self.resources:
            if resources.subject == subject:
                filtered_resources.append(resources)
        if filtered_resources:
            for resources in filtered_resources:
                print(resources)
        else:

            print("No Books found for the subject: {subject}")


library = Library()

# Display the admin to choose 
while True:

    print("1. Add a new resource to the Library system.")
    print("2. Remove a resource from the Library system.")
    print("3. Available Resources.")
    print("4. Unavailable Resources.")
    print("5. update Resources.")
    print("6. filter by subjects")
    print("10. Quit")

    choice = int(input("Enter the number about your choice:"))

    if choice == 1:
        source = input(" Please enter what resource type do you want ........! (Book,Magazine/Educational DVD/Lecture CD)")

        if source == "Book":

            # Display the admin to enter the details to the system
            print("Enter the details to the system")
            isbn = input("ISBN Number: ")
            title = input("Title: ")
            format = input("Format (Hardcover or Paperback): ")
            while format not in ["Hardcover", "Paperback"]:
                print("Invalid format. Available formats: Hardcover, Paperback.")
                format = input("Format (Hardcover or Paperback): ")
            subject = input("Subject (Science, History or Literature): ")
            while subject not in ["Science", "History", "Literature"]:
                print("Invalid subject. Available subjects: Science, History, Literature.")
                subject = input("Subject (Science, History or Literature): ")
            rental_price = float(input("Rental price per a day: "))
            num_of_copies = int(input("Number of copies: "))
            print('Details added Successfully.........!')

            # Create a new Book object and add it to the library
            book = Book(isbn, title, format, subject, rental_price, num_of_copies)
            library.add_resource(book)

        elif source == "Magazine":
            # Display the admin to enter the details to the system
            print("Enter the details to the system:")
            magazine_no = input("magazine_no")
            title = input("Title: ")
            color = input("Magazine_color(black & white / color): ")
            while color not in ["black & white ", "color"]:
                print("Invalid color format. Available color format: black & white / color")
                color = input("Magazine_color(black & white / color): ")
            subject = input("Subject (Science, Technology and Sports): ")
            while subject not in ["Science", "Technology and Sports"]:
                print("Invalid subject. Available subjects: Science, Technology and Sports")
                subject = input("Subject (Science, Technology and Sport):")
            rental_price = float(input("Rental price per a day: "))
            num_of_copies = int(input("Number of copies: "))

            # Create a new Magazine and add it to the library
            magazin = Magazine(magazine_no, title, color, subject, rental_price, num_of_copies)
            library.add_resource(magazin)

        elif source == "Educational DVD":
            # Display the admin to enter the details to the system
            print("Enter the details to the system:")
            DVD_number = input("DVD_number")
            title = input("Title: ")

            subject = input("Subject (Astronomy, Math and Technology): ")
            while subject not in ["Astronomy", "Math and Technology"]:
                print("Invalid subject. Available subjects: Astronomy ,Math and Technology")
                subject = input("Subject (Astronomy, Math and Technology):")
            rental_price = float(input("Rental price per a day: "))
            num_of_copies = int(input("Number of copies: "))

            # Create a new Educational dvd and add it to the library
            education = Educational_DVD(DVD_number, title, subject, rental_price, num_of_copies)
            library.add_resource(education)

        elif source == "Lecture CD":
            # Display  the admin to enter the details to the system
            print("Enter the details to the system:")
            DVD_number = input("CD_number")
            title = input("Title: ")

            subject = input("Subject (Music, Math and Foreign Languages): ")
            while subject not in ["Music", "Math and Foreign Languages"]:
                print("Invalid subject. Available subjects: Music, Math and Foreign Languages")
                subject = input("Subject (Music, Math and Foreign Languages):")
            rental_price = float(input("Rental price per a day: "))
            num_of_copies = int(input("Number of copies: "))

            # Create a new Lecture CD and add it to the library
            education_cd = Lecture_CD(DVD_number, title, subject, rental_price, num_of_copies)
            library.add_resource(education_cd)



    elif choice == 2:

        source = input("Please enter what resource type do you want ........! (Book,Magazine/Educational DVD/Lecture CD)")

        if source == "Book":

            # Display the admin to enter the details to remove from the system
            print("Enter the details to remove from the system:")
            title = input("Title: ")
            resources_to_remove = [r for r in library.resources if r.title == title]

            # If there are many items to choose , admin can remove one from the system
            if len(resources_to_remove) > 1:
                print("Multiple resources found with that title:")
                for i, resource in enumerate(resources_to_remove):
                    print(f"{i + 1}. {resource}")
                index = int(input("Enter the number of the resource to remove: ")) - 1
                resource = resources_to_remove[index]
            elif len(resources_to_remove) == 1:
                resource = resources_to_remove[0]
            else:
                resource = None

            # Remove the item from the library
            if resource:
                library.remove_resource(resource)
            else:
                print("Resource not founded in the library System.")

        elif source == "Magazine":
            print("Enter the details to remove from the system:")
            title = input("Title: ")
            resources_to_remove = [r for r in library.resources if r.title == title]

            # If there are many items to choose , admin can remove one from the system
            if len(resources_to_remove) > 1:
                print("Multiple resources found with that title:")
                for i, resource in enumerate(resources_to_remove):
                    print(f"{i + 1}. {resource}")
                index = int(input("Enter the number of the resource to remove: ")) - 1
                resource = resources_to_remove[index]
            elif len(resources_to_remove) == 1:
                resource = resources_to_remove[0]
            else:
                resource = None

            # Remove the item from the library
            if resource:
                library.remove_resource(resource)
            else:
                print("Resource not founded in the library System.")

        elif source == "Educational DVD":
            print("Enter the details to remove from the system:")
            title = input("Title: ")
            resources_to_remove = [r for r in library.resources if r.title == title]

            # If there are many items to choose , admin can remove one from the system
            if len(resources_to_remove) > 1:
                print("Multiple resources found with that title:")
                for i, resource in enumerate(resources_to_remove):
                    print(f"{i + 1}. {resource}")
                index = int(input("Enter the number of the resource to remove: ")) - 1
                resource = resources_to_remove[index]
            elif len(resources_to_remove) == 1:
                resource = resources_to_remove[0]
            else:
                resource = None

            # Remove the item from the library
            if resource:
                library.remove_resource(resource)
            else:
                print("Resource not founded in the library System.")

        elif source == "Lecture CD":
            print("Enter the details to remove from the system:")
            title = input("Title: ")
            resources_to_remove = [r for r in library.resources if r.title == title]

            # If there are many items to choose , admin can remove one from the system
            if len(resources_to_remove) > 1:
                print("Multiple resources found with that title:")
                for i, resource in enumerate(resources_to_remove):
                    print(f"{i + 1}. {resource}")
                index = int(input("Enter the number of the resource to remove: ")) - 1
                resource = resources_to_remove[index]
            elif len(resources_to_remove) == 1:
                resource = resources_to_remove[0]
            else:
                resource = None

            # Remove the items from the library
            if resource:
                library.remove_resource(resource)
            else:
                print("Resource not founded in the library System.")



    elif choice == 3:

        source = input("Please enter what resource type do you want ........! (Book,Magazine/Educational DVD/Lecture CD)")
        if source == "Book":
            print("Available books:")
            for Book in library.available_resources("Science"):
                print(Book.title)

        elif source == "Magazine":
            print("Available Technology and Sports Books:")
            for magazine in library.available_resources("Technology and Sports"):
                print(magazine.title)

        elif source == "Educational DVD":
            print("Available Math and Technology Books:")
            for DVD in library.available_resources(" Math and Technology "):
                print(DVD.title)

        elif source == "Lecture CD":
            print("Available Math and Foreign Languages Books:")
            for cd in library.available_resources("Math and Foreign Languages"):
                print(cd.title)




    elif choice == 4:

        source = input("Please enter what resource type do you want ........! (Book,Magazine/Educational DVD/Lecture CD)")
        if source == "Book":
            print("Unavailable History Books:")
            for Book in library.unavailable_resourses("History"):
                print(Book.title)

        elif source == "Magazine":
            print("Unavailable History Books:")
            for magazine in library.unavailable_resourses("History"):
                print(magazine.title)

        elif source == "Educational DVD":
            print("Unavailable History Books:")
            for DVD in library.unavailable_resourses("History"):
                print(DVD.title)

        elif source == "Lecture CD":
            print("Unavailable History Books:")
            for cd in library.unavailable_resourses("History"):
                print(cd.title)




    elif choice == 5:

        ISBN_NO = input("Enter the ISBN Number of the Book received back: ")
        library.update_Book(ISBN_NO)







    elif choice == 6:
        source = input("Please enter what resource type do you want ........! (Book,Magazine/Educational DVD/Lecture CD)")
        if source == "Book":
            subject = input("Enter the subject to filter by: ")
            library.filter_by_subject(subject)

        elif source == "Magazine":
            subject = input("Enter the subject to filter by: ")
            library.filter_by_subject(subject)

        elif source == "Educational DVD":
            subject = input("Enter the subject to filter by: ")
            library.filter_by_subject(subject)

        elif source == "Lecture CD":
            subject = input("Enter the subject to filter by: ")
            library.filter_by_subject(subject)

 # Exit from the program

    elif choice == 10:
       
        break

    else:
        print("Invalid choice. Please enter 1, 2,4,5,6,7, or 10.")




