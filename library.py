from Pyro5.api import Daemon, serve, expose
from datetime import datetime


@expose
class library(object):
    def __init__(self):
        self.users = {}
        self.authors = {}
        self.books = {}
        self.users_loans = {}

    def add_user(self, name, id):
        self.users[name] = {'id': id}
        self.users[name]['book_info'] = dict()

    def return_users(self):
        return self.users

    def delete_user(self, name):
        if self.users[name] == name and self.users_loans[name] == 0:
            del self.users[name]
            return 1
        else:
            return 0

    def add_author(self, name, category):
        self.authors[name] = category

    def return_authors(self):
        return self.authors

    # def return_books(self):
    #     return self.books

    def add_book_copy(self, author, title):
        if title in self.books:
            self.books[title]['copies'] += 1
        else:
            self.books[title] = {'author': author, 'copies': 1}

    def return_books_not_loan(self):
        books_not_loan = {}
        for title, book_info in self.books.items():
            if book_info['copies'] > 0:
                books_not_loan[title] = book_info['author']
        return books_not_loan

    def loan_book(self, user, title, year, month, day):
        if title not in self.books:
            return 0
        else:
            if self.books[title]['copies'] == 0:
                return 0
            else:
                self.users_loans[user] = 1
                loan_date = [year, month, day]
                self.users[user]['book_info'].update({
                    title: [self.books[title]['author'], loan_date]})
                self.books[title]['copies'] -= 1
                self.books[title][user] = loan_date
                return 1

    def return_books_loan(self):
        books_loan = {}
        for title, book_info in self.books.items():
            if len(book_info) > 2:
                books_loan[title] = str(self.books[title]['copies'] +
                                        len(book_info) - 2)+' '+'copies have been borrowed'
        if books_loan:
            return books_loan
        else:
            return 'No books have been borrowed'

    def end_book_loan(self, user, title, year, month, day):
        if user in self.books[title]:
            self.books[title].pop(user)
            self.books[title]['copies'] += 1
        else:
            self.books[title] = {'author': self.users[user]
                                 ['book_info'][title][0], 'copies': 1}
        self.users[user]['book_info'][title].append(
            [year, month, day])

    def delete_book(self, title):
        if title in self.books:
            del self.books[title]

    def user_loans_date(self, user, start_year, start_month, start_day, end_year, end_month, end_day):
        if user not in self.users:
            return "Invalid user"
        user_loans = []
        C = datetime(start_year, start_month, start_day)
        D = datetime(end_year, end_month, end_day)
        for title, book_info in self.users[user]['book_info'].items():
            A = datetime(book_info[1][0], book_info[1][1], book_info[1][2])
            B = datetime(book_info[2][0], book_info[2][1], book_info[2][2])
            if C <= A <= D and C <= B <= D:
                user_loans.append(title)
        if user_loans:
            return user_loans
        else:
            return 'this user has not borrowed any books in this time period'


P1 = library()
daemon = Daemon()

serve({library: "example.library"}, daemon=daemon, use_ns=True)
