from typing import Any, Set

class Container:
    username: str
    state: Set[Any]
    saved: bool
    
    def add(self, *args) -> None:
        print("Adding", *args)
        count = self.state.__len__()
        self.state.update(args)
        print(f"Were added {len(self.state) - count} elements")
    
    def remove(self, *args) -> None:
        print("Removing", *args)
        count = len(self.state)
        for item in args:
            if item in self.state:
                self.state.remove(item)
            else:
                print("There no such element")
        print(f"Were removed {len(self.state) - count} elements")
