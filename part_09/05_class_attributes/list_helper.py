class ListHelper:

    def __init__(self):
        pass

    @classmethod
    def get_item_counts(cls, my_list: list) -> dict:
        counting_dict = {}
        for item in my_list:
            if item not in counting_dict.keys():
                counting_dict[item] = 1
            else:
                counting_dict[item] += 1
        return counting_dict

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counting_dict = ListHelper.get_item_counts(my_list)

        most_frequent_item = ""
        highest_frequency = 0
        for key, value in counting_dict.items():
            if value > highest_frequency:
                highest_frequency = value
                most_frequent_item = key

        return most_frequent_item

    @classmethod
    def doubles(cls, my_list: list) -> list:
        counting_dict = ListHelper.get_item_counts(my_list)

        return [key for key, value in counting_dict.items() if value >= 2]

    @classmethod
    def doubles_count(cls, my_list: list) -> int:
        return len(ListHelper.doubles(my_list))


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.get_item_counts(numbers))
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
    print(ListHelper.doubles_count(numbers))
