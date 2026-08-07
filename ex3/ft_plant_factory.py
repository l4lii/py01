#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    plant = [Plant("Rose", 25, 30),
             Plant("Oak", 200, 365),
             Plant("Cactus", 5, 90),
             Plant("Sunflower", 80, 45),
             Plant("Fern", 15, 120)]
    for p in plant:
        print("Created:", end=" ")
        p.show()


def main() -> None:
    print("\033[32m", "=== Plant Factory Output ===", "\033[0m")
    ft_plant_factory()


if __name__ == "__main__":
    main()
