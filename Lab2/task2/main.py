import os

from constants import HELLO_MSG
from entities import User


if __name__ == '__main__':
    user: User = User(input("Enter username to load data: "))
    print(HELLO_MSG)

    while (cmd := input()) != "stop":
        os.system("clear")
        print("Results")
        print('-'*40)

        match (cmd):
            case "add":
                elements = input("Enter element(elements) to add to container(splitting by /): ")
                user.add(*(elements.split('/')))
            case "remove":
                elements = input("Enter element(elements) to remove from container(splitting by /): ")
                user.remove(*(elements.split('/')))
            case "find":
                elements = input("Enter element(elements) to find them in container(splitting by /): ")
                user.find(*(elements.split('/')))
            case "list":
                user.list()
            case "grep":
                regex = input("Enter regular expression to find elements: ")
                user.grep(regex)
            case "switch":
                username = input("Enter username to switch user and load data: ")
                user.switch(username)
            case "save":
                user.save()
            case "load":
                username = input("Enter username to load data: ")
                user.load(username)
            case _:
                continue

        print('-' * 40)
        print(HELLO_MSG)

    if not user.container.saved:
        ans = input("Your data is not currently saved. Do you want to continue?(Y/N): ")
        if ans != "Y":
            print("Data wasn't saved. Goodbye.")
        else:
            print("Data was saved. Goodbye.")
            user.save()
            