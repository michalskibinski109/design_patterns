import time
import numpy as np
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, data: dict):
        self.data = data


class Subject(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def registerObserver(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        pass


class WeatherStation(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.temperature = np.random.randint(-10, 30)
        self.windspeed = np.random.randint(-10, 30)
        self.pressure = np.random.randint(-10, 30)

    def getState(self):
        return {'temperature': self.temperature, 'windspeed': self.windspeed, 'pressure': self.pressure}

    def setState(self):
        self.temperature = np.random.randint(-10, 30)
        self.windspeed = np.random.randint(-10, 30)
        self.pressure = np.random.randint(-10, 30)
        self.notifyObservers()

    def notifyObservers(self):
        for obs in self.observers:
            obs.update(self.getState())


class AlertSystem(Observer):

    def update(self, data: dict):
        super().update(data)
        self.alert()

    def alert(self):
        if self.data['temperature'] < 5:
            print('COLD ALERT')


class Logger(Observer):

    def update(self, data: dict):
        super().update(data)
        self.log()

    def log(self):
        print(self.data)

if __name__ == '__main__':
    station = WeatherStation()
    logger = Logger()
    alert = AlertSystem()
    station.registerObserver(alert)
    station.registerObserver(logger)
    for i in range(10):
        station.setState()
        time.sleep(2)
