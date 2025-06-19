import random
import string
import itertools
import sys

class User:
    id = itertools.count(1)

    def __init__(self, name, password, rating):
        self.id = next(User.id)
        self.name = name
        self.password = password
        self.rating = rating

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Password: {self.password}, Rating: {self.rating}"


class UsersManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        name = "".join(random.choice(string.ascii_letters) for _ in range(10))
        password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(8, 12)))
        rating = random.randint(0, 100)
        user = User(name, password, rating)
        self.users.append(user)

    def show_all_users(self):
        if not self.users:
            print("Users list is empty")
        else:
            for user in self.users:
                print(user)

    def top_users(self):
        if not self.users:
            print("Users list is empty")
        else:
            top = max(self.users, key=lambda user: user.rating)
            print(f"User with highest rating is {top}")

    def save_to_file(self):
            with open("Users.txt", "w") as file:
                for user in self.users:
                    file.write(str(user))
                    file.write("\n")

    def load_from_file(self, filename):
        try:
            with open(filename) as file:
                for line in file:
                    part = line.strip().split(", ")
                    if len(part) == 4:
                        id_part, name_part, password_part, rating_part = part
                        name = name_part.split(": ")[1]
                        password = password_part.split(": ")[1]
                        rating = int(rating_part.split(": ")[1])
                        user = User(name, password, rating)
                        self.users.append(user)

        except FileNotFoundError:
            print(f"Error: Source file '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred during file copy: {e}")


manager = UsersManager()

val = -1
while val != 0:
    print("1. Додати користувача\n"
          "2. Переглянути всіх користувачів\n"
          "3. Топ користувач\n"
          "4. Зберегти\n"
          "5. Завантажити\n"
          "0. Вийти")
    try:
        val = int(input(">> "))
        if val < 0 or val > 5:
            raise ValueError
    except ValueError:
        print("Вводьте лише числа 0-5")
    else:
        match val:
            case 0:
                sys.exit(0)
            case 1:
                manager.add_user()
                print("Користувача додано!")
            case 2:
                print("Список всіх користувачів: ")
                manager.show_all_users()
            case 3:
                print("Топ користувач: ")
                manager.top_users()
            case 4:
                manager.save_to_file()
                print("Дані збережено у файл.")
            case 5:
                try:
                    manager.load_from_file(input("Введіть файл який хочете завантажити (.txt): "))
                except FileNotFoundError:
                    print("Файл не знайдено")