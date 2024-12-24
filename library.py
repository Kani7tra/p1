class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.author} - {self.price} руб."


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.purchase_history = []

    def add_purchase(self, book):
        self.purchase_history.append(book)

    def __str__(self):
        return self.username


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return "Пользователь с таким именем уже существует."
        self.users[username] = User(username, password)
        return "Пользователь успешно зарегистрирован."

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return "Пользователь успешно удален."
        return "Пользователь не найден."


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return "Книга успешно удалена."
        return "Книга не найдена."

    def update_book(self, old_title, new_title, new_author, new_price):
        for book in self.books:
            if book.title == old_title:
                book.title = new_title
                book.author = new_author
                book.price = new_price
                return "Данные книги успешно обновлены."
        return "Книга не найдена."

    def list_books(self):
        if not self.books:
            return "Нет доступных книг."
        return "\n".join(str(book) for book in self.books)


def admin_menu(bookstore, user_manager):
    while True:
        print("\n--- Меню администратора ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Изменить данные книги")
        print("4. Удалить пользователя")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                price = float(input("Введите цену книги: "))
                bookstore.add_book(Book(title, author, price))
                print("Книга успешно добавлена.")
            except ValueError:
                print("Ошибка: Введите корректную цену.")

        elif choice == '2':
            title = input("Введите название книги для удаления: ")
            print(bookstore.remove_book(title))

        elif choice == '3':
            old_title = input("Введите текущее название книги: ")
            new_title = input("Введите новое название книги: ")
            new_author = input("Введите нового автора книги: ")
            try:
                new_price = float(input("Введите новую цену книги: "))
                print(bookstore.update_book(old_title, new_title, new_author, new_price))
            except ValueError:
                print("Ошибка: Введите корректную цену.")

        elif choice == '4':
            username = input("Введите имя пользователя для удаления: ")
            print(user_manager.remove_user(username))

        elif choice == '5':
            break


def user_menu(bookstore, user):
    while True:
        print("\n--- Меню пользователя ---")
        print("1. Просмотреть книги")
        print("2. Купить книгу")
        print("3. Просмотреть свою историю покупок")
        print("4. Изменить пароль")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nДоступные книги:")
            print(bookstore.list_books())

        elif choice == '2':
            print("\nДоступные книги:")
            print(bookstore.list_books())
            title = input("Введите название книги для покупки: ")
            for book in bookstore.books:
                if book.title == title:
                    user.add_purchase(book)
                    print(f"Вы купили книгу: {book}")
                    break
            else:
                print("Книга не найдена.")

        elif choice == '3':
            if user.purchase_history:
                print(f"История покупок пользователя {user.username}:")
                for book in user.purchase_history:
                    print(book)
            else:
                print("У вас нет истории покупок.")

        elif choice == '4':
            new_password = input("Введите новый пароль: ")
            user.password = new_password
            print("Пароль успешно изменен.")

        elif choice == '5':
            break


def main():
    bookstore = BookStore()
    user_manager = UserManager()

    initial_books = [
        ("1984", "Джордж Оруэлл", 500),
        ("Война и мир", "Лев Толстой", 700),
        ("Гарри Поттер", "Джоан Роулинг", 600),
        ("Преступление и наказание", "Федор Достоевский", 400),
        ("Мастер и Маргарита", "Михаил Булгаков", 550),
    ]

    for title, author, price in initial_books:
        bookstore.add_book(Book(title, author, price))

    while True:
        print("\n1. Войти как пользователь")
        print("2. Войти как администратор")
        print("3. Зарегистрироваться")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            user = user_manager.authenticate(username, password)
            if user:
                print(f"Добро пожаловать, {user.username}!")
                user_menu(bookstore, user)
            else:
                print("Неверное имя пользователя или пароль.")

        elif choice == '2':
            username = input("Введите имя администратора: ")
            password = input("Введите пароль администратора: ")
            if username == "Admin" and password == "1234":
                print("Добро пожаловать, администратор!")
                admin_menu(bookstore, user_manager)
            else:
                print("Неверное имя администратора или пароль.")

        elif choice == '3':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            print(user_manager.add_user(username, password))

        elif choice == '4':
            break


if __name__ == "__main__":
    main()
