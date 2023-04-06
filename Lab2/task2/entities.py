import re
import pickle
import os
from typing import Any

from constants import LOAD_QUESTION


class User:
    
    def __init__(self, username) -> None:
        self.username = username
        self.container: Container = Container(False)
        if not os.path.exists(f"/home/aehold/githab/IGI_Shmidt_153503/Lab2/task2/data/{username}.pkl"):
            self.data = set()
            return
        answer = input(LOAD_QUESTION.format(username))
        if answer == "Y":
            self.load(self.username)
            return
        
        print("Continue without loading data...")

    def load(self, new_username):
        self.container.load(new_username)

    def add(self, *args):
        self.container.add(*args)

    def remove(self, *args):
        self.container.remove(*args)

    def find(self, *args):
        self.container.find(*args)
    
    def grep(self, regex: str):
        self.container.grep(regex)
    
    def list(self):
        self.container.list()

    def save(self):
        self.container.save(self.username)

    def switch(self, new_username):
        self.container.switch(new_username)
        self.username = new_username


class Container:

    def __init__(self, saved):
        self.saved: bool = saved
        self.data: set[Any] = set()    

    def add(self, *args) -> None:
        self.saved = False

        print("Adding", *args)

        count = self.data.__len__()
        self.data |= set(args)

        print(f"{len(self.data) - count} elements were added")
    
    def remove(self, *args) -> None:
        self.saved = False
            
        print("Removing", *args)

        count = len(self.data)
        self.data -= set(args)

        print(f"{count - len(self.data)} elements were removed")

    def find(self, *args) -> None:
        count = 0

        for item in args:
            if item in self.data:
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
        print(*self.data, sep = '\n')

    def grep(self, regex:str) -> None:
        count = 0
        for item in self.data:
            if (res := re.match(regex, item)):
                print(f"Matching pattern {item}")
                count += 1
            if not count:
                print("There are no items, matching by this regular expression")
            else:
                print(f"Found {count} matches")

    def switch(self, new_username) -> None:
        if not os.path.exists(f"/home/aehold/githab/IGI_Shmidt_153503/Lab2/task2/data/{new_username}.pkl"):
            self.data = set()
            return
        
        answer = input(LOAD_QUESTION.format(new_username))
        if answer == "Y":
            self.load(new_username, switch = True)
            return
        
        self.data = set()
        print("Continue without loading data...")
      
    def load(self, username: str, switch = False) -> None:
        print ("Loading...")

        try:
            with open(f"/home/aehold/githab/IGI_Shmidt_153503/Lab2/task2/data/{username}.pkl", "rb") as f:
                self.data = (
                    self.data | pickle.load(f) if not switch 
                    else pickle.load(f)
                )
        except FileNotFoundError:
            self.data = set()

        print("Loaded:", *self.data)

    def save(self, username) -> None:
        if self.saved:
            print("Your data has been already saved")
            return
        
        with open(f"/home/aehold/githab/IGI_Shmidt_153503/Lab2/task2/data/{username}.pkl", "wb+") as f:
            pickle.dump(self.data, f)

        self.saved = True
        print("Data succesfully saved")