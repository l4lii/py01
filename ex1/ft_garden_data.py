#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_garden_data() -> None:
    plant = [Plant("Rose", 25, 30),
             Plant("Sunflower", 80, 45),
             Plant("Cactus", 15, 120)]
    for p in plant:
        p.show()

def main() -> None:
    print("=== Garden Plant Registry ===")
    ft_garden_data()

if __name__ == "__main__":
    main()