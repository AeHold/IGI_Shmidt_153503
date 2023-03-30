import re
import json
import os
from typing import Any, Set

class Container:
    username: str
    state: Set[Any]
    saved: bool
    
    def add(self, *args) -> None:
        if self.saved:
            self.saved = False

        print("Adding", *args)
        count = self.state.__len__()
        self.state.update(args)
        print(f"Were added {len(self.state) - count} elements")
    
    def remove(self, *args) -> None:
        if self.saved:
            self.saved = False
            
        print("Removing", *args)
        count = len(self.state)
        for item in args:
            if item in self.state:
                self.state.remove(item)
            else:
                print("There no such element")
        print(f"Were removed {len(self.state) - count} elements")

    def find(self, *args) -> None:
        count = 0
        for item in args:
            if item in self.state:
                print (f"Item {item} were found")
                count += 1
            else:
                print (f"{item} not found")
        if not count:
            print("No items were found")
        else:
            print(f"Were found {count} items")
    
    def list(self) -> None:
        print("Printing all elements from container")
        print(*self.state, sep = '\n')

    def grep(self, regex:str) -> None:
        count = 0
        for item in self.state:
            if (res := re.match(regex, item)):
                print(f"Matching pattern {item}")
                count += 1
            if not count:
                print("There are no items, matching by this regular expression")
            else:
                print(f"Found {count} matches")

    def switch(self, username) -> None:
        if self.state == username:
            print("You have already logged in this account")
            return
        self.load(username)
        
    def __init__(self, username):
        self.saved = True
        self.load(username)

    def load(self, username: str) -> None:
        if not self.saved:
            ans = input("Your data is not currently saved. Do you want to continue?(Y/N):")
            if ans != "Y":
                print("Loading new data without saving")
            else:
                self.save()
        print ("Loading...")
        data:dict = {}
        self.username = username
        try:
            with open("data.txt", "r+") as f:
                data = json.load(f)
                print(data)
        except FileNotFoundError:
            os.system("touch data.txt && echo {} >> data.txt")
            with open ("data.txt", "r+") as f:
                data = json.load(f)
                print(data)
        if not username in data:
            print("There are no such user in database. Creating...")
            self.state = set()
            self.save()
        else:
            self.state = set(data.get(username, []))
            self.saved = True

        print("Loaded:", *self.state)

    def save(self) -> None:
        if self.saved:
            print("Your data has been already saved")
            return
        
        data = None
        with open("data.txt", "r+") as f:
            data = json.load(f)
            data[self.username] = list(self.state)
        with open("data.txt", "w+") as f:
            json.dump(data, f)

        self.saved = True
        print("Data succesfully saved")

if __name__ == '__main__':
    username = input("Enter username to load data: ")
    container = Container(username)
while (cmd := input()) != "stop":
    match (cmd):
        case "add":
            elements = input("Enter element(elements) to add to container(splitting by /)")
            container.add(*(elements.split('/')))
        case "remove":
            elements = input("Enter element(elements) to remove from container(splitting by /)")
            container.remove(*(elements.split('/')))
        case "find":
            elements = input("Enter element(elements) to find them in container(splitting by /)")
            container.find(*(elements.split('/')))
        case "list":
            container.list()
        case "grep":
            regex = input("Enter regular expression to find elements)")
            container.grep(regex)
        case "switch":
            username = input("Enter username to switch user and load data: ")
            container.switch(username)
        case "save":
            container.save()
        case "load":
            username = input("Enter username to load data")
            container.load(username)
        case _:
            continue
if not container.saved:
    ans = input("Your data is not currently saved. Do you want to continue?(Y/N): ")
    if ans != "Y":
        print("Loading new data without saving")
    else:
        container.save()
        