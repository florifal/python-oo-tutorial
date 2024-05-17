class ShoppingList:

    def __init__(self):
        self._entries = []

    def add(self, name: str, amount: str):
        self._entries.append((name, amount))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self._entries):
            entry = self._entries[self.n]
            self.n += 1
            return entry
        else:
            raise StopIteration


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")