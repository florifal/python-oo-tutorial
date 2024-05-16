class WeatherStation:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name != "":
            self.__name = name
        else:
            raise ValueError("Name must not be an empty string.")

    def add_observation(self, observation: str) -> None:
        if observation != "":
            self.__observations.append(observation)
        else:
            raise ValueError("Observation must not be an empty string.")

    def number_of_observations(self):
        return len(self.__observations)

    def latest_observation(self):
        return self.__observations[-1] if self.number_of_observations() > 0 else ""

    def __str__(self):
        return f"{self.name}, {self.number_of_observations()} observation{'s' * (self.number_of_observations() != 1)}"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    print(station)
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

    print()

    station = WeatherStation("Portland")
    try:
        station.name = ""
    except Exception as e:
        print(e)
    print(station.name)
    print(station)
