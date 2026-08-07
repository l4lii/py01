#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, grow_len: float):
        self.name = name
        self.height = height
        self.age = age
        self.grow_len = grow_len
        self.total_grow = 0.0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age} days old\n")

    def grow(self) -> None:
        self.height += self.grow_len
        self.total_grow += self.grow_len

    def age_up(self) -> None:
        self.age += 1

def ft_plant_growth(plant_obj: Plant) -> None:
    print("\033[32m", "=== Garden Plant Growth ===", "\033[0m")
    plant_obj.show()
    for i in range(1, 8):
        print("\033[32m", f"=== Day {i} ===", "\033[0m")
        plant_obj.grow()
        plant_obj.age_up()
        plant_obj.show()
    print( "\033[32m", f"Growth this week: {plant_obj.total_grow}cm", "\033[0m")

def main() -> None:
    plant_data = Plant("Rose", round(25.0, 1), 30, 0.8)
    ft_plant_growth(plant_data)


if __name__ == "__main__":
    main()
