#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            self.show_error("height")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            self.show_error("age")

    def show_error(self, field: str) -> None:
        print(f"{self._name}: Error, {field} can't be negative")
        print(f"{field.capitalize()} update rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def grow(self, amount=5.0) -> None:
        self._height += amount
        self._stats._grow += 1

    def age_up(self) -> None:
        self._age += 1

    def growing(self, days: int) -> None:
        for _ in range(days):
            self.grow()
            self.age_up()

    def report_stats(self) -> None:
        self._stats.display()

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stats._show += 1

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def check_is_older_than_year(days: int) -> bool:
        return days > 365


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int = 0):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def grow(self, amount: float = 5.0):
        was_bloomed = self.bloomed
        super().grow(amount)
        if self.bloomed and not was_bloomed:
            self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant):
    print(f"[statistics for {plant._name}]")
    plant.report_stats()


class Tree(Plant):
    class Shadow(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    days = 30
    print(
        f"Is {days} days more than a year? ->",
        Plant.check_is_older_than_year(days)
        )
    days = 400
    print(
        f"Is {days} days more than a year? ->",
        Plant.check_is_older_than_year(days)
        )
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "Red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()
    print("=== Seed")
    sunflow = Seed("Sunflower", 80.0, 45, "yellow", 1)
    sunflow.show()
    display_stats(sunflow)
    print(f"[make {sunflow._name} grow, age and bloom]")
    sunflow.growing(20)
    sunflow.bloom()
    sunflow.show()
    display_stats(sunflow)
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous_plant()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
