#!/usr/bin/env python3

class Plant:
    def __init__(self, name : str, height : float, age : int) -> None:
        self.name = name
        self.height = 0.0
        self.age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}: {self.height}cm, {self.age} days old")
    
    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(float(height), 1)

def set_age(self, age) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

def ft_garden_security() -> None:
     print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()
    rose.set_height(-5)
    rose.set_age(-5)
    print()
    print(f"Current state: {rose._name}: {rose.get_height()}cm, {rose.get_age()} days old")


if __name__ == "__main__":
    ft_garden_security()
