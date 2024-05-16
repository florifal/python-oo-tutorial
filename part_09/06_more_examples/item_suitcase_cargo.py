class Item:

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, name: str):
    #     self.__name = name
    #
    # @property
    # def weight(self):
    #     return self.__weight
    #
    # @weight.setter
    # def weight(self, weight: int):
    #     self.__weight = weight

    # To comply exactly with the exercise:

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

    def __int__(self):
        return self.weight()


class Suitcase:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def __str__(self):
        return f"{self.item_count()} item{'s' * (self.item_count() != 1)} ({self.weight()} kg)"

    def weight(self):
        return sum([item.weight() for item in self.__items])

    def item_count(self):
        return len(self.__items)

    def add_item(self, item: Item) -> None:
        if not self.weight() + item.weight() > self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        current_heaviest = None
        current_weight = 0
        for item in self.__items:
            if item.weight() > current_weight:
                current_weight = item.weight()
                current_heaviest = item
        return current_heaviest


class CargoHold:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def __str__(self):
        return f"{self.suitcase_count()} suitcases, space for {self.__max_weight - self.weight()} kg"

    def weight(self):
        return sum([suitcase.weight() for suitcase in self.__suitcases])

    def suitcase_count(self):
        return len(self.__suitcases)

    def add_suitcase(self, suitcase: Suitcase) -> None:
        if not self.weight() + suitcase.weight() > self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":

    # Part 1: Item

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)

    print("")

    # Part 2: Suitcase and Part 3: Mind your language

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)

    print("")

    # Part 4: All the items

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

    print("")

    # Part 5: The heaviest item

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

    print("")

    # Part 6: Cargo hold

    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

    falcon_heavy = Suitcase(10000)
    tesla_roadster = Item("Tesla Roadster", 1250)
    falcon_heavy.add_item(tesla_roadster)
    cargo_hold.add_suitcase(falcon_heavy)
    print(cargo_hold)

    print("")

    # Part 7: The contents of the cargo hold

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
