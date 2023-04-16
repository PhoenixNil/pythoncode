from Pyro5.api import Daemon, serve
from library import library


class Library:
    def __init__(self):
        self.users = {}
        self.authors = {}
        self.books = {}

    def add_user(self, name, id):
        self.users[id] = name

    def return_users(self):
        return self.users

    def delete_user(self, name):
        for id, user in self.users.items():
            if user == name:
                del self.users[id]

    def add_author(self, name, category):
        self.authors[name] = category

    def return_authors(self):
        return self.authors

    def add_book_copy(self, author, title):
        if author not in self.authors:
            print("Error: author not found")
        else:
            if title in self.books:
                self.books[title]['copies'] += 1
            else:
                self.books[title] = {'author': author, 'copies': 1}

    def return_books_not_loan(self):
        books_not_loan = []
        for title, book_info in self.books.items():
            if book_info['copies'] > 0:
                books_not_loan.append(title)
        return books_not_loan

    def loan_book(self, user, title, year, month, day):
        if title not in self.books:
            print("Error: book not found")
        else:
            if self.books[title]['copies'] == 0:
                print("Error: no copies available")
            else:
                loan_date = (year, month, day)
                self.books[title]['copies'] -= 1
                if user in self.users:
                    if user in self.books[title]:
                        self.books[title][user].append(loan_date)
                    else:
                        self.books[title][user] = [loan_date]
                else:
                    print("Error: user not found")

    def return_books_loan(self):
        books_loan = {}
        for title, book_info in self.books.items():
            if len(book_info) > 2:
                books_loan[title] = book_info
        return books_loan

    def end_book_loan(self, user, title, year, month, day):
        if title not in self.books:
            print("Error: book not found")
        else:
            loan_date = (year, month, day)
            if user in self.books[title]:
                if loan_date in self.books[title][user]:
                    self.books[title][user].remove(loan_date)
                    self.books[title]['copies'] += 1
                else:
                    print("Error: loan not found")
            else:
                print("Error: user not found")

    def delete_book(self, title):
        if title in self.books:
            del self.books[title]

    def user_loans_date(self, user, start_year, start_month, start_day, end_year, end_month, end_day):
        if user not in self.users:
            print("Error: user not found")
        else:
            user_loans = {}
            for title, book_info in self.books.items():
                if user in book_info:
                    for loan_date in book_info[user]:
                        if (start_year, start_month, start_day) <= loan_date <= (end_year, end_month, end_day):
                            if title in user_loans:
                                user_loans[title] += 1
                            else:
                                user_loans[title] = 1
            return user_loans


daemon = Daemon()

serve({library: "example.library"}, daemon=daemon, use_ns=True)
